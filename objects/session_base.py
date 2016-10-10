import binascii
import os

import bcrypt
from redis.exceptions import RedisError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from voluptuous import MultipleInvalid

from models.puppet_model import Account
from objects.io.output_manager import OutputManager
from objects.io.response_codes import ResponseCodes
from objects.puppet_base import PuppetBase
from utils.input_validation.input_error_parser import InputErrorParser
from utils.input_validation.input_validator import InputValidator


class SessionBase(PuppetBase):
    AUTH_TOKEN_LENGTH = 24
    AUTH_TOKEN_TTL = 86400  # seconds

    def __init__(self, account_id=None):

        super(SessionBase, self).__init__()

        self.puppet_db = self.get_db('puppet')
        self.session_db = self.get_cache('sessions')

        self.account_id = account_id
        self.auth_token = None

    def get_account_id(self):
        return self.account_id

    def get_auth_token(self):
        return self.auth_token

    def register_auth_token(self, auth_token=None):
        if auth_token:
            _account_id = self.session_db.get(auth_token)

            if _account_id:
                self.session_db.expire(auth_token, SessionBase.AUTH_TOKEN_TTL)
                self.account_id = _account_id
                self.auth_token = auth_token

    def protect(self):
        if not self.account_id:
            raise InvalidSession('Authorization failure')

    def create_session(self, **payload):
        _output = OutputManager()
        _validator_key = self.create_session.__name__

        try:
            # Validate user inputs
            InputValidator(_validator_key).validate(payload)

            try:
                _account = self.__get_account(email=payload['email'])

                # Compare user password with hash
                if self.__verify_password_hash(payload['password'], _account.password):
                    _new_token = binascii.hexlify(os.urandom(SessionBase.AUTH_TOKEN_LENGTH))
                    _new_token = _new_token.decode(encoding='utf-8')

                    try:
                        self.session_db.set(_new_token, _account.id)
                        self.session_db.expire(_new_token, SessionBase.AUTH_TOKEN_TTL)
                        self.session_db.rpush(_account.id, _new_token)
                        self.session_db.ltrim(_account.id, 0, 999)

                        return _output.output(
                            status=ResponseCodes.OK['success'],
                            data={
                                'auth_token': _new_token
                            }
                        )

                    except RedisError as e:
                        return _output.output(
                            status=ResponseCodes.INTERNAL_SERVER_ERROR['internalError']
                        )

                else:
                    return _output.output(
                        status=ResponseCodes.UNAUTHORIZED['authError']
                    )
            except (NoResultFound, MultipleResultsFound):
                return _output.output(
                    status=ResponseCodes.UNAUTHORIZED['authError']
                )
            except SQLAlchemyError:
                return _output.output(
                    status=ResponseCodes.INTERNAL_SERVER_ERROR['internalError']
                )

        except MultipleInvalid as e:
            error_parser = InputErrorParser()

            return _output.output(
                status=ResponseCodes.BAD_REQUEST['invalidQuery'],
                data=error_parser.translate_errors(e)
            )

    def delete_session(self):
        _output = OutputManager()

        try:
            self.protect()

            try:
                self.session_db.delete(self.auth_token)

            except RedisError:
                return _output.output(
                    status=ResponseCodes.INTERNAL_SERVER_ERROR['internalError']
                )

            return _output.output(
                status=ResponseCodes.OK['success']
            )

        except InvalidSession:
            return _output.output(
                status=ResponseCodes.UNAUTHORIZED['authError']
            )

    def delete_all_sessions(self):
        try:
            _account_tokens = self.session_db.lrange(self.account_id, 0, -1)
            self.session_db.delete(*_account_tokens)

        except RedisError:
            raise SessionError('Session database failure')

    def __get_account(self, account_id=None, email=None):
        if account_id:
            try:
                _account = self.puppet_db.query(
                    Account.id,
                    Account.email,
                    Account.first_name,
                    Account.last_name,
                    Account.password
                ).filter(
                    Account.id == account_id
                ).one()

                return _account
            except (NoResultFound, MultipleResultsFound, SQLAlchemyError) as e:
                raise e

        if email:
            try:
                _account = self.puppet_db.query(
                    Account.id,
                    Account.email,
                    Account.first_name,
                    Account.last_name,
                    Account.password
                ).filter(
                    Account.email == email
                ).one()

                return _account
            except (NoResultFound, MultipleResultsFound, SQLAlchemyError) as e:
                raise e

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(bytes(password, encoding='utf-8'), bcrypt.gensalt())

    @staticmethod
    def __verify_password_hash(password, pw_hash):
        return bcrypt.hashpw(bytes(password, encoding='utf-8'),
                             bytes(pw_hash, encoding='utf-8')) == bytes(pw_hash, encoding='utf-8')


class InvalidSession(ValueError):
    def __init__(self, message, *args):
        self.message = message  # without this you may get DeprecationWarning
        super(InvalidSession, self).__init__(message, *args)


class SessionError(Exception):
    def __init__(self, message, *args):
        self.message = message  # without this you may get DeprecationWarning
        super(SessionError, self).__init__(message, *args)

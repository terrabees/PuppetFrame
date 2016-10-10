from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from voluptuous import MultipleInvalid

from models.puppet_model import Account
from objects.io.output_manager import OutputManager
from objects.io.response_codes import ResponseCodes
from objects.session_base import SessionBase, SessionError, InvalidSession
from utils.input_validation.input_error_parser import InputErrorParser
from utils.input_validation.input_validator import InputValidator


class AccountBase(SessionBase):
    def __init__(self, account_id=None):
        super(AccountBase, self).__init__(account_id=account_id)

    def create_account(self, **payload):
        _output = OutputManager()
        _validator_key = self.create_account.__name__

        try:
            # Validate user inputs
            InputValidator(_validator_key).validate(payload)

            # Check if account already exists
            try:
                if self.__has_account(email=payload['email']):
                    return _output.output(
                        status=ResponseCodes.FORBIDDEN['accountExists'],
                        data={
                            'email': 'Email address is already associated with an existing account'
                        }
                    )
            except SQLAlchemyError:
                return _output.output(
                    status=ResponseCodes.INTERNAL_SERVER_ERROR['internalError']
                )

            # Hash the received password
            payload['password'] = self.hash_password(payload['password'])

            try:
                # Create a new account
                _new_account = Account(**payload)
                self.puppet_db.add(_new_account)
                self.puppet_db.commit()

                return _output.output(
                    status=ResponseCodes.OK['success']
                )
            except SQLAlchemyError:
                self.puppet_db.rollback()

                return _output.output(
                    status=ResponseCodes.INTERNAL_SERVER_ERROR['internalError']
                )

        except MultipleInvalid as e:
            error_parser = InputErrorParser()

            return _output.output(
                status=ResponseCodes.BAD_REQUEST['invalidQuery'],
                data=error_parser.translate_errors(e)
            )

    def update_account(self, **payload):
        _output = OutputManager()

        try:
            self.protect()

            _validator_key = self.update_account.__name__
            _update_list = {}

            try:
                # Validate user inputs
                InputValidator(_validator_key).validate(payload)

                if 'first_name' in payload:
                    _update_list[Account.first_name] = payload['first_name']

                if 'last_name' in payload:
                    _update_list[Account.last_name] = payload['last_name']

                if 'password' in payload:
                    # Hash the received password
                    _update_list[Account.password] = self.hash_password(payload['password'])

                if not _update_list:
                    return _output.output(
                        status=ResponseCodes.BAD_REQUEST['invalidQuery']
                    )

                else:
                    try:
                        # Update table with new values
                        self.puppet_db.query(Account).filter(
                            Account.id == self.get_account_id()
                        ).update(
                            _update_list
                        )

                        if 'password' in payload:
                            try:
                                self.delete_all_sessions()

                            except SessionError:
                                self.puppet_db.rollback()

                                return _output.output(
                                    status=ResponseCodes.INTERNAL_SERVER_ERROR['internalError']
                                )

                        self.puppet_db.commit()

                        return _output.output(
                            status=ResponseCodes.OK['success']
                        )

                    except SQLAlchemyError:
                        self.puppet_db.rollback()

                        return _output.output(
                            status=ResponseCodes.INTERNAL_SERVER_ERROR['internalError']
                        )

            except MultipleInvalid as e:
                error_parser = InputErrorParser()

                return _output.output(
                    status=ResponseCodes.BAD_REQUEST['invalidQuery'],
                    data=error_parser.translate_errors(e)
                )

        except InvalidSession:
            return _output.output(
                status=ResponseCodes.UNAUTHORIZED['authError']
            )

    def __has_account(self, email):
        try:
            self.puppet_db.query(
                Account.email
            ).filter(
                Account.email == email
            ).one()

            return True

        except MultipleResultsFound:
            return True

        except NoResultFound:
            return False

        except SQLAlchemyError as e:
            raise e

import json

from objects.account_base import AccountBase


class RouteAccount(object):
    @staticmethod
    def on_post(req, resp):
        _account = AccountBase()

        # Request body
        _payload = json.loads(str(req.stream.read(), encoding='utf-8'))
        # Execution
        _result = _account.create_account(**_payload)
        # Response handlers
        resp.status = _result.get('status', {}).get('code')
        resp.body = json.dumps(_result)

    @staticmethod
    def on_put(req, resp):
        _account = AccountBase()

        # Request body
        _payload = json.loads(str(req.stream.read(), encoding='utf-8'))
        # Authenticated execution
        _account.register_auth_token(req.auth)
        _result = _account.update_account(**_payload)
        # Response handlers
        resp.status = _result.get('status', {}).get('code')
        resp.body = json.dumps(_result)

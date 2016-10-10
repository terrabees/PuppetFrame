import json

from objects.session_base import SessionBase


class RouteSession(object):
    @staticmethod
    def on_post(req, resp):
        _payload = json.loads(str(req.stream.read(), encoding='utf-8'))

        _result = SessionBase().create_session(**_payload)

        resp.status = _result.get('status', {}).get('code')
        resp.body = json.dumps(_result)

    @staticmethod
    def on_delete(req, resp):
        _session = SessionBase()

        # Authenticated execution
        _session.register_auth_token(req.auth)
        _result = _session.delete_session()

        resp.status = _result.get('status', {}).get('code')
        resp.body = json.dumps(_result)

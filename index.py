import falcon

from routes import route_account, route_session

app = falcon.API()

# ## Routes ## #

account = route_account.RouteAccount()
app.add_route('/account', account)

session = route_session.RouteSession()
app.add_route('/session', session)

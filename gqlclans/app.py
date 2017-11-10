
from aiohttp import web
from aiohttp_graphql import GraphQLView

from gqlclans.schema import schema


app = web.Application()
app.router.add_get('/', lambda req: web.HTTPTemporaryRedirect(f'/graphiql?{req.query_string}'))

graphiql_view = GraphQLView(schema=schema, graphiql=True)
app.router.add_route('*', '/graphiql', graphiql_view)

graphql_view = GraphQLView(schema=schema, batch=True)
app.router.add_route('*', '/graphql', graphql_view)


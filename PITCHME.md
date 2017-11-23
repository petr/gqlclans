
# GraphQL And Clans

---

## Resources

- https://github.com/petr/gqlclans
- https://mm.wargaming.net/clans/channels/grahpql
- Image path in docker registry: sudoaptget/gqlclans
- https://gqlclans.sloppy.zone

---

## Docs

- http://docs.graphene-python.org/en/latest
- http://graphql.org/learn
- https://www.apollographql.com/docs/react/

---

## NO NDA

Based on https://developers.wargaming.net !

---

## Schema description

![Paper schema](https://github.com/petr/gqlclans/blob/master/images/paper_schema.jpeg?raw=true)

---

## Schema in python

```
    class Member(graphene.ObjectType):
        name = graphene.String()
        account_id = graphene.ID()
        role = graphene.String()

    class Message(graphene.ObjectType):
        body = graphene.String()

    class Clan(graphene.ObjectType):
        name = graphene.String()
        tag = graphene.String()
        clan_id = graphene.ID()
        color = graphene.String()
        members = graphene.List(Member)
        messages = graphene.List(Message)
```

---

## Schema and aioHttp

```
from aiohttp import web
from aiohttp_graphql import GraphQLView

from gqlclans.schema import schema

app = web.Application()

graphql_view = GraphQLView(schema=schema, batch=True)
app.router.add_route('*', '/graphql', graphql_view)

```

---

## Graphql Console

---

## CI

- creating pull request to master
- tests in cloud.docker start |
- new docker image in cloud.docker is created |
- Webhook "New image appear!" is triggered sloppy.io webhook and updates sloppy.io |

---

## Why use Apollo/Relay with GraphQL?

- Editor tooling (GraphQL IntelliJ plugin)
- Code generation for static typing |
- TypeScript/Flow integration |
- Server-side logging  |
- Persisted queries |

---

# JOIN US

https://github.com/petr/gqlclans

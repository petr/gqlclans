
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

![Paper schema](https://photos-2.dropbox.com/t/2/AAAdhky1jBy6Q79TueVcrwmbDqi8rdkXysvGTG3dyyZicg/12/7681788/jpeg/32x32/1/_/1/2/%D0%A4%D0%B0%D0%B9%D0%BB%2023.11.17%2C%2014%2011%2035.jpeg/EMS_2gUYzj8gBygH/eNW7KoYDuFWOmYtHx6pGb11J3jPJI0PhjW9JnwkXCP8?size=2048x1536&size_mode=3)

---

## Schema in python

https://github.com/petr/gqlclans/blob/master/gqlclans/schema.py

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

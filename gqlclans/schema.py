
import graphene

from gqlclans.logic import get_clan_info, search_clan


class Member(graphene.ObjectType):
    name = graphene.String()
    account_id = graphene.ID()
    role = graphene.String()

    class Meta:
        interfaces = (graphene.relay.Node,)


class MemberConnection(graphene.Connection):
    class Meta:
        node = Member


class Message(graphene.ObjectType):
    body = graphene.String()


class AddMessage(graphene.Mutation):
    class Arguments:
        body = graphene.String()
        clan_id = graphene.ID()

    success = graphene.Boolean()
    message = graphene.Field(lambda: Message)# lambda is nice pattern for describe relation with not loaded yet classes

    def mutate(self, info, body, clan_id):
        message = Message(body=body)
        success = True
        return AddMessage(message=message, success=success)


class Clan(graphene.ObjectType):
    name = graphene.String()
    tag = graphene.String()
    clan_id = graphene.ID()
    color = graphene.String()
    members = graphene.relay.ConnectionField(MemberConnection)
    messages = graphene.List(Message)

    class Meta:
        interfaces = (graphene.relay.Node,)

    @staticmethod
    def get_member(member):
        return Member(
            name=member['account_name'],
            account_id=member['account_id'],
            role=member['role']
        )

    def resolve_members(self, info, **kwargs):
        return [self.get_member(m) for m in self.members]


class ClanConnection(graphene.Connection):
    class Meta:
        node = Clan


class Mutation(graphene.ObjectType):
    add_message = AddMessage.Field()


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    ping = graphene.String()
    clans = graphene.relay.ConnectionField(ClanConnection, clan_id=graphene.String(default_value='20226'))
    search = graphene.relay.ConnectionField(ClanConnection, search_txt=graphene.String(default_value=''))

    def resolve_ping(context, info):
        return 'Ping success!'

    def resolve_clans(context, info, clan_id, *args, **kwargs):
        data = get_clan_info(clan_id)['data']
        return get_clans(data)

    def resolve_search(context, info, search_txt):
        result = search_clan(search_txt)['data']
        clan_ids = list(map(lambda clan: clan['clan_id'], result))
        clan_ids = ','.join(map(str, clan_ids))
        data = get_clan_info(clan_ids)['data']
        return get_clans(data)


def get_clans(data):
    clans = []
    for content in data.values():
        clans.append(
            Clan(
                name=content['name'],
                tag=content['tag'],
                clan_id=content['clan_id'],
                color=content['color'],
                members=content['members'],
                messages=[],
            ))
    return clans


schema = graphene.Schema(query=Query, mutation=Mutation)

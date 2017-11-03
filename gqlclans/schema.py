
import graphene

from gqlclans.logic import get_clan_info, search_clan


class Member(graphene.ObjectType):
    name = graphene.String()
    account_id = graphene.ID()
    role = graphene.String()


class Clan(graphene.ObjectType):
    name = graphene.String()
    tag = graphene.String()
    clan_id = graphene.ID()
    color = graphene.String()
    members = graphene.List(Member)



class Query(graphene.ObjectType):
    ping = graphene.String()
    clans = graphene.Field(
        graphene.List(Clan), clan_id=graphene.String(default_value='20226')
    )
    search = graphene.Field(
        graphene.List(Clan), search_txt=graphene.String(default_value='')
    )

    def resolve_ping(context, info):
        return 'Ping success!'

    '''
    Здесь мы должны получить запрос вида
    { 
        query(clanId: clan_id) { !!! Для того что бы был clan_id нужно в schema выключить настройку!
            name
            tag
        }
    }
    '''
    def resolve_clans(context, info, clan_id):
        data = get_clan_info(clan_id)['data']
        return parse_data(data)

    def resolve_search(context, info, search_txt):
        result = search_clan(search_txt)['data']
        clan_ids = list(map(lambda clan: clan['clan_id'], result))
        clan_ids = ','.join(map(str, clan_ids))
        data = get_clan_info(clan_ids)['data']
        return parse_data(data)


def parse_data(data):
    get_member = lambda member: Member(
        name=member['account_name'],
        account_id=member['account_id'],
        role=member['role']
    )
    clans = []
    for content in data.values():
        clans.append(
            Clan(
                name=content['name'],
                tag=content['tag'],
                clan_id=content['clan_id'],
                color=content['color'],
                members=map(get_member, content['members'])
            ))
    return clans


schema = graphene.Schema(query=Query)


import requests


CLAN_INFO = 'https://api.worldoftanks.ru/wgn/clans/info/?application_id=8c2d3111d4e93eaa2a6e008424123d6d&clan_id={}'
SEARCH_CLAN = 'https://api.worldoftanks.ru/wgn/clans/list/?application_id=8c2d3111d4e93eaa2a6e008424123d6d&fields=clan_id&game=wot&search={}'

def get_clan_info(clan_id):
    return requests.get(CLAN_INFO.format(clan_id)).json()


def search_clan(search_txt):
    return requests.get(SEARCH_CLAN.format(search_txt)).json()


def prepare_clans(data):
    clans = []
    for content in data.values():
        clans.append({

        })


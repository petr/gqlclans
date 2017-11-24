
import requests

CLAN_INFO = 'https://api.worldoftanks.ru/wgn/clans/info/?application_id=8c2d3111d4e93eaa2a6e008424123d6d&clan_id={}'
SEARCH_CLAN = 'https://api.worldoftanks.ru/wgn/clans/list/?application_id=8c2d3111d4e93eaa2a6e008424123d6d&fields=clan_id&game=wot&search={}'
SERVERS_INFO = 'https://api.worldoftanks.ru/wgn/servers/info/?application_id=8c2d3111d4e93eaa2a6e008424123d6d&game=wot'


class PapiRequestSession:
    session = None
    adapters = {}

    def __init__(self):
        self.session = requests.Session()
        for url, adapter in PapiRequestSession.adapters.items():
            self.session.mount(url, adapter)


def get_clan_info(clan_id):
    papi_request = PapiRequestSession()
    return papi_request.session.get(CLAN_INFO.format(clan_id)).json()


def search_clan(search_txt):
    papi_request = PapiRequestSession()
    return papi_request.session.get(SEARCH_CLAN.format(search_txt)).json()


def get_servers_info():
    papi_request = PapiRequestSession()
    return papi_request.session.get(SERVERS_INFO).json()

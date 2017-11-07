
import json

from graphene.test import Client
from gqlclans.schema import schema
from gqlclans.app import app


def test_ping():
    client = Client(schema)
    result = client.execute('{ ping }')
    assert result == {
        'data': {
            'ping': 'Ping success!'
        }
    }


QUERY = '''
query getUser($id: ID) {
        user(id: $id) {
            id
            firstName
            lastName
        }
    }
'''


def test_clan():
    query = '{ clans(clanId: "10164") { tag name }}'
    client = Client(schema)
    result = client.execute(query)
    assert result == {
        'data': {
            'clans': [
                {
                    'tag': 'BOUHA',
                    'name': 'Второй  всадник  апокалипсиса',
                }
            ]
        }
    }


def test_mutation():
    query = '''
        mutation TestTitle {
            addMessage(body: "Some text", clanId: "28"){
                message {
                    body
                }
                success
            }
        }
    '''
    client = Client(schema)
    result = client.execute(query)
    assert result == {
        'data': {
            'addMessage': {
                'message': {
                    'body': 'Some text',
                },
                'success': True
            }
        }
    }


async def test_app(test_client):
    client = await test_client(app)
    response = await client.get('/?query={clans{name tag}}')
    assert response.history[0].status == 307
    assert response.status == 200
    assert response.url.relative().human_repr() == '/graphiql?query={clans{name tag}}'

    response = await client.get('/graphql?query={ clans(clanId: "10164") { tag name }}')
    assert response.status == 200
    content = await response.content.read()
    assert json.loads(content) == {
        'data': {
            'clans': [{'tag': 'BOUHA', 'name': 'Второй  всадник  апокалипсиса'}]
        }
    }

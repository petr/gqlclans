
import json

from schema import schema
from app import app

def test_ping():
    query = '{ ping }'
    result = schema.execute(query)

    assert hasattr(result, 'data'), 'No attribute data in result'
    assert 'ping' in result.data, 'No ping key in result.data'
    assert result.data['ping'] == 'Ping success!'


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
    result = schema.execute(query)

    assert hasattr(result, 'data'), 'No attribute data in result'
    assert 'clans' in result.data, 'No clan key in result.data'
    assert dict(result.data['clans'][0]) == {'tag': 'BOUHA', 'name': 'Второй  всадник  апокалипсиса'}


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

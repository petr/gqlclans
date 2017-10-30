

from schema import schema


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
    query = '{ clan { tag name }}'
    result = schema.execute(query)

    assert hasattr(result, 'data'), 'No attribute data in result'
    assert 'clan' in result.data, 'No clan key in result.data'
    print(result.data['clan'])

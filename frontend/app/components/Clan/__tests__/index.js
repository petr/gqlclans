import React from 'react'
import { Clan, mutation } from '../'

import { shallow } from 'enzyme'

const setUp = (props) => {
    const defaultProps = {
        clan: {
            clanId: '123',
            name: 'Gold LordS',
            tag: 'GLS',
            color: '#1010E6',
            members: [
                { 
                    name: 'Zibiro', 
                    accountId: '30915272', 
                    role: 'executive_officer', 
                    __typename: 'Member' 
                },
            ],
            messages: [],
            __typename: 'Clan',
        },
        mutate: jest.fn(() => Promise.resolve()),
    }

    return {
        wrapper: shallow(<Clan {...defaultProps} {...props} />),
        props: {...defaultProps, ...props},
    }
}

describe('Clan specification', () => {
    it('render query shape', () => {
        expect(mutation).toMatchSnapshot()
    })

    it('render render clan data', () => {
        const { wrapper, props } = setUp()
        const columns = wrapper.find('TableRowColumn')
        expect(columns.at(0).prop('children').join('')).toEqual(`[${props.clan.tag}]-${props.clan.name}`)
        expect(columns.at(1).prop('children')).toEqual(props.clan.members.length)
        expect(columns.at(2).prop('children').props.style.backgroundColor).toEqual(props.clan.color)
    })

    it('mutate clan message', () => {
        const { wrapper, props } = setUp()
        wrapper.setState({ message: 'Fake message' })
        const messageButton = wrapper.find('RaisedButton')
        messageButton.simulate('click')

        expect(props.mutate.mock.calls.length).toEqual(1)
        expect(props.mutate).toHaveBeenCalledWith({
            variables: {
                body: 'Fake message',
                clanId: '123',
            }
        })
    })
})
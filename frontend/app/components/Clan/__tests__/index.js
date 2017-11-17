import React from 'react'
import { Clan } from '../'

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
        mutate: jest.fn(() => Promise.resolve({ data: { addMessage: { status: 'success' } } })),
    }

    return {
        wrapper: shallow(<Clan {...defaultProps} {...props} />),
        props: {...defaultProps, ...props},
    }
}

describe('Clan specification', () => {
    it('render render clan data', () => {
        const { wrapper, props } = setUp()
        expect(wrapper.find('TableRowColumn').at(0).prop('children').join('')).toEqual(`[${props.clan.tag}]-${props.clan.name}`)
        expect(wrapper.find('TableRowColumn').at(1).prop('children')).toEqual(props.clan.members.length)
        expect(wrapper.find('TableRowColumn').at(2).prop('children').props.style).toEqual({ backgroundColor: props.clan.color, width: 30, height: 30 })
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
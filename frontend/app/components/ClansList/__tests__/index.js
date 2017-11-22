import React from 'react'
import ClansList from '../'

import { shallow } from 'enzyme'

const setUp = (props) => {
    const defaultProps = {
        ids: ['123'],
        data: {
            loading: false,
            clans: [
                {
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
            ],
        }
    }

    return shallow(<ClansList {...defaultProps} {...props} />)
}

describe('ClansList specification', () => {
    it('render CircularProgress if data is loading', () => {
        const wrapper = setUp({ data: { loading: true } })
        expect(wrapper.find('CircularProgress').length).toEqual(1)
    })

    it('render CircularProgress if clans are empty', () => {
        const wrapper = setUp({ data: { clans: null } })
        expect(wrapper.find('CircularProgress').length).toEqual(1)
    })

    it('render Table if there is clans data', () => {
        const wrapper = setUp()
        expect(wrapper.find('Table').length).toEqual(1)
    })
})
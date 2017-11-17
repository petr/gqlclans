import React from 'react'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'

import ClansList from 'components/ClansList'

export const query = gql`
    query ClansList($ids: String) {
        clans(clanId: $ids) {
            clanId
            name
            tag
            color
            members {
              name
              accountId
              role
            }
            messages {
              body
            }
        }
    }
`
const options = {
    options: (props) => ({
         variables: {
          ids: props.ids.join(','),
        }
    })
}

export default graphql(query, options)(ClansList)

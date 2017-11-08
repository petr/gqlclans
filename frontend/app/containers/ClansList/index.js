import React from 'react'
import { connect } from 'react-redux'
import { compose, graphql } from 'react-apollo'
import gql from 'graphql-tag'

import ClansList from 'components/ClansList'

const mapStateToProps = (state, ownProps) => ({})
const mapDispatchToProps = (dispatch) => ({})
const query = gql`
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

export default compose(
    graphql(query, options),
    connect(mapStateToProps, mapDispatchToProps),
)(ClansList)

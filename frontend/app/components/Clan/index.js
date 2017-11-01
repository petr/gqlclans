import React from 'react'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'

class Clan extends React.Component {
    propTypes = {
        data: React.PropTypes.shape({
            clans: React.PropTypes.array,
        }),
    }

    render() {
        if (this.props.data.clans) {
            const clan = this.props.data.clans[0]
            return (
                <div>
                    <span>[{clan.tag}]-{clan.name}</span>
                </div>
            )
        }
        return (<span>Loading</span>)
    }
}

const query = gql`
    query ClansList($id: String) {
        clans(clanId: $id) {
            name
            tag
        }
    }
`

const options = {
    options: (props) => ({
         variables: {
          id: props.id,
        }
    })
}

export default graphql(query, options)(Clan)
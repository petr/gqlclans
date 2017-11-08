import React from 'react'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'

import { TableRow, TableRowColumn, RaisedButton, TextField, Snackbar } from 'material-ui'

class Clan extends React.Component {
    static propTypes = {
        clan: React.PropTypes.object,
        mutate: React.PropTypes.func,
    }

    state = {
        open: false,
        message: '',
        status: null,
    }

    sendMessage = () => {
        const variables = {
            clanId: this.props.clan.clanId,
            body: this.state.message,
        }

        this.props.mutate({ variables }).then(({ data }) => {
            this.setState({ open: true, status: data.addMessage.success  })
        })
    }

    handleRequestClose = () => {
        this.setState({ open: false })
    }

    handleChange = (event) => {
        this.setState({ message: event.target.value })
    }

    render() {
        return (
            <TableRow>
                <TableRowColumn>[{this.props.clan.tag}]-{this.props.clan.name}</TableRowColumn>
                <TableRowColumn>{this.props.clan.members.length}</TableRowColumn>
                <TableRowColumn>
                    <div style={{backgroundColor: this.props.clan.color, width: 30, height: 30}} />
                </TableRowColumn>
                <TableRowColumn>
                    <TextField
                        hintText="Type message to a clan"
                        value={this.state.message}
                        onChange={this.handleChange}
                    />
                </TableRowColumn>
                <TableRowColumn>
                    <RaisedButton label="Send message" primary onClick={this.sendMessage} />
                    <Snackbar
                        open={this.state.open}
                        message={`Message "${this.state.message}" to clan "${this.props.clan.name}" was sent with status "${this.state.status}"`}
                        autoHideDuration={4000}
                        onRequestClose={this.handleRequestClose}
                    />
                </TableRowColumn>
            </TableRow>
        )
    }
}


const mutatuon = gql`
    mutation addMessage($body: String, $clanId: ID) {
        addMessage(body: $body, clanId: $clanId){
            message {
                body
            }
            success
        }
    }
`

export default graphql(mutatuon)(Clan)
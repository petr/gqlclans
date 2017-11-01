import React from 'react'
import { connect } from 'react-redux'
import Clan from 'components/Clan'

export const mapStateToProps = (state, ownProps) => ({})

export const mapDispatchToProps = (dispatch) => ({})

class ClansList extends React.Component {
    static propTypes = {
        ids: React.PropTypes.arrayOf(React.PropTypes.string),
    }

    render() {
        return (
            <div>
                {this.props.ids.map(id => (
                    <Clan id={id} key={id} />
                ))}
            </div>
        )
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(ClansList)

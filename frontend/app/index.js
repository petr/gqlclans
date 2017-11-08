import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import thunkMiddleware from 'redux-thunk'
import { ApolloProvider } from 'react-apollo'
import ApolloClient from 'apollo-client-preset'
import { createStore, applyMiddleware, compose } from 'redux'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

import App from 'components/App'
import rootReducer from 'reducers'

import 'stylesheets/styles.scss'

const enhancer = compose(applyMiddleware(thunkMiddleware))
const store = createStore(rootReducer, {}, enhancer)
const client = new ApolloClient()

const app = (store) => (
    <Provider store={store}>
        <ApolloProvider client={client}>
            <MuiThemeProvider>
                <App />
            </MuiThemeProvider>
        </ApolloProvider>
    </Provider>
)

ReactDOM.render(
    app(store),
    document.getElementById('app'),
)

/* global __dirname */

import path from 'path'
import CleanWebpackPlugin from 'clean-webpack-plugin'
import CopyWebpackPlugin from 'copy-webpack-plugin'
import ExtractTextPlugin from 'extract-text-webpack-plugin'
import HtmlWebpackPlugin from 'html-webpack-plugin'

const repoRoot = __dirname
const appRoot = path.join(repoRoot, 'app')
const distRoot = path.join(repoRoot, 'dist')
const publicRoot = path.join(repoRoot, 'public')

export default (env = {}) => ({
    context: repoRoot,

    entry: {
        bundle: path.join(appRoot, 'index.js'),
    },

    resolve: {
        modules: [
            appRoot,
            'node_modules',
        ],
        alias: {
            stylesheets: path.join(appRoot, 'assets', 'stylesheets'),
        },
    },

    output: {
        path: distRoot,
        filename: '[name]-[hash].js',
        libraryTarget: 'umd',
    },

    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                include: [
                    appRoot,
                    publicRoot,
                ],
                exclude: /node_modules/,
                use: 'babel-loader',
            },
            {
                test: /\.scss$/,
                include: [
                    appRoot,
                    publicRoot,
                ],
                exclude: /node_modules/,
                use: ExtractTextPlugin.extract({
                    use: [
                        'css-loader',
                        'sass-loader',
                    ],
                }),
            },

        ],
    },

    devtool: 'inline-source-map',

    devServer: {
        contentBase: [
            publicRoot,
        ],
        host: '0.0.0.0',
        port: '8010',
        noInfo: true,
        proxy: {
          '/graphql': {
            target: `http://${env.graphQLHost || '0.0.0.0'}:8567`,
            secure: false,
          }
        }
    },

    plugins: [
        new CleanWebpackPlugin([distRoot]),
        new ExtractTextPlugin('style-[hash].css'),
        new HtmlWebpackPlugin({
            template: 'public/index.html',
        }),
        new CopyWebpackPlugin([
            { from: path.join(publicRoot, 'index.html') },
        ]),
    ],
})

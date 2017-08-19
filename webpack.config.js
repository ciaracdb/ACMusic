let path = require('path');
let webpack = require('webpack');
let BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    entry: './reactapp/index',
    output: {
        path: path.resolve('./reactapp/bundles/'),
        //naming convention webpack should use for your files
        filename: '[name]-[hash].js',
    },
    plugins: [
        //tells webpack where to store data about your bundles.
        new BundleTracker({filename: './webpack-stats.json'}),
        //makes jQuery available in every module
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        })
    ],
    module: {
        loaders: [
            //a regexp that tells webpack use the following loaders on all
            //.js and .jsx files
            {test: /\.jsx?$/,
                exclude: /node_modules/,
                //use the babel loader
                loader: 'babel-loader',
                query: {
                    //specify that we will be dealing with React code
                    presets: ['react']
                }
            }
        ]
    },
    resolve: {
        //tells webpack where to look for modules
        modules: ['node_modules'],
        //extensions that should be used to resolve modules
        extensions: ['.js', '.jsx']
    }
};
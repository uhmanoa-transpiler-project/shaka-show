const path = require('path');

module.exports = {
  entry: './shaka_show/static/index.js',
  output: {
    path: path.resolve(__dirname, 'shaka_show/static/dist'),
    filename: "bundle.js"
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['env']
          }
        }
      }
    ]
  },
  stats: {
    colors: true
  },
  watch: true
};

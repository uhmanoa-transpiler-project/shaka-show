
module.exports = {
    entry: './shaka_show/static/index.js',
    output: {
        path:  __dirname + "/shaka_show/static/dist",
        filename: "bundle.js"
    },
    watch: true
};

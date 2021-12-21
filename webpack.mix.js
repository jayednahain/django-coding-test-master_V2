let mix = require('laravel-mix');
var path = require('path');

mix.js('config/templates/assets/js/app.js', 'js')
    .sass('config/templates/assets/scss/main.scss', 'css')
    .vue({version: 2})
    .setPublicPath('config/static')
    .options({
        runtimeChunkPath: 'static/rr'
    })
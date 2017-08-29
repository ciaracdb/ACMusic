const gulp = require('gulp');
const webpack_stream = require('webpack-stream');
const webpack_config = require('./webpack.config.js');

gulp.task('default', () => {
    gulp.watch(['reactapp/**/*.js', '!reactapp/bundles/*'], ['webpack']).on('change', e => {
        console.log('React file ' + e.path + ' has been changed. Compiling.');
    });
});

gulp.task('webpack', [], () => {
    return webpack_stream(webpack_config)
        .pipe(gulp.dest('reactapp/bundles'));
});
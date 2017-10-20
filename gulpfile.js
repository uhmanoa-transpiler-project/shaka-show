const gulp    = require('gulp'),
    gutil   = require('gulp-util'),
    webpack = require('webpack'),
    config  = require('./webpack.config.js');


gulp.task('test-gutil', function() {
  return gutil.log('Gulp is running!');
});

gulp.task('webpack', function() {
  return gutil.log('Todo!');
});

gulp.task('watch', function() {
  gulp.watch('shaka_show/static/**/*.js', ['webpack']);
});

gulp.task('default', ['test-gutil']);


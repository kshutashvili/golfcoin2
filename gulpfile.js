var gulp = require("gulp");
var babel = require("gulp-babel");
var sass = require("gulp-sass");
var clean = require("gulp-clean");
var imagemin = require('gulp-imagemin');
var concat = require("gulp-concat");
var minify_css = require("gulp-clean-css");
var uglify = require('gulp-uglifyjs');
var sourcemap = require("gulp-sourcemaps");
var autoprefixer = require('gulp-autoprefixer');
var server = require('browser-sync').create();



//components

var components = {
    scss: [
        "node_modules/font-awesome/css/font-awesome.min.css",
        "src/scss/libs/*",
        "src/scss/*",
        "src/scss/page-elements/*"
    ],

    js: [
        "node_modules/jquery/dist/jquery.min.js",
        "node_modules/jquery-validation/dist/jquery.validate.min.js",
        "src/js/libs/*",
        "src/js/*"
    ],

    img: [
        "src/icons/*",
        "src/img/*"
    ],

    fonts: [
        "node_modules/font-awesome/fonts/fontawesome-webfont.eot",
        "node_modules/font-awesome/fonts/fontawesome-webfont.woff",
        "node_modules/font-awesome/fonts/fontawesome-webfont.woff2",
        "src/fonts/*"
    ],
}


//tasks
//clean task

gulp.task('clean', function () {
    return gulp.src('build/*')
        .pipe(clean({ force: true }))
});

//css task
gulp.task('css', function () {
    return gulp.src(components.scss)
        .pipe(autoprefixer({
            browsers: ['last 16 versions'],
            cascade: false
        }))
        .pipe(sass().on('error', sass.logError))
        .pipe(concat("style.css"))
        .pipe(minify_css())
        .pipe(gulp.dest('build/css'));

});
//css ie task
gulp.task('ie', function () {
    return gulp.src("src/scss/ie/*")
        .pipe(autoprefixer({
            browsers: ['last 16 versions'],
            cascade: false
        }))
        .pipe(sass().on('error', sass.logError))
        .pipe(minify_css("ie.css"))
        .pipe(gulp.dest('build/css'));

});

//js task
gulp.task("js", function () {
    gulp.src(components.js)
        .pipe(babel({ presets: ['es2015'] }))
        .pipe(concat('app.js'))
        .pipe(uglify())
        .pipe(sourcemap.init({ loadMaps: true }))
        .pipe(sourcemap.write('./maps'))
        .pipe(gulp.dest('build/js/'));
});

//fonts task

gulp.task('fonts', function () {
    return gulp.src(components.fonts)
        .pipe(gulp.dest('build/fonts'));

});

//image task

gulp.task('img', function () {
    return gulp.src(components.img)
        .pipe(imagemin())
        .pipe(gulp.dest('build/img'));

});

//pages task
gulp.task('pages', function () {
    gulp.src('src/pages/*')
        .pipe(gulp.dest("build/pages/"));
});

//html task

gulp.task('html', function () {
    gulp.src('src/index.html')
        .pipe(gulp.dest("build/"));
});

//server
gulp.task('server', function () {
    server.init({
        server: {
            baseDir: "build",
        }
    });
    server.watch(['build/**/*.*']).on('change', server.reload);
});

//watch task for css and js files

gulp.task('watch', function () {
    gulp.watch(components.scss, ['css']);
    gulp.watch("src/scss/ie/*", ['ie']);
    gulp.watch(components.img, ['img']);
    gulp.watch(components.fonts, ['fonts']);
    gulp.watch("src/index.html", ['html']);
    gulp.watch("src/pages/*", ['pages']);
    gulp.watch(components.js, ['js']);

})
gulp.task('serv', ['watch', 'server']);

//default task
gulp.task("default", ['clean', 'html', 'pages', 'css', "ie", 'js', 'img', 'fonts']);


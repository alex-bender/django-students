// Place third party dependencies in the lib folder
//
// Configure loading modules from the lib directory,
// except 'app' ones,
console.log('app js loaded');

require.config({
    deps: ['app/main'],

    "baseUrl": "static/media/lib",
    "paths": {
        "backbone": "../lib/backbone-min",
//        "last": "../app/last",
        "app": "../app",
        "underscore": "underscore",
        "hest": "../app/hest"
    },
    "shim": {

        'backbone': {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },
        'underscore': {
            exports: '_'
        },
        'jquery': {
            exports: '$'
        }

    }
});

require(["app/main", "app/last"], function(main, last){
    console.log(main, last);
});

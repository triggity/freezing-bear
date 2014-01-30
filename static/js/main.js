
require.config({
  paths: {
    'underscore': 'vendor/underscore',
    'jquery': 'vendor/jquery-2.0.3.min',
//  
  },
  shim: {
    "underscore": {
      "exports": "_"
    },
  }
});
require([
  "underscore",
  "jquery"
  ], function(_, $) {
  console.log('run require'); 
  });

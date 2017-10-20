import { codeMirror } from './codemirror';

define([
    'jquery'
], function($) {

  // Get the source code once the page has loaded
  $.ajax({
    url: '/ajax/codetracker/sourcecode',
    type: 'GET',
    success: function(jsonResponse) {
      console.log('SUCCESS');
      console.log(jsonResponse);
    },
    error: function() {
      console.log('codetracker: JSON ERROR');
    }
  });
});
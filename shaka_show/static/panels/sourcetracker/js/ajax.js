import { codeMirror } from './codemirror';

define([
  'jquery'
], function($) {

  // Get the source code once the page has loaded
  $.ajax({
    url: '/ajax/codetracker/sourcecode',
    type: 'GET',
    success: function(sourcecode) {
      console.log('SUCCESS');
      console.log(sourcecode);
      codeMirror.setValue(sourcecode);
    },
    error: function() {
      console.log('codetracker: JSON ERROR');
    }
  });
});
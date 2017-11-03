import { codeMirror } from './codemirror';

define([
  'jquery'
], function($) {

  console.log('entered sourcetracker/ajax.js');

  // Get the source code once the page has loaded
  $.ajax({
    url: '/ajax/codetracker/sourcecode',
    type: 'GET',
    success(sourcecode) {
      console.log('codetracker: sourcecode GET success');
      codeMirror.setValue(sourcecode);
    },
    error() {
      console.log('codetracker: GET ERROR');
    }
  });
});
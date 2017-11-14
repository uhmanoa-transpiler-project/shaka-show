import { codeMirror } from './codemirror';

define([
  'jquery',
  'underscore'
], function($, _) {

  console.log('entered sourcetracker/ajax.js');

  const source_files = {}

  // Get the source code once the page has loaded
  $.ajax({
    url: '/ajax/codetracker/sourcecode',
    type: 'GET',
    success(sources) {
      console.log('codetracker: sourcecode GET success');

      _.each(JSON.parse(sources), (code, name) => {
        source_files[name] = code;
      });

      const default_filename = Object.keys(source_files)[0];
      const default_source   = source_files[default_filename];

      const template = document.querySelector('#codetracker-file-tab-template');
      const text_div = template.content.querySelectorAll('div');
      text_div[0].textContent = default_filename;

      const menu = document.querySelector('#codetracker-file-menu');
      const clone = document.importNode(template.content, true);
      menu.appendChild(clone);

      codeMirror.setValue(default_source);
    },
    error() {
      console.log('codetracker: GET ERROR');
    }
  });
});
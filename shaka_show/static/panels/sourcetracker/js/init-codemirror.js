require.config({
  packages: [{
    name: 'codemirror',
    location: '../../../'
  }]
});

define([
    'codemirror',
], function(CodeMirror) {

  require('codemirror/mode/scheme/scheme');
  const codeMirror = CodeMirror.fromTextArea(document.getElementById('codetracker-container'), {
    lineNumbers: true,
    mode: 'scheme'
  });

  console.log(codeMirror);
});
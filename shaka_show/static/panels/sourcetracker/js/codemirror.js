console.log('entered sourcetracker/codemirror.js: ');

const codeMirror = CodeMirror(document.getElementById('shaka-codemirror'), {
  mode: 'scheme',
  lineNumbers: true
});

export { codeMirror };

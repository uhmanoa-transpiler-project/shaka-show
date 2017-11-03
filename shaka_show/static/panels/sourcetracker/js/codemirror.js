const codeMirror = CodeMirror(document.getElementById('shaka-codemirror'), {
  mode: 'scheme',
  lineNumbers: true
});

export { codeMirror };

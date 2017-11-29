console.log('entered sourcetracker/codemirror.js: ');

const codeMirror = CodeMirror(document.getElementById('shaka-codemirror'), {
  mode: 'scheme',
  lineNumbers: true,
  theme: 'dracula',
  viewportMargin: Infinity
});

export { codeMirror };

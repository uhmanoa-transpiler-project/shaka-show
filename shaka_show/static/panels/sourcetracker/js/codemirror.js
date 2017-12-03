console.log('entered sourcetracker/codemirror.js: ');

const codeMirror = CodeMirror(document.getElementById('shaka-codemirror'), {
  mode: 'scheme',
  lineNumbers: true,
  theme: 'dracula',
  //theme: 'paraiso-light',
  viewportMargin: Infinity
});

export { codeMirror };

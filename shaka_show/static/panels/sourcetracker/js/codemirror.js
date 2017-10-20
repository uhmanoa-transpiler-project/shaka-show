const codeMirror = CodeMirror(document.getElementById('shaka-codemirror'), {
  mode: 'scheme',
  lineNumbers: true,
  value: '; Scheme test\n; Testing 123\n(define x 1)\n',
});

export { codeMirror };

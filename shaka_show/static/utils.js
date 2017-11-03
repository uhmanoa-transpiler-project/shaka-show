/**
 * Helper functions used through out client code.
 */
console.log('entered utils.js');

// Used to get _xsrf cookie value from within client.
// The value of this cookie must be sent with any POSTS
// to the shaka-show server to ensure there is no
// cross-site requests.
const getXSRFCookie = function() {
  const xsrf = document.cookie.match(/\b_xsrf=([^;]*)\b/);
  return xsrf ? xsrf[1] : undefined;
};

export { getXSRFCookie };

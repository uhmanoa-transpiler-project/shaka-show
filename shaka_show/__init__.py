"""Shaka-Show web based debugger"""

import os

# Used for website renderers. Static files include:
#   Images, js, less, css, sass
DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), 'static')

# Used for specifying base 'templates' folder path. Used for website renderers.
# Template files include:
#   HTML, HTML with template variables
DEFAULT_TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates')

del os

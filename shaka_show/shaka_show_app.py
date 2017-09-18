"""
A Tornado-made web based debugger for the Shaka-Scheme interpreter.

ShakaShowWebApp:
    - Primary class for the Python server.
    - Is the webserver that listens for incoming requests
    - Handles serving website
"""

from __future__ import absolute_import

# System imports
import webbrowser
import importlib

# Tornado imports
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# Shaka-Show imports
from showutil import load_handlers, parse_args

from __init__ import (
    DEFAULT_STATIC_FILES_PATH,
    DEFAULT_TEMPLATE_FILES_PATH
)



#----------------------------------------------------------------
# Main web server class
#----------------------------------------------------------------

class ShakaShowWebApp(tornado.web.Application):
    def __init__(self):
        """
        Here we populate the settings dict and handler list
        that are used during instantiation of this class.
        """
        settings = self.init_settings()
        handlers = self.init_handlers(settings)
        super(ShakaShowWebApp, self).__init__(handlers, **settings)


    def init_settings(self):
        settings = dict(
            template_path = DEFAULT_TEMPLATE_FILES_PATH,
            static_path = DEFAULT_STATIC_FILES_PATH,
            autoreload = True,
            serve_traceback = True,
            compress_response = True,
            websocket_ping_interval = 10,
            websocket_ping_timeout = 60,
            xsrf_cookies = True
        )
        return settings


    def init_handlers(self, settings):
        """Return a list of tuples representing URL / Handler pairs.
        Each handler is loaded using the "load_handler(name)" function.
        The name passed in is the path to the handers.py module for each
        handler.
        The handler order matters, so put important handlers first
        and error or less important handlers last. It uses first handler
        in the list that matches the corresponding url.
        """
        handlers = []
        handlers.extend(load_handlers('base.handlers'))
        return handlers



#----------------------------------------------------------------
# Entry points for app
#----------------------------------------------------------------
def main():
    print("shaka_show_app.py", "Hello World!")
    httpServer = tornado.httpserver.HTTPServer(ShakaShowWebApp())
    httpServer.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    print("shaka_show_app.py", "launching main")
    main()

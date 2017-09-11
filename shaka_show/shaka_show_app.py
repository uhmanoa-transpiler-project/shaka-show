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

# Tornado imports
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from __init__ import (
    DEFAULT_STATIC_FILES_PATH,
    DEFAULT_TEMPLATE_FILES_PATH
)


#----------------------------------------------------------------
# Helper functions
#----------------------------------------------------------------

#----------------------------------------------------------------
# Main web server class
#----------------------------------------------------------------

class ShakaShowWebApp(tornado.web.Application):
    def __init__(self):
        settings = self.init_settings()
        handlers = self.init_handlers(settings)
        super(ShakaShowWebApp, self).__init__(handlers, **settings)


    def init_settings(self):
        settings = dict(
            template_path = DEFAULT_TEMPLATE_FILES_PATH,
            static_path = DEFAULT_STATIC_FILES_PATH
        )
        return settings


    def init_handlers(self, settings):
        handlers = []
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

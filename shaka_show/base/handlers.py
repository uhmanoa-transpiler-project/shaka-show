"""
Default handlers for web application such as 404.
"""

from tornado import web


class MainHandler(web.RequestHandler):
    """
    MainHandler is the handler that sets up the arguments
    to render within each html template.
    """
    def get(self):

        # Check for xsrf cookie
        if not self.get_cookie('_xsrf'):
            self.set_cookie('_xsrf', self.xsrf_token)

        # The panels to include
        panels = ['codetracker.html', 'console.html']
        panelargs = {}

        # controls settings
        controls_args = {}
        # codetracker settings
        codetracker_args = {}
        # console settings
        console_args = {}


        panelargs['codetracker.html'] = codetracker_args
        panelargs['console.html'] = console_args

        self.render('page.html', panels=panels, panelargs=panelargs)


class Error404Handler(web.RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.render('404.html')


default_handlers = [
    (r'/', MainHandler)
]

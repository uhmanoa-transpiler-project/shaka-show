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

        # The panels to include
        panels = ['codetracker.html']

        panelargs = {}

        # codetracker settings
        codetracker_args = dict(
            filename=self.settings['cmdargs']['filename'],
            sourcecode=self.settings['cmdargs']['source']
        )
        panelargs['codetracker.html'] = codetracker_args

        self.render('page.html', panels=panels, panelargs=panelargs)


class Error404Handler(web.RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.render('404.html')


default_handlers = [
    (r'/', MainHandler),
    (r'(.*)', Error404Handler)
]

"""
Default handlers for web application such as 404.
"""

from tornado import web


class Error404Handler(web.RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.render('404.html')


default_handlers = [
    (r'(.*)', Error404Handler)
]

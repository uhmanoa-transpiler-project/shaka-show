"""
Handlers for all ajax communication with sourcetracker panel.
"""

from tornado import web


class SourcecodeHandler(web.RequestHandler):
    """
    SourcecodeHandler serves the source code to the sourcetracker
    when it sends a get request to /ajax/sourcetracker/sourcecode.
    """
    def get(self):
        self.write(self.settings['cmdargs']['source'])


default_handlers = [
    (r'/ajax/codetracker/sourcecode', SourcecodeHandler)
]

"""
Handlers for all ajax communication with sourcetracker panel.
"""

from tornado import web
import json


class SourcecodeHandler(web.RequestHandler):
    """
    SourcecodeHandler serves the source code to the sourcetracker
    when it sends a get request to /ajax/sourcetracker/sourcecode.
    """
    def get(self):
        source_files = self.settings['cmdargs']['source_files']
        self.write(json.dumps(source_files, separators=(',', ':')))


default_handlers = [
    (r'/ajax/codetracker/sourcecode', SourcecodeHandler)
]

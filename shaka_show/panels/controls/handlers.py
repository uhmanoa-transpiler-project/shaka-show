"""
Handlers for buttons and all menu items in the Controls panel.
"""

from tornado import web


class ButtonsHandler(web.RequestHandler):
    """
    ButtonsHandler simply receives a 'notification' when
    one of the runtime control buttons is pressed.
    It then sends the corresponding request to the
    shaka-scheme interpreter.
    """
    def post(self):
        button_posts = [
            'start',
            'pause',
            'stop',
            'step'
        ]
        api_call = self.request.uri.split('/')[-1]
        print(api_call)
        if api_call in button_posts:
            self.write('button API post success')
        else:
            self.write('button API post failure')


default_handlers = [
    (r'/ajax/controls/buttons/\w+', ButtonsHandler)
]

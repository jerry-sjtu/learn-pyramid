import logging
log = logging.getLogger(__name__)


from pyramid.view import (
    view_config,
    view_defaults
    )

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
	log.debug('in home view')
        return {'name': 'Home View'}

    @view_config(route_name='hello')
    def hello(self):
	log.debug('in hello view')
        return {'name': 'Hello View'}

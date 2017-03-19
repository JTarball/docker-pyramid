from pyramid.view import view_config
from pyramid.response import Response
#http://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/request_response.html
# for params 
# http://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/routing.html
import logging
log = logging.getLogger(__name__)

from libutils.log_formatters import ColoredFormatter, LevelFormatter


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    log.error("fdlkjsfkjhsj")
    log.debug("kjdslkdjhfdsjkhfkhsjkhfkjsdhjkfhjksdh")
    log.warn("dskjfhjsdghjfb")
    return {'project': 'Docker Pyramid'}


@view_config(route_name='home2', renderer='templates/mytemplate.jinja2')
def my_view2(request):
    return Response('<body><h1>Hello World!</h1></body>')


# from pyramid.view import (
#     view_config,
#     view_defaults
#     )

# @view_defaults(renderer='home.pt')
# class TutorialViews:
#     def __init__(self, request):
#         self.request = request

#     @view_config(route_name='home')
#     def home(self):
#         return {'name': 'Home View'}

#     @view_config(route_name='hello')
#     def hello(self):
#         return {'name': 'Hello View'}

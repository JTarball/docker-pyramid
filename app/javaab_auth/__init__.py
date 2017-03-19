"""
    javaab_auth.__init__
    =======================

    Main routine.

    Add config here
"""
import colander

from pyramid.config import Configurator

from cornice import Service
from cornice.service import get_services
from cornice.validators import colander_body_validator
from cornice_swagger import CorniceSwagger

from sqlalchemy import engine_from_config

#from .models import DBSession, Base

_VALUES = {}


# Create a simple service that will store and retrieve values
values = Service(name='foo',
                 path='/values/{key}',
                 description="Cornice Demo")


# Create a body schema for our requests
class BodySchema(colander.MappingSchema):
    value = colander.SchemaNode(colander.String(),
                                description='My precious value')


# Create a response schema for our 200 responses
class OkResponseSchema(colander.MappingSchema):
    body = BodySchema()


# Aggregate the response schemas for get requests
response_schemas = {
    '200': OkResponseSchema(description='Return value')
}


# Create our cornice service views
class MyValueApi(object):
    """My precious API.

    """

    @values.get(tags=['values'], response_schemas=response_schemas)
    def get_value(request):
        """ Returns the value.

            ```ruby
            # This is some Ruby code!
            ```

            ```python
            # This is some Python code!
            ```

            > The above command returns JSON structured like this:

            ```json
            [
              {
                "id": 1,
                "name": "Fluffums",
                "breed": "calico",
                "fluffiness": 6,
                "cuteness": 7
              },
              {
                "id": 2,
                "name": "Max",
                "breed": "unknown",
                "fluffiness": 5,
                "cuteness": 10
              }
            ]

        """
        key = request.matchdict['key']
        return _VALUES.get(key)

    @values.put(tags=['values'], validators=(colander_body_validator, ),
                schema=BodySchema(), response_schemas=response_schemas)
    def set_value(request):
        """Set the value and returns *True* or *False*."""

        key = request.matchdict['key']
        _VALUES[key] = request.json_body
        return _VALUES.get(key)


# Create a service to serve our OpenAPI spec
swagger = Service(name='OpenAPI',
                  path='/__api__',
                  description="OpenAPI documentation")


@swagger.get()
def openAPI_spec(request):
    doc = CorniceSwagger(get_services())
    doc.summary_docstrings = True
    my_spec = doc.generate('MyAPI', '1.0.0')
    return my_spec


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    #engine = engine_from_config(settings, 'sqlalchemy.')
    #DBSession.configure(bind=engine)
    #Base.metadata.bind = engine

    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include("cornice")
    config.include('cornice_swagger')
    config.include('.models')
    config.include('.security')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('home2', '/dan')
    config.scan()
    return config.make_wsgi_app()

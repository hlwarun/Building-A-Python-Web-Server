from pyramid.config import Configurator
from pyramid.response import Response

# Defining the function that reflects the view response
def indexView(request):
    return Response(
        'Hello from the Pyramid app!\n',
        content_type='text/plain',
    )

# Creating a Configurator object
config = Configurator()

# Defining a route for the indexView
config.add_route('index', '/')

# Connecting indexView to the above route
config.add_view(indexView, route_name='index')

# Creating pyramid app
app = config.make_wsgi_app()

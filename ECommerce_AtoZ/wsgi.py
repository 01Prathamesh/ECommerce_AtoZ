# import os
# from django.core.wsgi import get_wsgi_application
# from django.core.handlers.wsgi import WSGIRequest
# from django.http import HttpResponse

# # Set the default settings module for the 'DJANGO_SETTINGS_MODULE' environment variable.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ECommerce_AtoZ.settings')

# # Get the WSGI application callable.
# application = get_wsgi_application()

# # Vercel expects either 'app' or 'handler'.
# # Assign the WSGI application callable to 'handler'.
# def handler(request):
#     # Convert the Vercel request into a Django WSGIRequest
#     environ = {
#         'REQUEST_METHOD': request.method,
#         'PATH_INFO': request.path,
#         'QUERY_STRING': request.query_string,
#         'CONTENT_TYPE': request.headers.get('Content-Type', ''),
#         'CONTENT_LENGTH': str(request.headers.get('Content-Length', 0)),
#         'wsgi.input': request.body,
#         'SERVER_NAME': 'localhost',
#         'SERVER_PORT': '8000',
#     }

#     # Create a Django request object
#     django_request = WSGIRequest(environ)

#     # Call the WSGI application (Django)
#     response = application(django_request)

#     # Return a simple HttpResponse
#     return HttpResponse(response.content, status=response.status_code, content_type=response.get('Content-Type'))

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'DJANGO_SETTINGS_MODULE' environment variable.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ECommerce_AtoZ.settings')

# Get the WSGI application callable.
application = get_wsgi_application()

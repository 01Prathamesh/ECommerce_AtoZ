import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'DJANGO_SETTINGS_MODULE' environment variable.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ECommerce_AtoZ.settings')

# Get the WSGI application callable.
application = get_wsgi_application()

# Vercel expects either 'app' or 'handler'. 
# We will assign the WSGI application callable to 'app'.
app = application

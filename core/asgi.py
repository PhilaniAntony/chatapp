
import os
from django.core.asgi import get_asgi_application
import django
from channels.routing import get_default_application
#from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
application = get_asgi_application()

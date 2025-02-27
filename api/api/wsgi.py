"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
sys.path.append('/home/sfuehr/Documents/TUB-WI/S7_BA_SimRa/simra-visualizations-server/api')
sys.path.append('/home/sfuehr/Documents/TUB-WI/S7_BA_SimRa/simra-visualizations-server/api/api')

application = get_wsgi_application()

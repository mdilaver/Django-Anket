import os, sys

sys.path.append('/var/www')
sys.path.append('/var/www/Mysite')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mysite.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
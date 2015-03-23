import os,sys
sys.path.append('/var/www')
sys.path.append('/var/www/anket')
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anket.settings")
 
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
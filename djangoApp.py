import sys
sys.path.insert(0, './helloDjango')
from helloDjango import wsgi

# Creating django app
app = wsgi.application

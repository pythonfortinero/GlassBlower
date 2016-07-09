from flask.ext.via.routers import default
from app.views import *

urls = [
	# url, clase y nombre de la vista
    default.Pluggable('/', Index, 'index'),
    default.Pluggable('/about', About, 'about')
]
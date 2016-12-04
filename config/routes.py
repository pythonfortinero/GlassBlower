from flask.ext.via.routers.default import Pluggable as p
from app.views import *

urls = [
    # url, clase y nombre de la vista
    p('/', Index, 'index'),
    p('/about', About, 'about')
]
#

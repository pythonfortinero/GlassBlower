from flask.ext.via.routers.default import Pluggable as p
from app.views import *

urls = list()
    
'''
In de route.blz file add the parameters url,method_view_class,view_name
for the routes.py
'''
with open('config/routes.blz','r') as file:
    for row in file:
        p_row = row.replace('\n','').replace(' ','').split(',')
        exec("urls.append(p('%s', %s, '%s'))" % (p_row[0], p_row[1], p_row[2]))

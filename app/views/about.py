from flask.views import MethodView
from flask import render_template

class About(MethodView):

    def get(self):
        return render_template('about.html')

    def post(self):
    	pass

    def put(self):
    	pass

    def delete():
    	pass

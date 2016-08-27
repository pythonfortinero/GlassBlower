from flask.views import MethodView
from flask import render_template
from flask.ext.login import login_required

class Index(MethodView):

    @login_required
    def get(self):
        return render_template('index.html')

    def post(self):
        pass

    def put(self):
        pass

    def delete():
        pass
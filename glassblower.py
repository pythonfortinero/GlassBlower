import os 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("blow")
parser.add_argument("option")
parser.add_argument("--newFile")
args = parser.parse_args()

currentPath = os.getcwd()
if args.blow == "blow" and args.option == 'view':
    fileDir = os.path.join(currentPath, 'app', 'views', args.newFile.lower() + '.py')
    with open(fileDir,'w') as af:
        af.write('from flask.views import MethodView \n')
        af.write('from flask import render_template \n')
        af.write('\n')
        af.write('class %s(MethodView): \n' % args.newFile.capitalize())
        af.write('\n')
        af.write('    def get(self): \n')
        af.write('        return render_template("%s.html") \n' % args.newFile.lower())
        af.write('\n')
        af.write('    def post(self): \n')
        af.write('        pass \n')
        af.write('\n')
        af.write('    def put(self): \n')
        af.write('        pass \n')
        af.write('\n')
        af.write('    def delete(): \n')
        af.write('        pass \n')
    initDir = os.path.join(currentPath, 'app', 'views', '__init__.py')
    with open(initDir,'a') as af:
        af.write('\nfrom %s import * \n' % args.newFile.lower())
    htmlDir = os.path.join(currentPath, 'app', 'templates', args.newFile.lower() + '.html')
    with open(htmlDir,'w') as af:
        af.write('{% extends "base.html" %} \n')
        af.write('\n')
        af.write('{% block content %} \n')
        af.write('<h1 class="text-center">%s</h1> \n' % args.newFile.upper())
        af.write('\n')
        af.write('{% endblock %} \n')
    print "Updated Directories"
    print fileDir
    print initDir
    print htmlDir
elif args.blow == "blow" and args.option == 'model':
    fileDir = os.path.join(currentPath, 'app', 'models', args.newFile.lower() + '.py')
    with open(fileDir,'w') as af:
        af.write('from manage import app, db \n')
        af.write('from sqlalchemy import ForeignKey \n')
        af.write('from sqlalchemy.orm import relationship \n')
        af.write('\n')
        af.write('class %s(db.Model): \n' % args.newFile.capitalize())
        af.write('\n')
        af.write('    __tablename__ = "%s" \n' % args.newFile.lower() )
        af.write('    id = db.Column(db.Integer, primary_key=True)')
    initDir = os.path.join(currentPath, 'app', 'models', '__init__.py')
    with open(initDir,'a') as af:
        af.write('\nfrom %s import * \n' % args.newFile.lower())
    print "Updated Directories"
    print fileDir
    print initDir
elif args.blow == "blow" and args.option == 'login':
    fileDir = os.path.join(currentPath, 'app', '__init__.py')
    with open(fileDir,'a') as af:
        af.write('\n')
        af.write('from flask.ext.login import LoginManager\n')
        af.write('login_manager = LoginManager()\n')
        af.write('login_manager.init_app(app)\n')
        af.write('\n')
        af.write('login_manager.login_view = "login"\n')
        af.write('\n')
        af.write('@login_manager.user_loader\n')
        af.write('def load_user(id):\n')
        af.write('    return User.query.get(int(id))\n')

    routesDir = os.path.join(currentPath, 'config', 'routes.py')
    with open(routesDir,'a') as af:
        af.write("\nuser_url = [default.Pluggable('/register',UserRegister,'register'),")
        af.write("\n    default.Pluggable('/login',UserLogin,'login'),")
        af.write("\n    default.Pluggable('/logout', UserLogout,'logout')]")
        af.write("\nurls = urls + user_url")
    import shutil
    shutil.copy2(os.path.join(currentPath, 'utilities', 'user', 'models','user.py'),
                 os.path.join(currentPath, 'app','models','user.py'))
    shutil.copy2(os.path.join(currentPath, 'utilities', 'user', 'templates','login.html'),
                 os.path.join(currentPath, 'app', 'templates','login.html'))
    shutil.copy2(os.path.join(currentPath, 'utilities', 'user', 'templates','register.html'),
                 os.path.join(currentPath, 'app', 'templates','register.html'))
    shutil.copy2(os.path.join(currentPath, 'utilities', 'user', 'views','user.py'),
                 os.path.join(currentPath, 'app','views','user.py'))

    modelDir = os.path.join(currentPath, 'app', 'models', '__init__.py')
    with open(modelDir,'a') as af:
        af.write('\nfrom user import * \n')
    
    viewDir = os.path.join(currentPath, 'app', 'views', '__init__.py')
    with open(viewDir,'a') as af:
        af.write('\nfrom user import * \n')
    print "Updated Directories"
    print fileDir
    print routesDir
    print modelDir
    print viewDir
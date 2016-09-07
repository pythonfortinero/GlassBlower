from flask.views import MethodView 
from flask import render_template, request, url_for, redirect, flash
from flask.ext.login import login_user, logout_user, current_user, login_required
from manage import db
from app.models import User, pwd_context

class UserRegister(MethodView): 

    def get(self): 
        return render_template("register.html") 

    def post(self): 
        user = User(request.form['username'] , request.form['password'],request.form['email'])
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered')
        return render_template("login.html")

    def put(self): 
        pass 

    def delete(): 
        pass 

class UserLogin(MethodView): 

    def get(self): 
        return render_template("login.html")

    def post(self): 
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and pwd_context.verify(password, user.password):
            login_user(user)
            flash('Logged in successfully')
            return redirect(url_for('index'))
        flash('Username or Password is invalid' , 'error')
        return render_template('login.html')

    def put(self): 
        pass 

    def delete(): 
        pass 

class UserLogout(MethodView): 

    @login_required
    def get(self): 
        logout_user()
        return redirect(url_for('index')) 

    def post(self): 
        pass 

    def put(self): 
        pass 

    def delete(): 
        pass 
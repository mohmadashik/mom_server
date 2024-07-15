import os
from datetime import datetime
import time 
from flask import Blueprint, jsonify,render_template,url_for,flash,redirect,request
from flask_login import login_user,current_user,logout_user, login_required
from .. import bcrypt


from ..db_manager import DBManager
from ..models.user import User

user_bp = Blueprint('user_controller',__name__,url_prefix='/user')

db = DBManager.get_db()

@user_bp.route('/home')
@login_required
def home():
    return jsonify({'status':'Welcome to User Home Page'}), 200


@user_bp.route("/register", methods=['GET', 'POST'])
def register():
    try:
        from .. import bcrypt 
        print('entry into register')
        if current_user.is_authenticated:
            return jsonify({'message':'Already Logged in'}), 200
        if request.method == 'POST':
            print('POST method')
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            created_at = str(datetime.now())
            print(f'created_at : {created_at}')
            user = User(username=username, password=hashed_password,created_at=created_at)
            db.session.add(user)
            db.session.commit()
            return jsonify({'message':'User registered successfully'}), 200
    except Exception as err:
        print(f'error while user registration : {err}')
        return jsonify({'message':f'error : {err}'}) , 500
    

@user_bp.route("/login", methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify({'message':'Already logged in'}), 200
    else:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return jsonify({'message':'Login successful'}),200
        else:
            return jsonify({'message':'Login unsuccessful. Check username and password'}), 401

@user_bp.route("/update/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    try:
        from .. import bcrypt
        if not current_user.is_authenticated:
            return jsonify({'message': 'Please log in to update your profile'}), 401

        user = User.query.get(user_id)
        if user is None:
            return jsonify({'message': 'User not found'}), 404

        if request.method == 'PUT':
            data = request.get_json()
            new_username = data.get('new_username')
            new_password = data.get('new_password')

            # Update user information
            user.username = new_username
            user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            db.session.commit()

            return jsonify({'message': 'User information updated successfully'}), 200

    except Exception as err:
        return jsonify({'message': f'Error while updating user profile: {err}'}), 500


@user_bp.route("/logout")
def logout():
    logout_user()
    return jsonify({'message':'Logged out successfully'}), 200


@user_bp.route("/")
def ping():
    return {"status":"User Controller is UP"}, 200
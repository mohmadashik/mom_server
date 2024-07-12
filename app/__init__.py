''' main flask file'''

import traceback 

from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate 
from flask_cors import CORS 

from .config.sql_config import Config

from .db_manager import DBManager

bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    try:
        # global login_manager,bcrypt

        app = Flask(__name__)
        CORS(app,supports_credentials=True)

        app.config.from_object(Config)

        db_manager = DBManager()
        db = db_manager.get_db()
        db.init_app(app)
        migrate.init_app(app,db)
        bcrypt.init_app(app)

        login_manager = LoginManager(app)
        login_manager.login_view = 'user_controller.login'

        from .controllers.user import user_bp
        app.register_blueprint(user_bp)

        @app.route('/')
        def ping():
            return 'Goaler App is UP and Running'
        
        @login_manager.user_loader 
        def load_user(user_id):
            from .models.user import User
            return User.query.get(int(user_id))
        
        return app
    except Exception as err:
        print(f'Error while creating the app : {err}')
        traceback.print_exc()







from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.root_path}/market.db'
app.config['SECRET_KEY'] = 'ca84b9da7a1d3bb0d66cbf82'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login_page'
login_manager.login_message_category = 'info'
app.app_context().push()


from market import routes


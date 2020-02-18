from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

csrf=CSRFProtect()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'labthree'
csrf.init_app(app)
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '2525' 
 
mail = Mail(app)
from app import views


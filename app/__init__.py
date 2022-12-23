from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# tem que ser importado depois que as variavel existirem 
from app.controllers import default

# ======================== OLD ========================
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# # tem que ser importado depois que as variavel existirem 
# from app.controllers import default
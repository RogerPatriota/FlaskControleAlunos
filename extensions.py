from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instanciando os objetos
db = SQLAlchemy()
migrate = Migrate()
from app import app
from app.blueprints.web_logic import web_logic

app.register_blueprint(web_logic)
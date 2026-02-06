import sys
sys.path.append('./src')

from app import app
from utils.db import db

with app.app_context():
    db.create_all()
    pass

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
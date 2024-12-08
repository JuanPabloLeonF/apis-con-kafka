import os

from flask import Flask
from dotenv import load_dotenv

from configuration import init_dabase, db

load_dotenv()

app = Flask(__name__)
init_dabase(app=app)

if __name__ == '__main__':
    from controllers import productRouter
    app.register_blueprint(productRouter)
    app.run(debug=os.getenv('DEBUG'), host=os.getenv('HOST'), port=os.getenv('PORT'))
    with app.app_context():
        db.create_all()
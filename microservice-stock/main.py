import os
import threading

from flask import Flask
from dotenv import load_dotenv

from configuration import init_dabase, db
from configuration_kafka import runConsumer

load_dotenv()

app = Flask(__name__)

consumer_started: bool = False

def startConsumer():
    global consumer_started
    if not consumer_started:
        consumerThread = threading.Thread(target=runConsumer, daemon=True)
        consumerThread.start()
        consumer_started = True

init_dabase(app=app)

if __name__ == '__main__':
    from controllers import stockRouter
    app.register_blueprint(stockRouter)

    startConsumer()

    with app.app_context():
        db.create_all()

    app.run(debug=False, host=os.getenv('HOST'), port=os.getenv('PORT'))
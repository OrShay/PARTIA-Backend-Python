from app.rides import rides_blueprint
from app.event import event_blueprint
from app.equipment import equipment_blueprint
from app.participant import participant_blueprint
from flask import Flask, request


app = Flask(__name__)


app.register_blueprint(rides_blueprint)
app.register_blueprint(event_blueprint)
app.register_blueprint(equipment_blueprint)
app.register_blueprint(participant_blueprint)


if __name__ == '__main__':
    app.run()


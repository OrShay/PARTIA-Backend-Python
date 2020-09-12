from pathlib import Path
import logging
import os
from partia_app.rides import rides_blueprint
from partia_app.event import event_blueprint
from partia_app.equipment import equipment_blueprint
from partia_app.participant import participant_blueprint
from partia_app.login import login_blueprint
from partia_app.cashier import cashier_blueprint
from flask import Flask, request
from partia_app.responses import response_200

app = Flask(__name__)

app.register_blueprint(rides_blueprint)
app.register_blueprint(event_blueprint)
app.register_blueprint(equipment_blueprint)
app.register_blueprint(participant_blueprint)
app.register_blueprint(cashier_blueprint)
app.register_blueprint(login_blueprint)

dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(str(Path(dir_path).parent.parent), "server.log")
logging.basicConfig(filename=path, level=logging.DEBUG)


@app.before_request
def log_request_info():
    app.logger.debug(f'Got request url: {request.base_url}')
    app.logger.debug(f'Request Body: {request.json} ')
    app.logger.debug(f'Request Values: {list(request.values.items())} ')


@app.route('/', methods=['GET'])
def is_alive():
    app.logger.info("Server is UP!")
    return response_200({"message": "The server is up Queen! :)"})


if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify, render_template

from lsst.db.utils import ButlerDataController

app = Flask(__name__)


@app.route('/')
def home():
   return render_template('simple_test.html')

# @app.route('/', methods=['POST'])
# def get_logs():
#     args = request.args
#     observation_day = args.get('obs_day')
#     sequence_number = args.get('seq_num')
#     butler_data_controller = ButlerDataController()
#     timestamp = butler_data_controller.get_time_spam_from_observation_id(observation_day, sequence_number)
#
#     return jsonify({})
#
# @app.route('/logs', methods=['GET'])
# def get_logs():
#     args = request.args
#     observation_day = args.get('obs_day')
#     sequence_number = args.get('seq_num')
#     return jsonify({})

app.run(port=5000)
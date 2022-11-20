from flask import Flask, jsonify, request
import schedule_builder

api = Flask(__name__)

@api.route('/generate', methods=['GET'])
def generate_schedule():
    # policies = request.get_json() 
    res = schedule_builder.get_schedule()
    print(res)
    return jsonify(res)

if __name__ == '__main__':
    api.run() 

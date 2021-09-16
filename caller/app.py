from __future__ import print_function, unicode_literals
import random
import time
import docker
import re
from pprint import pprint
from PyInquirer import prompt, print_json
from flask import Flask, jsonify, request

app = Flask(__name__)
docker_client = docker.from_env()

@app.route('/', methods=["GET"])
def hello():
  return 'Hello world'

@app.route('/images', methods=["GET"])
def get_images():
  try:
    images_list = docker_client.images.list(all=True)
    return jsonify({
      'success': True, 
      'images': [{'id': image.short_id, 'tags': image.tags} for image in images_list if image.tags]
    }), 200
  except:
    return jsonify({'success': False, 'msg': 'Something went wrong'}), 500


@app.route('/images', methods=["POST"])
def run_images():
  try:
    request_data = request.get_json()
    c = docker_client.containers.run(
        image = request_data['id'], 
        command = 'python3 main.py --task=\"{}\"'.format(request_data['task']), 
        detach=True,
        volumes={
          'mock-volume': {'bind': '/storage', 'mode': 'rw'}
        }
      )
    return jsonify({
      'success': True,
      'container': c.short_id
    }), 200
  except:
    return jsonify({'success': False, 'msg': 'Something went wrong'}), 500


@app.route('/process', methods=["POST"])
def run_process():
  """
    data: {
      images: List of docker image to run
      
    }
  """
  try:
    request_data = request.get_json()
    
    return jsonify({
      'success': True,
    }), 200
  except:
    return jsonify({'success': False, 'msg': 'Something went wrong'}), 500

# if __name__ == "__main__":
#   app.run(host='0.0.0.0', port='8080', debug=True)
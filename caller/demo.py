from __future__ import print_function, unicode_literals
import random
import time
import docker
import re
from pprint import pprint
from PyInquirer import prompt, print_json

docker_client = docker.from_env()


def main():
  images_list = docker_client.images.list(all=True)
  questions = [
    {
        'type': 'list',
        'name': 'image',
        'message': 'Which image is used to execute?',
        'choices': [
          'ID: {id} - Tags: {tags}'.format(id=image.short_id, tags=image.tags) for image in images_list if image.tags
        ],
        'filter': lambda val: re.search(r"sha256:\w*", val).group(0)
    }, 
    {
        'type': 'list',
        'name': 'task',
        'message': 'Which task is executed?',
        'choices': ['Dataset 1', 'Dataset 2', 'Dataset 3'],
    },
    {
        'type': 'confirm',
        'message': 'Run container in detach mode?',
        'name': 'detach',
        'default': True,
    },
  ]
  answers = prompt(questions)
  pprint(answers)

  c = docker_client.containers.run(
        image = answers['image'], 
        command = 'python3 main.py --task=\"{}\"'.format(answers['task']), 
        detach=answers['detach'],
        volumes={
          'mock-volume': {'bind': '/storage', 'mode': 'rw'}
        }
      )
  if answers['detach']:
    print('Container {} is running. Use docker logs to view'.format(c.short_id))
  else:
    print('Container {} finished'.format(c.short_id))

if __name__ == "__main__":
  main()
from typing import Any, List, Optional, Callable

from app.core import docker_client
from app import schemas

def run_serial_image(_layers: List[schemas.LayerBase], shared_volume: str):

  sort_order: Callable[[schemas.LayerBase], int] = lambda l: l.order
  layers: List[schemas.LayerBase] = sorted(_layers, key=sort_order)

  for i in range(len(layers)):
    l: schemas.LayerBase = layers[i]

    cmd: str = 'python3 main.py'
    for k, v in l.input_params.items():
      cmd += ' --{} {}'.format(k, v)
    
    print('Running {} with cmd: {} // and volume: {}'.format(l.docker_image, cmd, shared_volume))

    docker_client.containers.run(
      image = l.docker_image, 
      command = cmd, 
      volumes={
        shared_volume: {'bind': '/storage', 'mode': 'rw'}
      }
    )
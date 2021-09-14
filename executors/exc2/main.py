import random
import time
from tqdm import tqdm
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--task', type=str, default='Dataset 0', help='example argument')

def main(task: str):
  for i in tqdm(range(120)):
    time.sleep(1)
  
  acc = random.random()

  result = 'Exc1 finished task {task} ==> Acc: {acc: .2f}'.format(task=task, acc = acc)
  print(result)
  if os.path.isdir('/storage'):
    if not os.path.isdir('/storage/executor2'):
      os.mkdir('/storage/executor2')
    
    path = "/storage/executor2/{}.txt".format(int(time.time()))
    f = open(path, "w")
    f.write(result)
    f.close()
    print('Saved result to {}'.format(path))

if __name__ == "__main__":
  args = parser.parse_args()
  main(args.task)
import random
import time
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--task', type=str, default='ImageNet', help='example argument')

def main(task: str):
  for i in tqdm(range(180)):
    time.sleep(1)
  
  acc = random.random()
  print('Exc1 finished task {task} ==> Acc: {acc: .2f}'.format(task=task, acc = acc))

if __name__ == "__main__":
  args = parser.parse_args()
  main(args.task)
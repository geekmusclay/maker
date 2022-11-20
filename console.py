import re
import argparse
import json

from pathlib import Path
from lib.logger import Logger

def to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

parser = argparse.ArgumentParser(
                    prog = 'GeekMusclay maker',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

parser.add_argument('command') # Positional argument
parser.add_argument('name')

logger = Logger()

args = parser.parse_args()
parts = args.command.split(':')
if 2 != len(parts):
    logger.log_fail('Wrong command construction')
    exit()

# Get config
file = open('./config.json')
config = json.load(file)

if 'cmd_file' not in config:
    logger.log_fail('Wrong configuration file')
    exit()

file = open(config['cmd_file'])
data = json.load(file)

# Check all keys
if parts[1] not in data:
    logger.log_fail('Commad does not exist')
    exit()

if 'src' not in data[parts[1]]:
    logger.log_fail('Source does not exist')
    exit()

if 'dest' not in data[parts[1]]:
    logger.log_fail('Destination does not exist')
    exit()

if 'ext' not in data[parts[1]]:
    logger.log_fail('No file extension')
    exit()

# Making directory
path = Path(data[parts[1]]['dest'])
path.mkdir(parents=True)

name = parts[1].capitalize()
res = args.name
logger.log_success('Lauching command ' + args.command)

fin = open(data[parts[1]]['src'], "rt")
fout = open(data[parts[1]]['dest'] + "/" + res + name + '.' + data[parts[1]]['ext'], "wt")

for line in fin:
    replaced = line.replace('{name}', name).replace('{lower}', name.lower()).replace('{snake}', to_snake(name)).replace('{upper}', name.upper())
    fout.write(replaced)
    
fin.close()
fout.close()

logger.log_success('Done')
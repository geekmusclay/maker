import re
import argparse
import json

from pathlib import Path
from lib.logger import Logger

def to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def replace(string, name):
    return string.replace('{name}', name).replace('{lower}', name.lower()).replace('{snake}', to_snake(name)).replace('{upper}', name.upper())

def manage_simple(config):
    if 'src' not in config:
        logger.log_fail('Source does not exist')
        exit()

    if 'dest' not in config:
        logger.log_fail('Destination does not exist')
        exit()

    if 'ext' not in config:
        logger.log_fail('No file extension')
        exit()

    # Making directory
    path = Path(config['dest'])
    path.mkdir(parents=True)

    name = args.name
    logger.log_success('Treatment for ' + config['src'])

    fin = open(config['src'], "rt")
    fout = open(config['dest'] + "/" + replace(config['file_name'], name) + '.' + config['ext'], "wt")

    for line in fin:
        replaced = replace(line, name)
        fout.write(replaced)
        
    fin.close()
    fout.close()

    logger.log_success('Done')

def manage_bulk(config):
    for target in config['targets']:
        manage_simple(target)

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

if 'type' not in data[parts[1]]:
    logger.log_fail('Commad does not have any type')
    exit()

if 'simple' == data[parts[1]]['type']:
    manage_simple(data[parts[1]])
elif 'bulk' == data[parts[1]]['type']:
    manage_bulk(data[parts[1]])
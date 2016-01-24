#!/usr/bin/env python

# Import Kindle highlights in python
# Author - Tudor Barbu <hello@tudorbarbu.ninja>
# Licence - Apache 2

import os, sys, json, ConfigParser, trello

def get_app_config():
    config_path = os.path.expanduser('~/.trello-kindle-config')
    if os.path.exists(config_path) == False:
        raise Exception("Cannot find config file: " + config_path)

    config = ConfigParser.SafeConfigParser()
    fp = open(config_path, 'r')
    config.readfp(fp)
    fp.close()

    return {k: v for k,v in config.items('Config')}

def get_json_file(f):
    if os.path.exists(f) == False:
        raise Exception("Cannot find file: " + f)

    return json.load(open(f, 'r'))

def main():
    if len(sys.argv) != 2:
        raise Exception('Usage: %s <path_to_json>' % (sys.argv[0]))

    json   = get_json_file(sys.argv[1])
    config = get_app_config()
    cards  = trello.Cards(config['api_key'], config['api_token'])

    for item in json['highlights']:
        cards.new(item['text'], config['list_id'], item['location']['url'])

if __name__ == '__main__':
    code = 0
    try:
        main()
    except Exception as e:
        print e
        code = 1

    sys.exit(code)

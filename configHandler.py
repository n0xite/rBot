import configparser
import json

def read_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def splitter(category, name):
    return json.loads(configparser.ConfigParser().get(category, name))

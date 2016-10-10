import configparser
import os

DB_CONFIG_PATH = os.path.expanduser(os.path.join('~', 'config', 'puppet', 'db.ini'))


def db_config():
    _db_config = configparser.ConfigParser()
    _db_config.read(DB_CONFIG_PATH)

    return _db_config

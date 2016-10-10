import configparser
import os

from sqlalchemy import create_engine

import config
from models.puppet_model import PuppetModel


class CreateSchema(object):
    def __init__(self):
        self.db_config = config.db_config()

        _engine = create_engine('mysql+mysqldb://%s:%s@%s/%s' % (
            self.db_config['PUPPET']['Username'],
            self.db_config['PUPPET']['Password'],
            self.db_config['PUPPET']['Host'],
            self.db_config['PUPPET']['Database']
        ), echo=True)

        PuppetModel.metadata.create_all(_engine)


CreateSchema()

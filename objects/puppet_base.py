import redis
from redis import StrictRedis
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session

import config
from models.puppet_model import PuppetModel


class PuppetBase(object):
    def __init__(self):
        self.db_config = config.db_config()
        self.db_session = {}
        self.cache_session = {}

        #####################
        # MASTER DATA STORE #
        #####################
        _engine = create_engine('mysql+mysqldb://%s:%s@%s/%s' % (
            self.db_config['PUPPET']['Username'],
            self.db_config['PUPPET']['Password'],
            self.db_config['PUPPET']['Host'],
            self.db_config['PUPPET']['Database']
        ), echo=True)

        # Bind the engine to the metadata of the PuppetBase class so that the
        # declaratives can be accessed through a DBSession instance
        PuppetModel.metadata.bind = _engine

        _db_session = scoped_session(sessionmaker(bind=_engine))
        self.db_session['puppet'] = _db_session()

        ######################
        # SESSION DATA CACHE #
        ######################
        self.cache_session['sessions'] = redis.StrictRedis(
            host=self.db_config['SESSION-CACHE']['Host'],
            port=self.db_config['SESSION-CACHE']['Port'],
            db=self.db_config['SESSION-CACHE']['Database'],
            socket_connect_timeout=3
        )

    def get_db(self, db_name) -> Session:
        if db_name in self.db_session:
            return self.db_session[db_name]
        else:
            raise Exception('Database not found')

    def get_cache(self, cache_name) -> StrictRedis:
        if cache_name in self.cache_session:
            return self.cache_session[cache_name]
        else:
            raise Exception('Cache session not found')

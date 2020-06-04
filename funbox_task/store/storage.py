from .link import LinkStore
from redis.client import Redis
from redis_conn import RedisConn


class MainStorage(LinkStore):
    r: Redis

    def __init__(self, config):
        self.r = RedisConn(config).get_r_conn()


import redis


class RedisConn(object):
    def __init__(self, config):
        self.r_conn = redis.Redis(host=config.get('host'),
                                  port=config.get('port'),
                                  db=config.get('database'))

    def get_r_conn(self):
        return self.r_conn

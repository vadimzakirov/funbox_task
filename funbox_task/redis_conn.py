import redis


class RedisConn(object):
    """
    Implements Redis connection to use it in Store Classes
    """
    def __init__(self, config):
        """
        :param config: Dict of YAML config
        """
        self.r_conn = redis.Redis(host=config.get('host'),
                                  port=config.get('port'),
                                  db=config.get('database'))

    def get_r_conn(self):
        """
        :return: Redis.Client
        """
        return self.r_conn

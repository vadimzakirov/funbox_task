from redis.client import Redis


class BaseStore(object):
    """
    Construct base Redis operations
    """
    r: Redis
    set_name = 'domains'

    def scan_keys(self, pattern):
        """
        :param pattern: Scan pattern
        :return: list of keys
        """
        result = []
        cur, keys = self.r.scan(cursor=0, match=pattern, count=2)
        result.extend(keys)
        while cur != 0:
            cur, keys = self.r.scan(cursor=cur, match=pattern, count=2)
            result.extend(keys)
        return result

    def get_list_elements(self, key):
        """
        :param key: Redis key that contains List
        :return: List
        """
        lenght = self.r.llen(key)
        print(self.r.lrange(key, 0, lenght))

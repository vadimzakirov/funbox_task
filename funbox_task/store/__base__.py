from redis.client import Redis


class BaseStore(object):
    r: Redis
    set_name = 'domains'

    def scan_keys(self, pattern):
        result = []
        cur, keys = self.r.scan(cursor=0, match=pattern, count=2)
        result.extend(keys)
        while cur != 0:
            cur, keys = self.r.scan(cursor=cur, match=pattern, count=2)
            result.extend(keys)
        return result

    def get_list_elements(self, key):
        lenght = self.r.llen(key)
        print(self.r.lrange(key, 0, lenght))

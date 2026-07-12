import time


class MemoryCache:

    def __init__(self):
        self.storage = {}

    def get(self, key):

        item = self.storage.get(key)

        if item is None:
            return None

        value, expire = item

        if expire < time.time():
            del self.storage[key]
            return None

        return value

    def set(self, key, value, ttl=300):

        self.storage[key] = (
            value,
            time.time() + ttl
        )
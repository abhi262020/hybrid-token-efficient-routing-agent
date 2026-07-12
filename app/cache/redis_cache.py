import redis


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def get(key):

    return redis_client.get(key)


def set(key, value, ttl=300):

    redis_client.setex(
        key,
        ttl,
        value
    )
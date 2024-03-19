import functools


def cache(fn):
    _cache = dict()

    @functools.wraps(fn)
    def cacher(*args):
        if args not in _cache:
            _cache[args] = fn(*args)
        return _cache[args]
    return cacher


@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(38))

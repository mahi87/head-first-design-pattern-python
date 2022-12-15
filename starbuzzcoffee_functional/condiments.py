import inspect

def with_mocha(cost_fn):
    return lambda: cost_fn() + 0.20

def with_milk(cost_fn):
    def inner(*args, **kwargs):
        ref = args[0] if args else None
        if ref:
            return cost_fn(ref) + 0.5
        return cost_fn() + 0.5
    return inner

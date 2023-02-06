import collections
import functools

func_register = set()


def strategy_register(active=True):
    def register(func):
        func_register.add(func) if active is True else func_register.discard(func)
        print(func_register)
        return func

    return register


Customer = collections.namedtuple("Customer", "name fidelity")


class Goods:

    def __init__(self, name, quality, unit_price):
        self.name = name
        self.quality = quality
        self.unit_price = unit_price

    def total(self):
        return self.unit_price * self.quality


class Order:

    def __init__(self, customer, items, strategy=None):
        self.customer = customer
        self.items = list(items)
        self.strategy = strategy

    def total_price(self):
        """折扣前订单总价"""
        return sum([item.total() for item in self.items])

    def actual_price(self):
        """折扣后订单价格"""
        pass


@strategy_register()
def fidelity_strategy(order):
    pass


@strategy_register()
def goods_strategy(order):
    pass


@strategy_register()
def order_strategy(order):
    pass


def strategy_controller(order):
    pass


print(order_strategy)

a = {}
b = collections.defaultdict(set)

cc = a.setdefault("a", "b")
print(a, cc)
print(b["b"])
print(b)

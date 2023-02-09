import abc
import random


class TomBola(abc.ABC):

    def __init__(self, iterable_obj):
        self._items = list(iterable_obj)

    # 虚拟方法，子类必须复写该方法才能创建实例，否则就是无法创建实例的虚拟子类，创建实例会报错
    @abc.abstractmethod
    def pick(self):
        """
        随机删除一个元素, 并将被删除的元素返回
        """

    # 虚拟方法
    @abc.abstractmethod
    def load(self, items):
        """
        将传入的items或item添加到self._items中
        """

    def inspect(self):
        return self._items[0]

    def loaded(self):
        return bool(self._items)


class TomBolaChildA(TomBola):

    def pick(self):
        pass

    def load(self, items):
        pass


class TomBolaChildB(TomBola):
    def pick(self):
        pass

    def load(self, items):
        pass

    def inspect(self):
        pass

    def loaded(self):
        pass


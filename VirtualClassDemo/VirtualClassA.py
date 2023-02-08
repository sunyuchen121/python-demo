import abc
import random


class TomBola(abc.ABC):

    def __init__(self, iterable_obj):
        self._items = list(iterable_obj)

    @abc.abstractmethod
    def pick(self):
        """
        随机删除一个元素, 并将被删除的元素返回
        """

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

    def pick(self, position=-1):
        pass

    def load(self, item):
        pass


class TomBolaChildB(TomBola):
    def pick(self, position=-1):
        pass

    def load(self, item):
        pass

    def inspect(self):
        pass

    def loaded(self):
        pass

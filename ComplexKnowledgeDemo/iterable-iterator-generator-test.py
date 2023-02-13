import itertools
from collections.abc import Iterable, Iterator, Generator


class IterableObj:
    def __init__(self, name, elements):
        self.name = name
        self.elements = [ele for ele in elements if len(ele) >= 3]

    def __iter__(self):
        print(f"{self.__class__.__name__} __iter__")
        return IteratorObj(self.elements)


class IteratorObj:
    def __init__(self, elements):
        self.elements = elements
        self.index = -1

    def __iter__(self):
        print(f"{self.__class__.__name__} __iter__")
        return self

    def __next__(self):
        print(f"{self.__class__.__name__} __next__")
        self.index += 1
        try:
            return self.elements[self.index]
        except IndexError:
            raise StopIteration

    def roll_back(self):
        pass


IteratorObj_1 = IteratorObj(["abcd", "3", "11111", "l9000"])
for iii in IteratorObj_1:
    print(iii)
print("-" * 50)
# 此时 迭代器IteratorObj_1 self.index已经超出self.elements，将不会再有元素产出
for iii in IteratorObj_1:
    print(iii)

print("-" * 100)

# 正确方式是：把Iterable当作迭代器的生成工厂，每次iter(Iterable)都生成一个新的迭代器。不能把Iterator当作操作实例，因为他只能迭代一次
# Iterable的__iter__返回一个Iterator实例，可以多次迭代Iterable的实例，每次都使用新的Iterator实例完成迭代
# 或者 Iterable的__iter__返回一个迭代器实例，让迭代器自己实现迭代细节，参照IterableSingle
# 最常用的方式：只定义一个可迭代对象，__iter__方法使用生成器函数实现，例如IterableSingleCommon
IterableObj_1 = IterableObj("IterableObj_1", ["abcd", "3", "11111", "l9000"])
for aaa in IterableObj_1:
    print(aaa)
print("-" * 50)
for aaa in IterableObj_1:
    print(aaa)


class IterableSingle:

    def __init__(self, name, elements):
        self.name = name
        self.elements = [ele for ele in elements if len(ele) >= 3]

        # ↓↓↓ 下边的的生成器表达式本质是 把一个生成器赋值给self.elements，即self.elements只可迭代生成一轮数据
        # ↓↓↓ 不能把 迭代器/生成器 赋值给 类属性/实例属性，否则迭代一次这个属性后，生成器/迭代器就空了，无法再次使用
        # self.elements = (ele for ele in elements if len(ele) >= 3)

    def __iter__(self):
        # 1.
        # return (ele for ele in self.elements)
        # 2.
        return iter(self.elements)


class IterableSingleCommon:
    def __init__(self, name, elements):
        self.name = name
        self.elements = [ele for ele in elements if len(ele) >= 3]

    def __iter__(self):
        index = 0
        try:
            while True:
                yield self.elements[index]
                index += 1
        except IndexError:
            # 生成器函数中的return 会触发生成器对象抛出StopIteration异常。不能在__iter__中直接raise
            return


print("-" * 100)

iterable_obj_1 = IterableSingle("iterable_obj1", ["abcd", "3", "11111", "l9000"])
for aaa in iterable_obj_1:
    print(f"---------{aaa}--------")

print("-" * 50)

for aaa in iterable_obj_1:
    print(f"---------{aaa}--------")

print("-" * 100)

iterable_obj_2 = IterableSingleCommon("iterable_obj2", ["abcd", "3", "11111", "l9000"])
for bbb in iterable_obj_2:
    print(f"****{bbb}****")

print("-" * 50)

for bbb in iterable_obj_2:
    print(f"****{bbb}****")

print("-" * 100)


def gen_number(start, step=1, stop=None):
    print("----------calling gen_number----------")
    while not stop or start <= stop:
        print("----------nexting gen_number----------")
        yield start
        start += step


# yield
# yield from
# 生成器表达式


for i in gen_number(1, 2, 10):
    print(i)

print("-" * 50)

container_a = gen_number(1, 2, 10)
next(container_a)
next(container_a)
next(container_a)
next(container_a)

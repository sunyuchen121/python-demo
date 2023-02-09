from collections.abc import Iterable, Iterator, Generator


class GetitemIterableObj(object):
    _index_mapping = {
        "a": 1, "b": 2,
        "c": 3, "d": 4
    }

    def __init__(self, iterabl_obj):
        self.data_g = list(iterabl_obj)

    def __getitem__(self, item):
        print("item---> {}".format(item))
        return self.data_g[item]

    def __getattr__(self, item):
        if item in self._index_mapping:
            return self.data_g[self._index_mapping[item]]
        else:
            return None


inst_a = GetitemIterableObj((1, 2, 3, 4, 5))
print(inst_a.data_g)
print(inst_a[1])
print(inst_a[-1])
print(inst_a[1:2])
print(inst_a[1::2])
# print(inst_a[1:1:1, 2])

print("=" * 20)

for i in inst_a:
    print(i)

param_a, *_, param_b = inst_a
print(param_a, *_, param_b)

print(f"-------{isinstance(inst_a, Iterable)}-------")
print(tuple(inst_a))
print(dir(inst_a))

print("=" * 50)

# 获取实例属性的三种方式，__getattr__对第一种 inst.__dict__[key]不生效
# print(inst_a.__dict__["a"])
print(inst_a.a)
print(getattr(inst_a, "a"))

print(inst_a.__class__)


class TestGetattrAndGetattritube(object):
    class_p1 = "asd"
    class_p2 = "dsa"

    def __init__(self, param1, param2):
        self.inst_p1 = param1
        self.inst_p2 = param2

    def __getattribute__(self, item):
        print("long     {}".format(item))
        if item == "inst_p2":
            return "覆盖inst_p2"
        raise AttributeError

    def __getattr__(self, item):
        print("short     {}".format(item))
        if item == "undefined_p":
            return "11112222333"


print('\n\n\n')
test_inst = TestGetattrAndGetattritube("lll", "kkk")
print(test_inst.class_p1)
print(test_inst.__dict__)
print(getattr(test_inst, "inst_p2"))
print(TestGetattrAndGetattritube.class_p2)

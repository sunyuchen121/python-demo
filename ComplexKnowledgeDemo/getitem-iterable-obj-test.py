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

# 获取实例属性的三种方式，__getattr__对第一种 inst.__dict__[key]不生效,因为他获取的属性是inst.__dict__，然后去字典中找key
# 在没有属性拦截器等情况下，不可能找不到__dict__，所有也就走不到__getattr__

# print(inst_a.__dict__["a"])
print(inst_a.a)
print(getattr(inst_a, "a"))

print(inst_a.__class__)


class TestGetattrAndGetattribute(object):
    class_p1 = "class_p1__value"
    class_p2 = "class_p2__value"

    def __init__(self, param1, param2):
        self.inst_p1 = param1
        self.inst_p2 = param2

    def __getattribute__(self, item):
        print("拦截器     {}".format(item))
        if item == "inst_p2":
            return "拦截inst_p2"
        # __getattribute__拦截器中raise这个异常会继续走__getattr__，否则会返回None
        raise AttributeError

    def __getattr__(self, item):
        print("兜底机制     {}".format(item))
        if item == "undefined_p":
            return "11112222333"
        # 正常需要报下面的异常，否则会返回None，与实际不符。为了测试方便先注释掉
        # raise AttributeError


print("---" * 20 + '\n\n\n')
print("以下内容需要注释和不注释__getattribute__方法分别测试，会有不同的内容" + '\n\n\n' + "---" * 20)
test_inst = TestGetattrAndGetattribute("lll", "kkk")
print(test_inst.class_p1)
print(test_inst.__dict__)
print(test_inst.__class__)
print(getattr(test_inst, "inst_p2"))
print(test_inst.undefined_p)

test_inst.class_p2 = "redefine class_p2"
print(TestGetattrAndGetattribute.class_p2)
print(test_inst.class_p2)

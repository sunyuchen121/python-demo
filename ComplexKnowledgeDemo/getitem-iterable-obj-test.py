from collections.abc import Iterable, Iterator, Generator


class GetitemIterableObj(object):

    def __init__(self, iterabl_obj):
        self.data_g = list(iterabl_obj)

    def __getitem__(self, item):
        print("item---> {}".format(item))
        return self.data_g[item]


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

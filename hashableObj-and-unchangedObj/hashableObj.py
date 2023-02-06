class HashableObj:

    def __init__(self, num, name):
        self._index = num
        self._name = name

    def __eq__(self, other):
        if isinstance(other, HashableObj):
            return self.__hash__() == other.__hash__()
        return False

    def __hash__(self):
        hash_value = hash((self._index, self._name))
        print(f"{str(self)} hash-value: {hash_value}")
        return hash_value

    def __repr__(self):
        return f"HashObj:{self._index}-{self._name}"


inst_a = HashableObj(1, "syc")
inst_b = HashableObj(1, "syc")
inst_c = HashableObj(2, "syc")

print(inst_a == inst_b)
print(inst_c == inst_a)
# inst_a/b/c都可哈希，但a==b，所以set里只有俩元素
print({inst_a, inst_b, inst_c})

print(any([100, 0, 10]))
print(any([]))
print(all([100, 0, 10]))
print(all([]))


def test_default_list_param(default_param=[]):
    print(default_param)
    default_param.append(1)


test_default_list_param()
test_default_list_param()

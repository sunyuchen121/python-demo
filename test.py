_list = [1, 2, 3]
_tuple = (1, 2, _list)
print(_tuple)
# print(hash(_tuple))
_list.append(4)
print(_tuple)


def test(iterable=None, /, **kwds):
    print(iterable)
    print(kwds)
    # None
    # {'iterable': 111}


test(iterable=111)


# a = (1, 2, {3, 4})
# b = {a, 2}

class TestA(object):
    pass


a = TestA()
b = TestA()

print(hash(a), hash(b))

test_set_a = {a, b}
# 性能不如直接用{}创建set
test_set_b = set([a, b])

c = (a, b)
d = (1, 2)
# 在内置的可哈希对象中，整数、字符串和字节串又有点特殊。整数的哈希值是它本身，而字符串和字节串在计算哈希值时会加入随机盐值，并且在不同的进程中使用的盐值不一样，在同一个进程中一直使用同一个盐值。
# 自定义类和自定义类的对象默认是可哈希的，但每次计算的哈希值是不可控的，与其id有关系但又不同于id函数的返回值。
e = ("aaa111", a, 90)
print(f"{hash(c)}\n{hash(d)}\n{hash(e)}")

# https://www.runoob.com/python/python-func-zip.html
test_zip_func = zip([1, 2, 3], ["a", "b", "c"], ("_1", "_2", "_3"))
print(list(test_zip_func))


class TestInitParamEdit(object):
    def __init__(self, _list):
        self._list = _list

    def print(self):
        print(self._list, id(self._list))


aaa = [1, 2, [3, 3, 3]]
test_inst = TestInitParamEdit(aaa)
aaa.append("test_add")
test_inst.print()
print(id(aaa))


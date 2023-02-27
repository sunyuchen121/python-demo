class Test:
    _name = "syc"
    _age = 99

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __setattr__(self, key, value):
        print(key, value)
        if key == "ddd":
            key = "ppp"
        # 使用以下两种之一
        # self.__dict__[key] = value
        super(Test, self).__setattr__(key, value)

        # 不能使用self.key = value赋值，会死循环

    # def __getattribute__(self, item):
    #     pass

    # def __getattr__(self, item):
    #     pass
    #
    # def __getitem__(self, item):
    #     pass

    # def __delattr__(self, item):
    #     pass

    # def __delitem__(self, key):
    #     pass


print(Test.__dict__)

test_inst = Test("ddd", 18)

print(test_inst.__dict__)
test_inst["test_setitem"] = "success"
# test_inst[{111}] = 5
print(test_inst.__dict__)
print(test_inst.test_setitem)

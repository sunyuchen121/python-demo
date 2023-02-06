"""
实现简单的自定义散列表
todo 性能待提升
"""
from functools import partial, partialmethod, lru_cache
from operator import attrgetter, itemgetter, methodcaller
from types import MappingProxyType



class HashTableBase:
    def __init__(self, _iters):
        self.length = len(_iters)
        self.volume = 2 * self.length

    def _gen_key_basic(self, _key):
        """
        获取key的hash值与散列表的索引
        :param _key:
        :return:
        """
        _hash_value = hash(_key)
        _index = _hash_value % self.volume
        return _hash_value, _index


class HashTableZipper(HashTableBase):
    """
    拉链法
    """

    def __init__(self, _iters, *_, default_factory=None):
        super().__init__(_iters)
        # 结合collections.defaultdict 和 dict的setdefault方法
        self.default_factory = default_factory
        self.buckets = [[] for i in range(self.volume)]
        self._assign_buckets(_iters, True)

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    # todo set机制
    def setdefault(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return self.__setitem__(key, default if default else self.default_factory)

    # todo 扩容机制
    # todo 原bucket.clear() 与 使用temp_volume的内存使用差异
    def _auto_extend_volume(self):
        """
        扩容volume并rewrite buckets, set时判断是否需要扩容, 参照python中dict扩容机制, 预留约1/3空表
        :return:
        """
        self.temp_volume = []

    def _assign_buckets(self, _iters, rewrite=False):
        """
        调整hashtable必须使用该方法！！！
        :param _iters:
        :return:
        """
        for _iter in _iters:
            _k, _v, *_ = _iter
            _hash_value, _index = self._gen_key_basic(_k)
            self.buckets[_index].append((_k, _v))
        if rewrite is False:
            self.length += len(_iters)

    def _get_element_list(self, _key=None, _index=0):
        if _key:
            _index = self._gen_key_basic(_key)[1]
        return self.buckets[_index]

    def __setitem__(self, key, value):
        _hash_value, _index = self._gen_key_basic(key)
        element_list = self._get_element_list(_index=_index)
        # todo 判断是否需要扩容
        for _i, element, in enumerate(element_list):
            # 修改现有key-value
            if element[0] == key:
                self.buckets[_index][_i] = (key, value)
                break
        # 新增key-value
        else:
            self._assign_buckets([(key, value)])
        return value

    # 非内置映射类型和非继承内置映射类型的自定义类，__getitem__未找到key时不会走__missing__
    # def __missing__(self, key):
    #     raise KeyError(key)

    def __getitem__(self, item):
        element_list = self._get_element_list(item)
        for _k, _v in element_list:
            if _k == item:
                return _v
        else:
            raise KeyError(item)

    def __repr__(self):
        return str(self.buckets)

    def __contains__(self, item):
        element_list = self._get_element_list(item)
        for _k, _ in element_list:
            if _k == item:
                return True
        else:
            return False

    # if判断 和 bool() 都会走 __bool__
    def __bool__(self):
        return any(self.buckets)

    def __len__(self):
        return self.length

    def keys(self):

        return

    def values(self):

        return

    def items(self):

        return

    def update(self, _iter):
        """
        需要实现本方法的set机制, 不要for循环调用__setitem__, 性能差
        :param _iter:
        :return:
        """


class HashTableIncremental(HashTableBase):
    """
    开放式寻址法，简单实现几个方法
    暂时实现的方式，不支持key为None的键值对
    _assign_buckets _resize_buckets __settiem__ __getitem__
    """

    def __init__(self, _iters):
        super().__init__(_iters)
        # 默认为入参可迭代数据的两倍长度的散列表
        self.buckets = [None] * self.volume
        self._assign_buckets(_iters)

    def _assign_buckets(self, _iters):
        for _iter in _iters:
            _key, _value, *_ = _iter
            hash_value, _index = self._gen_key_basic(_key)
            if self.buckets[_index] is None:
                self.buckets[_index] = (_key, _value)
            else:
                origin_index = _index
                _index += 1

                while True:
                    if origin_index == _index:
                        break
                    if _index == self.volume - 1:
                        _index = 0
                        continue
                    if self.buckets[_index] is None:
                        self.buckets[_index] = (_key, _value)
                        break
                    _index += 1

    def _resize_buckets(self):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __repr__(self):
        return str(self.buckets)


if __name__ == "__main__":
    zipper_obj = HashTableZipper([
        (1, "value_1"),
        ("key_2", "value_2", "arg_2"),
        ("key_3", "value_3"),
        ("key_4", "value_4"),
        ("key_5", "value_5"),
        ("key_6", "value_6"),
        (15, "value_7", "arg_7", "arg_77")
    ])

    increment_obj = HashTableIncremental([
        (1, "value_1"),
        ("key_2", "value_2", "arg_2"),
        ("key_3", "value_3"),
        ("key_4", "value_4"),
        ("key_5", "value_5"),
        ("key_6", "value_6"),
        (15, "value_7", "arg_7", "arg_77")
    ])
    # print(zipper_obj[100])
    print(zipper_obj.get(100, "default_value"))
    print(zipper_obj)
    # if判断 和 bool() 都会走 __bool__
    if zipper_obj:
        print(bool(zipper_obj))

    zipper_obj[1] = "test_edit zipper_obj[1]"
    print(zipper_obj)
    print(increment_obj)


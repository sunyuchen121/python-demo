"""
通过obj.data_l1.data_l2.xxxx的形式获取多层嵌套的映射类型的数据，如多层嵌套的json等。
当obj.data_l1.data_l2.xxxx获取的是最内层的key时，返回对应的value，
不是最内层的key时，返回一个对象，对象包含该key的所有内层数据
"""

from collections import abc
import keyword


class JsonResolve:
    def __init__(self, mapping):
        self._extra_keys = []
        self._data = {}
        for _k, _v in mapping.items():
            if keyword.iskeyword(_k):
                self._extra_keys.append(_k)
                _k = f"_{_k}"
            self._data.update({
                _k: _v
            })

    def __getattr__(self, item):
        print(item)
        if hasattr(self._data, item):
            return getattr(self._data, item)
        else:
            return self.build(self._data[item])

    def extra_keys(self):
        return self._extra_keys

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return JsonResolve(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [JsonResolve(obj_) for obj_ in obj]
        return obj

    def __repr__(self):
        return f"{self._data}"


class JsonResolveUpdate:
    def __new__(cls, mapping):
        if isinstance(mapping, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(mapping, abc.MutableSequence):
            return [JsonResolveUpdate(obj_) for obj_ in mapping]
        else:
            return mapping

    def __init__(self, mapping):
        self._extra_keys = []
        self._data = {}
        for _k, _v in mapping.items():
            if keyword.iskeyword(_k):
                self._extra_keys.append(_k)
                _k = f"_{_k}"
            self._data.update({
                _k: _v
            })

    def __getattr__(self, item):
        print(item)
        if hasattr(self._data, item):
            return getattr(self._data, item)
        else:
            return JsonResolveUpdate(item)

    def extra_keys(self):
        return self._extra_keys

    def __repr__(self):
        return f"{self._data}"


if __name__ == "__main__":
    json_data = {
        "a": [{"a1": "a1", "a2": "a2"}],
        "b": [{"b1": "b1", "b2": "b2"}],
        "c": [{"c1": "c1", "c2": "c2"}]
    }

    json_resolve_obj = JsonResolve(json_data)
    print(json_resolve_obj.a[0].a1)

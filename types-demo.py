from types import MappingProxyType

_d1 = {"name": "_d1"}
_d1_proxy = MappingProxyType(_d1)
print(_d1_proxy)

try:
    _d1_proxy["name"] = "edit _d1_proxy"
except Exception as e:
    print(e)
print(_d1_proxy)

_d1["name"] = "edit origin _d1"
print(_d1_proxy)

_list = [1, 2, (1, 2), {"k1": "v1"}]
_dict = {"key1": "value1", "key2": [1, 2, 3], "key3": "value3", "key4": "value4"}
_set = {1, 2, 3, 4}
_truple = (1, 2, [1, 2], {"a": "b"})
_str = "hello"

_list2 = [5, 3, 2, 0, 9]

_l1, _l2, _l3, _l4 = _list
_d1, _d2, _d3, _d4 = _dict
_s1, _s2, _s3, _s4 = _set
_t1, _t2, _t3, _t4 = _truple
_str1, _str2, _str3, _str4, _str5 = _str

# 赋值语句中，*param的结果，永远为列表，即便为空也是空列表
# 函数中的可变参数 *args，获取的args为元组，不是列表
_l_min, *drop, _l_max = _list2




















print(111)

from collections import defaultdict, deque, OrderedDict, Counter, namedtuple

# defaultdict 和 dict.setdefault:
# defaultdict.get()方法不会设置默认值，defaultdict[key]才会设置默认值
default_dict_1 = defaultdict(list)
default_dict_2 = {}
keywords = ["app", "body", "apple", "ctrl", "create"]

for word in keywords:
    key_ = word[0]
    default_dict_1[key_].append(word)
    default_dict_2.setdefault(key_, []).append(word)
print(default_dict_1)
print(default_dict_2)

# OrderedDict


# Counter


# namedtuple

print(11111111)

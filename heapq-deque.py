import heapq

links = [
    "https://blog.csdn.net/weixin_42127358/article/details/123662898",
    "https://blog.csdn.net/weixin_43790276/article/details/104033696"
]

# heappush(_list, num)，先创建一个空堆，然后将数据一个一个地添加到堆中。每添加一个数据后，heap都满足小顶堆的特性。

# heapify(_list)，直接将数据列表调整成一个小顶堆(调整的原理参考上面堆排序的文章，heapq库已经实现了)。


test_deque = [100, 60, 90, 78]
heapq.heapify(test_deque)
print(test_deque)

_deque = []
heapq.heappush(_deque, 6)
heapq.heappush(_deque, 10)
heapq.heappush(_deque, 4)
print(_deque)
print(heapq.heappop(_deque))
print(heapq.heappop(_deque))
print(heapq.heappop(_deque))


# 实现按优先级排序的队列

class ItemObj(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "ItemObj({})".format(self.name)


class DynamicDeque(object):
    def __init__(self):
        self._deque = []
        # 记录进入的顺序，优先级相同的按照进入顺序从早到晚排列
        self._index = 0

    def put(self, item, priority):
        # headpq是小顶堆，按照优先级从小到大排的，-priority按照优先级从大到小排
        # 元组排序，会从第一个元素开始排，第一个元素相同才会走第二个元素的排序，依此类推
        heapq.heappush(self._deque, (-priority, self._index, item))
        self._index += 1
        return self._deque

    def pop(self):
        return heapq.heappop(self._deque)[-1]

    def get(self):
        return self._deque

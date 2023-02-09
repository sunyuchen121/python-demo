import collections
import numbers

Card = collections.namedtuple('Card', ['num', 'hs'])


class CardQue:
    num = [str(n) for n in range(2, 11)] + list("JQKA")
    hs = ['♠', '♥', '♣', '♦']

    def __init__(self):
        self.cards = [Card(n, h) for n in self.num for h in self.hs]

    def __getitem__(self, item):
        print(item)
        # if isinstance(item, int):
        #     return self.cards[item]
        # elif isinstance(item, str):
        #     return "str"
        # else:
        #     print("KeyError: Key Must in Int or String !")
        if isinstance(item, (numbers.Integral, slice)):
            # 实现细节交给list
            return self.cards[item]
        raise TypeError("CardQue indices must be integers or slices!")

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return "__str__"

    def __repr__(self):
        return "__repr__"



if __name__ == '__main__':
    CardInst = CardQue()
    print(len(CardInst))
    print(CardInst[2:6])
    # print(CardInst["asd555"])

    for card in CardInst:
        print('\n')

    print("%r" % CardInst)
    print(CardInst)
    print("{}".format(CardInst))
    print(str(CardInst))
    print("%s" % CardInst)


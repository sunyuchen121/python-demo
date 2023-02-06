# 位置参数


# 关键字参数


# 可变参数


# 可变关键字参数


# 仅限位置参数


# 仅限关键字参数


def gen_birthday(name, gender, *args, age, **kwargs):
    """
    :param name:
    :param gender:
    :param args:
    :param age:
    :param kwargs:
    :return:
    """
    print("{}\n{}\n{}\n{}\n{}".format(name, gender, args, age, kwargs))


*list_zip1, last_s = [1, 2, 3, 4, 5]
gen_birthday("name", *list_zip1, age=100, test="test_param")


def test_default_param(_list=[1], _dict={1: 1}):
    print(_list)
    print(_dict)
    _list.append(2)
    _dict.update({2: 2})
    print(_list)
    print(_dict)


test_default_param()
test_default_param()

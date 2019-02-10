# coding:utf-8
"""
@file: 5.10.py
@time: 2/10/2019 9:50 PM
@contact: dabuwang
@content:
支持函数式编程的包
5.10.1　operator模块
5.10.2　使用functools.partial冻结参数
"""

def test_510_1_1():
    from operator import mul
    print reduce(lambda a,b: a*b, range(1,4))
    print reduce(mul, range(1,4))

def test_510_1_2():
    """
    operator 模块中还有一类函数，能替代从序列中取出元素或读取对象属性的 lambda 表达式：
    因此，itemgetter 和 attrgetter 其实会自行构建函数。
    - itemgetter 的常见用途：根据元组的某个字段给元组列表排序。
    - attrgetter 与 itemgetter 作用类似，它创建的函数根据名称提取对象的属性。
        如果把多个属性名传给 attrgetter，它也会返回提取的值构成的元组。
        此外，如果参数名中包含 .（点号），attrgetter 会深入嵌套对象，获取指定的属性。
        我们要构建一个嵌套结构，这样才能展示 attrgetter 如何处理包含点号的属性名。
    - 在 operator 模块余下的函数中，我们最后介绍一下 methodcaller。
        它的作用与 attrgetter 和 itemgetter 类似，它会自行创建函数。
        methodcaller 创建的函数会在对象上调用参数指定的方法，
    :return:
    """
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
        ]
    # region itemgetter
    print "##### itemgetter"
    from operator import itemgetter
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)
    print "----------------"
    for city in sorted(metro_data, key=lambda fields: fields[1]):
        print(city)

    cc_name = itemgetter(1, 0)
    for city in metro_data:
        print(cc_name(city))
    # endregion

    # region itemgetter
    print "##### attrgetter"
    from collections import namedtuple
    from operator import attrgetter

    LatLong = namedtuple('LatLong', 'lat long')
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')
    metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
        for name, cc, pop, (lat, long) in metro_data]

    print metro_areas[0]
    print metro_areas[0].coord.lat

    name_lat = attrgetter('name', 'coord.lat')  # 定义一个 attrgetter，获取 name 属性和嵌套的 coord.lat 属性
    for city in sorted(metro_areas, key=attrgetter('coord.lat')):
        print name_lat(city)
    # endregion

    # region methodcaller
    print "##### methodcaller"
    from operator import methodcaller
    s = 'The time has come'
    upcase = methodcaller('upper')
    print upcase(s)
    hiphenate = methodcaller('replace', ' ', '-')
    print hiphenate(s)
    # endregion


def test_510_2():
    # 使用functools.partial冻结参数
    from operator import mul
    from functools import partial
    triple = partial(mul, 3)    # 使用 mul 创建 triple 函数，把第一个定位参数定为 3。
    print triple(7)             # 测试 triple 函数 ==> mul(3,7) ==> 3 * 7 = 21。

    print list(map(lambda x: x*3, range(10)))
    print list(map(triple, range(10)))


    print "#### example2: "
    import unicodedata
    nfc = partial(unicodedata.normalize, 'NFC')
    s1 = 'café'
    s2 = u'café'
    print s1,s2
    print "s1 == s2", s1 == s2

    # python2.7 hit wrong: TypeError: normalize() argument 2 must be unicode, not str
    print "nfc(s1) == nfc(s2)", nfc(s1) == nfc(s2)


if __name__ == '__main__':
    # test_510_1_1()
    # test_510_1_2()
    test_510_2()
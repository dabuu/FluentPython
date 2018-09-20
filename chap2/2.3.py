# coding:utf-8
"""
@file: 2.3.py
@time: 2018/9/17 18:19
@contact: dabuwang
@desc: tuple is *NOT* only the unchange list
"""


def tuple_test_1():
    lax_coordinates = (33.9, -118.2)
    city, year, pop, chg, area = ('Tokyo', 2013, 32450, 0.66, 8014)
    traveler_ids = [("USA", 1111), ("BRA", 2222), ("ESP", 3333)]
    for passport in sorted(traveler_ids):
        print "%s/%s" % passport

    for country, _ in traveler_ids:
        print country


def tuple_test_2():
    """
    tuple unbox the values:
    useful usage:change two values with eachother
    :return:
    """
    a, b = 1, 2
    print "a=%s,b=%s" % (a, b)
    a, b = b, a
    print "a=%s,b=%s" % (a, b)

    #
    #tuple as args [with one star]
    #
    print divmod(20, 8)

    input_dict = (20, 8)
    (ret, remain) = divmod(*input_dict)
    print ret
    print remain



def tuple_test_3():
    """
    nested tuple unbox values
    :return:
    """
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print ('{:15}|{:^9}|{:^9}'.format("","lat.","long."))
    fmt = "{:15}|{:9.4f}|{:9.4f}"
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <=0:
            print fmt.format(name, latitude, longitude)

def tuple_test_4():
    """
    name for tuple
    :return:
    """
    from collections import namedtuple
    #具名的元组的定义： 类名，字段：后者可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
    City = namedtuple('City', 'name country population coordinates')

    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print tokyo
    print tokyo.population
    print tokyo.coordinates
    print tokyo[1]

    """
    City._make(<data>), which could create object with dict
    City._asdict(), which return tuple with "collections.OrderedDict" format
    """
    print tokyo._asdict()
    for key, value in tokyo._asdict().items():
        print "%s : %s" % (key, value)

if __name__ == '__main__':
    # tuple_test_1()
    # tuple_test_2()
    # tuple_test_3()
    tuple_test_4()

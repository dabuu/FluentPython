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

"""
## 元组的本质 ##
2012 年，我在 PyCon US 上贴了一张关于 ABC 语言的墙报。Guido 在开创 Python 语言之前曾做过 ABC 解释器方面的工作，因此他也去看了我的墙报。
我们聊了不少，而且都提到了 ABC 里的 compounds 类型。compounds 算得上是 Python 元组的鼻祖，它既支持平行赋值，又可以用在字典（dict）里作为合成键（ABC 里对应字典的类型是表格，即 table）。
但 compounds 不属于序列，它不是迭代类型，也不能通过下标来提取某个值，更不用说切片了。
要么把 compounds 对象当作整体来用，要么用平行赋值把里面所有的字段都提取出来，仅此而已。

我跟 Guido 说，上面这些限制让 compounds 的作用变得很明确，它只能用作没有字段名的记录。
Guido 回应说，Python 里的元组能当作序列来使用，其实是一个取巧的实现。

这其实体现了 Python 的实用主义，而实用主义是 Python 较之 ABC 更好用也更成功的原因。
从一个语言开发人员的角度来看，让元组具有序列的特性可能需要下点功夫，结果则是设计出了一个概念上并不如 compounds 纯粹，却更灵活的元组——它甚至能当成不可变的列表来使用。

说真的，不可变列表这种数据类型在编程语言里真的非常好用（其实 frozenlist 这个名字更酷），而 Python 里这种类型其实就是一个行为很像序列的元组。

## “优雅是简约之父” ## 

很久以前，*extra 这种语法就在函数里用来把多个元素赋值给一个参数了。（我有本出版于 1996 年的讲 Python 1.4 的书，里面就提到了这个用法。）Python 1.6 或更新的版本里，这个语法在函数调用中用来把一个可迭代对象拆包成不同的参数，这算是跟上面说的那种用法互补。这一设计直观而优雅，并且取代了 Python 里的 apply 函数。如今到了 Python 3，*extra 这个写法又可以用在赋值表达式的左侧，从而在平行赋值里接收多余的元素。这一点让这个本来就很实用的语法锦上添花。

像这样的改进一个接着一个，让 Python 变得越来越灵活，越来越统一，也越来越简单。“优雅是简约之父”（“Elegance begets simplicity”）是 2009 年在芝加哥的 PyCon 的口号，印在 PyCon 的 T 恤上，同样印在 T 恤上的还有 Bruce Eckel 画的《易经》第二十二卦，即贲卦的卦象。贲代表着典雅高贵。这也是我最喜欢的一件 PyCon 的 T 恤。

## 混合类型列表 ##

Python 入门教材往往会强调列表是可以同时容纳不同类型的元素的，但是实际上这样做并没有什么特别的好处。我们之所以用列表来存放东西，是期待在稍后使用它的时候，其中的元素有一些通用的特性（比如，列表里存的是一类可以“呱呱”叫的动物，那么所有的元素都应该会发出这种叫声，即便其中一部分元素类型并不是鸭子）。在 Python 3 中，如果列表里的东西不能比较大小，那么我们就不能对列表进行排序：

>>> l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
>>> sorted(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() < int()

元组则恰恰相反，它经常用来存放不同类型的的元素。这也符合它的本质，元组就是用作存放彼此之间没有关系的数据的记录。

## key 参数很妙 ##
list.sort、sorted、max 和 min 函数的 key 参数是一个很棒的设计。其他语言里的排序函数需要用户提供一个接收两个参数的比较函数作为参数，像是 Python 2 里的 cmp(a, b)。用 key 参数能把事情变得简单且高效。说它更简单，是因为只需要提供一个单参数函数来提取或者计算一个值作为比较大小的标准即可，而 Python 2 的这种设计则需要用户写一个返回值是—1、0 或者 1 的双参数函数。说它更高效，是因为在每个元素上，key 函数只会被调用一次。而双参数比较函数则在每一次两两比较的时候都会被调用。诚然，在排序的时候，Python 总会比较两个键（key），但是那一阶段的计算会发生在 C 语言那一层，这样会比调用用户自定义的 Python 比较函数更快。

另外，key 参数也能让你对一个混有数字字符和数值的列表进行排序。你只需要决定到底是把字符看作数值，还是把数值看作字符：

>>> l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
>>> sorted(l, key=int)
[0, '1', 5, 6, '9', 14, 19, '23', 28, '28']
>>> sorted(l, key=str)
[0, '1', 14, 19, '23', 28, '28', 5, 6, '9']

"""


if __name__ == '__main__':
    # tuple_test_1()
    # tuple_test_2()
    # tuple_test_3()
    tuple_test_4()

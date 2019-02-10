# coding:utf-8
"""
@file: 5.1+2+3.py
@time: 2/10/2019 5:44 PM
@contact: dabuwang
@content:
5.1 all func are objects (所有函数 都是一等对象)
5.2 higher-order function: map, reduce, filter (other: any, all, zip etc.)
5.3 lambda expression
"""


# region 5.1 all funcs are objects
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


def test51():
    print factorial(5)
    print factorial.__doc__
    print type(factorial)

    fact = factorial
    print fact(5)

    print list(map(factorial, range(5)))
# endregion

#region 5.2 higer-order functions
"""
接受函数为参数，或者把函数作为结果返回的函数是高阶函数
"""
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
def test52():
    print "before sorted:",fruits
    print sorted(fruits, key=len)
    print "after sorted:",fruits

    # map's replacement
    print "map:",               list(map(factorial, range(6)))
    print "list derivation:",   [factorial(x) for x in range(6)]
    # filter's replacement
    print "filter:", list(map(factorial, filter(lambda n: n % 2, range(6))))
    print "list derivation with condition:",    [factorial(n) for n in range(6) if n % 2]

    # reduce
    print "reduce:", reduce(lambda x, y: x + y, range(6))
    print "sum:", sum(range(6))
#endregion

#region 5.3 lambda
"""
#Lundh 提出的 lambda 表达式重构秘笈#

如果使用 lambda 表达式导致一段代码难以理解，Fredrik Lundh 建议像下面这样重构。
(1) 编写注释，说明 lambda 表达式的作用。
(2) 研究一会儿注释，并找出一个名称来概括注释。
(3) 把 lambda 表达式转换成 def 语句，使用那个名称来定义函数。
(4) 删除注释。
这几步摘自“Functional Programming HOWTO”(https://docs.python.org/2.7/howto/functional.html)，这是一篇必读文章。
"""

def test53():
    print "lambda in sort:", sorted(fruits, key=lambda word: word[::-1])

#endregion

if __name__ == '__main__':
    # test51()
    # test52()
    test53()
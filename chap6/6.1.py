# coding:utf-8
"""
@file: 6.1.py
@time: 2/12/2019 9:36 PM
@contact: dabuwang
@content:
6.1 案例分析：重构“策略”模式
"""

from abc import abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            # discount = self.promotion.discount(self)  # 6.1.1
            discount = self.promotion(self) #  6.1.2
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# region 6.1.1 经典实现 策略模式
class Promotion():  # 策略：抽象基类

    @abstractmethod
    def discount(self, order):
        """返回折扣金额（正值）"""


class FidelityPromo(Promotion):  # 第一个具体策略
    """为积分为1000或以上的顾客提供5%折扣"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # 第二个具体策略
    """单个商品为20个或以上时提供10%折扣"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # 第三个具体策略
    """订单中的不同商品达到10个或以上时提供7%折扣"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
# endregion

# region 6.1.2 函数实现 策略模式
def fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0
# endregion

# region 6.1.3 选择最佳策略：简单的方式

promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)

# endregion

# region 6.1.4 找出模块中的全部策略
## option 1：
promos = [globals()[name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo']
def best_promo(order):
    """选择可用的最佳折扣
    """
    return max(promo(order) for promo in promos)

## option 2： 单独写个模块 promotions， 使用chap5 中内省的概念： 强调模块内省的一种用途
import inspect
promos = [func for name, func in
                inspect.getmembers(promotions, inspect.isfunction)]

def best_promo(order):
    """选择可用的最佳折扣
    """
    return max(promo(order) for promo in promos)
# endregion


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]
banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
def test611():
    Order(joe, cart, FidelityPromo())
    Order(ann, cart, FidelityPromo())

    Order(joe, banana_cart, BulkItemPromo())

    Order(joe, long_order, LargeOrderPromo())
    Order(joe, cart, LargeOrderPromo())

def test612():
    Order(joe, cart, fidelity_promo)
    Order(ann, cart, fidelity_promo)

    Order(joe, banana_cart, bulk_item_promo)

    Order(joe, long_order, large_order_promo)
    Order(joe, cart, large_order_promo)

def test613():
    Order(joe, long_order, best_promo)
    Order(joe, banana_cart, best_promo)
    Order(ann, cart, best_promo)
if __name__ == '__main__':
    test611()

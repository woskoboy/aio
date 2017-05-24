PROMOTIONS = []


class ItemCart:
    """ элемент товара в корзине """
    def __init__(self, product, count, price):
        self.product = product
        self.count = count
        self.price = price

    def total(self):
       return self.price * self.count


class Order:
    """ Заказ """
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        """ просуммировать элементы корзины """
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        """ оплата за вычитом скидки """
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __str__(self):
        return '<Order total: {:.2f} due: {:.2f}'.format(self.total(), self.due())


def promotion(promo_func):
    PROMOTIONS.append(promo_func)
    return promo_func


@promotion
def bonus_promo(order):
    """ от 1000 бонусов - размер скидки 5%"""
    return order.total() * .05 if order.customer.bonus >= 1000 else 0


@promotion
def big_cart_promo(order):
    """ от 10 единиц одного продукта - скидка 20% на такой товар"""
    discount = 0
    for item in order.cart:
        if item.count >= 10:
            discount += item.total() * .1
    return discount


@promotion
def different_items_promo(order):
    """ различных товаров больше 10 - скидка 7%"""
    uniq_products = {item.product for item in order.cart}
    return order.total() * .07 if len(uniq_products) >= 10 else 0



from collections import namedtuple
from shop.func_op import ItemCart, Order, PROMOTIONS
# ,Customer, best_promo  # big_cart_promo, bonus_promo, different_items_promo
# import inspect
# from shop import func_op


def best_promo(order):
    """ возвращает максимальный размер скидки """
    # promos = [func for name, func in inspect.getmembers(func_op, inspect.isfunction)]
    promos = [func for func in PROMOTIONS]
    return max(promo(order) for promo in promos)

Customer = namedtuple('Customer', 'name bonus')
joe = Customer(name='Joe', bonus=1000)
ann = Customer(name='Ann', bonus=0)

cart = [
    ItemCart('banana', 4, 1.5),
    ItemCart('apple', 3, 2.5),
    ItemCart('cherry', 1, 5.5),
]

print(Order(joe, cart, best_promo))
print(Order(ann, cart, best_promo))

cart = [
    ItemCart('banana', 4, 1.5),
    ItemCart('apple', 11, 2.5),
    ItemCart('cherry', 1, 5.5),
]

print(Order(ann, cart, best_promo))

cart = [ItemCart(str(i), 1, .5) for i in range(1, 12)]

print(Order(joe, cart, best_promo))

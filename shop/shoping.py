from shop.myshop import Customer, ItemCart, Order, BigCartPromo, BonusPromo, DifferentItemsPromo

joe = Customer(name='Joe', bonus=1000)
ann = Customer(name='Ann', bonus=0)

cart = [
    ItemCart('banana', 4, 1.5),
    ItemCart('apple', 11, 2.5),
    ItemCart('cherry', 1, 5.5),
]

print(Order(joe, cart, BonusPromo()))
print(Order(ann, cart, BonusPromo()))

cart = [
    ItemCart('banana', 4, 1.5),
    ItemCart('apple', 11, 2.5),
    ItemCart('cherry', 1, 5.5),
]

print(Order(ann, cart, BigCartPromo()))

cart = [ItemCart(str(i), 1, .5) for i in range(1, 12)]

print(Order(joe, cart, DifferentItemsPromo()))


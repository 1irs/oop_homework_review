from dataclasses import dataclass


@dataclass
class Product:
    """1. Название."""
    name: str

    """2. Цена за единицу."""
    price_per_one: float

    """3. Количество этих продуктов в корзине."""
    qnty_in_cart: float

    """"1. Подсчет суммы."""
    def amount(self) -> float:
        return self.qnty_in_cart * self.price_per_one

    """Печать информации о Продукте на экран в произвольной форме."""
    def print_prod(self):
        return print(f"Product name: {self.name}, price per one: {self.price_per_one}, quantity in cart: {self.qnty_in_cart}")

@dataclass
class Cart:
    """ Класс Cart с тремя полями:
    inside: лист объектов Product
    total_amount_no_discount: сумма всех товаров в корзине без скидки
    total_with_discount: сумма всех товаров со всеми возможными скидками

    К сожалению я так и не понял как сделать что бы по умолчанию лист был пустым
    """
    inside: list[Product]
    total_amount_no_discount: float = 0.0
    total_with_discount: float = 0.0
    # inside = []

    """Добавление Продукта в Корзину.
    Если лист пустой, я просто добавляю Продукт
    Если лист не пустой, я проверяю есть ли в корзине товар с таким именем и такой ценой,
    и, если такой товар есть, я просто добавляю к существующему количеству новое
    
    Таким образом у меня каждый объект в листе - это уникальная позиция"""

    def add_prod(self, x: Product):
        if self.inside == []:
            self.inside.append(x)
        else:
            for p in self.inside:
                if x.name == p.name and x.price_per_one == p.price_per_one:
                    p.qnty_in_cart += x.qnty_in_cart
                    return
            self.inside.append(x)
        self.total() # обновляю поля класса с суммами

    """Очистка корзины."""
    def clear_cart(self):
        self.inside.clear()
        self.total()  # обновляю поля класса с суммами
        # так наверное было бы быстрее:
        # self.total_amount_no_discount = 0
        # self.total_with_discount = 0

    """Подсчет количества разных продуктов в Корзине."""
    def different_prod_qnty(self):
        return len(self.inside)

    """4. Вычисление стоимости товаров в корзине. 
    4.1. Если товаров больше 10, то применяется скидка 3%.
    4.2. Если стоимость товаров больше 100 у. е., то дается дополнительная скидка в 5 у. е. 
    
    При вызове метода скидки начисляются последовательно, суммы округляются до 2х знаков и обновляются поля класса"""
    def total(self):
        amount: float = 0.0
        for p in self.inside:
            amount += round((p.amount()), 2) # используем метод .amount() класса Product 

        self.total_amount_no_discount = amount
        if self.different_prod_qnty() > 10:
            amount *= 0.97
            amount = round(amount, 2)
        if amount > 100:
            amount -= 5
        self.total_with_discount = amount
        # return

    """5. Метод, который выводит содержимое корзины, а также стоимость корзины до скидок и после скидок."""
    def print_cart(self):
        print("Products in the cart:")
        for p in self.inside:
            p.print_prod()  # используем метод .print_prod() класса Product 
        # self.total()
        print(f"Total without discount: {self.total_amount_no_discount}")
        print(f"Total with discount: {self.total_with_discount}")

    """ Метод, который найдет самый дорогой Продукт в корзине (вывести название)."""
    def expensive_prod(self):
        price: float = 0.0
        # сначала ищем самую высокую цену
        for p in range(len(self.inside)):
            if price <= self.inside[p].price_per_one:
                price = self.inside[p].price_per_one

        # проверяем есть ли еще в корзине Продукты с такой ценой, самый дорогой Продукт может быть не один
        # и выводим название на экран
        print("Expensive products in the cart: ")
        for pp in self.inside:
            if pp.price_per_one == price:
                print(pp.name)



# создаю несколько объектов, некоторые с одинаковыми именами и ценами, что бы проверить метод добавления в корзину 
p1 = Product("gggg", 5, 10)
p2 = Product("XXXXXXX", 2, 20)
p3 = Product("gggg", 5, 990)
p4 = Product("XXXXXXX", 2, 100)
p5 = Product("XXXXXXX", 500, 20)

# Создаю экземпляр класса Cart, Т.к. я не понял как сделать по умолчанию лист пустым, я передаю пустой агрумент []
cart1 = Cart([])
cart1.add_prod(p1)
print(cart1.inside)
cart1.add_prod(p2)
print(cart1.inside)
cart1.add_prod(p3)
print(cart1.inside)
cart1.add_prod(p4)
print(cart1.inside)
cart1.add_prod(p5)
print(cart1.inside)
print(cart1.different_prod_qnty()) # Добавление работает корректно


cart1.print_cart()

# добавляю в корзину еще 8 Продуктов, чтобы проверить как работает скидка
cart1.add_prod(Product("qweqwe", 1, 1.25))
cart1.add_prod(Product("wewe", 2, 2.55))
cart1.add_prod(Product("trrty", 3.2, 2.77))
cart1.add_prod(Product("5454", 500, 999))
cart1.add_prod(Product("fgsdfg", 1, 1))
cart1.add_prod(Product("qwerwer", 88, 0.1))
cart1.add_prod(Product("fdgsdh", 0.1, 0.01))
cart1.add_prod(Product("fdfasdfgsdh", 0.1, 0.01))

cart1.print_cart()

cart1.expensive_prod()
cart1.clear_cart()
cart1.print_cart()
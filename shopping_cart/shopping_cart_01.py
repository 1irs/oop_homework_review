from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: float

    def get_sum(self) -> float:
        return round(self.price * self.quantity, 2)

    def show_prod(self) -> None:
        print(
            f'Продукт {self.name} с ценой {self.price} в количестве {self.quantity}  общей стоимостью {Product.get_sum(self)}')


@dataclass
class Corzina:
    discount_qnt: float
    discount_sum: float
    products: list[Product]

    def add_item(self, item: Product) -> None:  # добавление продукта в корзину
        self.products.append(item)

    def clear_corzina(self) -> []:  # очистка корзины
        self.products.clear()

    def get_total_quantity(self) -> float: #Подсчет количества разных продуктов
        return len(self.products)
        #total_quantity: float = 0
        #for el in self.products:
        #    total_quantity += el.quantity
        #return total_quantity

    def get_sum(self) -> float: #Вычисление стоимости товаров в корзине.
        summa: float = 0
        for el in self.products:
            summa += el.get_sum()
        return round(summa, 2)

    def get_sum_after_discount(self) -> float:  # Вычисление стоимости товаров после скидки
        sum_after_discount: float=self.get_sum()
        if self.get_total_quantity() > 10:
            sum_after_discount -= self.get_sum() * self.discount_qnt
        if self.get_sum() > 100:
            sum_after_discount -= self.discount_sum
        return round(sum_after_discount, 2)

    def print(self) -> None:
        print('Товар    Цена  Количество  Общая стоимость')
        for el in self.products:
            print(f'{el.name}       {el.price}      { el.quantity}      {el.get_sum()}')
        print('________________________________________________')
        print('Общая сумма корзины до скидок:', self.get_sum())
        print('Общая сумма корзины после скидок:', self.get_sum_after_discount())
        print('________________________________________________')

    def max_price(self) -> str:
        max_price: float = 0.0
        name_max_price: str = ' '
        for el in self.products:
            if el.price > max_price:
                max_price = el.price
                name_max_price = el.name
        return name_max_price


item1 = Product(name='арбуз', price=5.00, quantity=3.20)
item2 = Product('дыня', 7.00, 4.20)
item3 = Product('груша', 2.00, 5.0)
item4 = Product('киви', 30.00, 2.0)
item5 = Product('яблоко', 2.00, 15.0)

product_list: list[Product] = [item1, item2, item3]

c = Corzina(
    discount_qnt=0.03,
    discount_sum=5.0,
    products=product_list
)

c.clear_corzina()
c.add_item(item5)
c.add_item(item4)
c.add_item(item3)
c.add_item(item2)
c.add_item(item1)
c.print()
c.max_price()
print(type(item1))

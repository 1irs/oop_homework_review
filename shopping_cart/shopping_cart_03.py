from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:

    product_name: str # имя продукта
    product_price: float # стоимость единицы продукта
    product_quantity: int # кол-во продуктов

    # метод подсчета суммы по позиции продукта
    def get_summ(self) -> float:
        return self.product_price * self.product_quantity

    def print_info(self):
        print(f'Название продукта: {self.product_name}\nСтоимость: {self.product_price}\nКоличество: {self.product_quantity}\nОбщая стоимость: {self.get_summ()}\n')


@dataclass
class Cart:

    product_items: List[Product] = field(default_factory=list) # массив продуктов в корзине
    cost_WO_discounts: float = 0.0 # стоимость продуктов БЕЗ скидок
    cost_with_discounts: float = 0.0 # стоимость продуктов со скидками

    # метод добавления продукта в корзину
    def add_product(self, Product):
        self.product_items.append(Product)
        self.get_total()

    # метод очистки корзины
    def clean_cort(self):
        self.product_items = []
        self.cost_WO_discounts: float = 0.0
        self.cost_with_discounts: float = 0.0

    # метод подсчета количества разных продуктов в Корзине
    def number_of_unique(self) -> int:
        unique_products: list[str] = []
        for product in self.product_items:
            unique_products.append(product.product_name)
        return len(set(unique_products))

    # метод вычисления стоимости товаров в корзине
    def get_total(self) -> tuple[float, float]:
        if len(self.product_items) == 0:
            print('Ваша корзина пуста')
            return self.cost_WO_discounts, self.cost_with_discounts
        elif len(self.product_items) <= 10:
            for product in self.product_items:
                self.cost_WO_discounts += product.get_summ()
            if self.cost_WO_discounts > 100:
                self.cost_with_discounts = self.cost_WO_discounts - 5
            return self.cost_WO_discounts, self.cost_with_discounts
        else:
            for product in self.product_items:
                self.cost_WO_discounts += product.get_summ()
            if self.cost_WO_discounts > 100:
                self.cost_with_discounts = self.cost_WO_discounts - 5
            self.cost_with_discounts = self.cost_WO_discounts - self.cost_WO_discounts * 0.03
            return self.cost_WO_discounts, self.cost_with_discounts

    # Метод, который выводит содержимое корзины, а также стоимость корзины до скидок и после скидок
    def print_cort(self):
        if len(self.product_items) == 0:
            print('Ваша корзина пуста')
        else:
            for product in self.product_items:
                product.print_info()
            print(f'Стоимость корзины: {self.cost_WO_discounts}\nСтоимость корзины с учетом скидок: {self.cost_with_discounts}')

    # Метод, который найдет самый дорогой продукт в корзине (выводит в консоль название)
    def print_most_expensive(self):
        prices: list = []
        most_expensive: list = []
        for product in self.product_items:
            prices.append(product.product_price)
        for product in self.product_items:
            if product.product_price == max(prices):
                most_expensive.append(product.product_name)
        if len(most_expensive) == 0:
            print('Ваша корзина пуста')
        elif len(most_expensive) > 1:
            print('Самые дорогие товары в корзине: ' + ", ".join(most_expensive))
        else:
            print(f'Самый дорогой товар в корзине: ' + ", ".join(most_expensive))

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    unit_price: float
    quantity: float

    """Подсчет суммы"""

    def total(self) -> float:
        return self.unit_price * self.quantity

    """Печать информации о Продукте на экран"""

    def product_info(self) -> None:
        print(f"Имя товара={self.name}\n"
              f"Количество={self.quantity}"
              f"Цена товара={self.unit_price}"
              )


@dataclass()
class ShoppingCart:
    cart = {}

    """Добавление в корзину"""

    def add_to_shopping_cart(self, product: Product) -> None:
        self.cart[product.name] = product.total()

    """Очистка корзины"""

    def clear_shopping_cart(self) -> None:
        self.cart.clear()

    """Подсчет количества разных товаров в корзине"""

    def items_in_the_cart(self) -> int:
        return len(self.cart)

    """Вычисление стоимости товаров в корзине"""

    def total_shopping_cart_wo_discount(self) -> float:
        return sum(self.cart.values())

    """Если товаров больше 10, то применяется скидка 3%"""

    def total_shopping_cart_w_discount(self) -> float:
        final_price = self.total_shopping_cart_wo_discount()
        if self.items_in_the_cart() > 10:
            final_price *= 0.97
        if self.total_shopping_cart_wo_discount() > 100.0:
            final_price -= 5.0
        return final_price

    def discount_3(self) -> float:
        counter = 0
        for Product.name in self.cart.items():
            counter += 1
            if counter > 10:
                discount = sum(self.cart.values()) - sum(self.cart.values()) * 0.03
                return discount

    """ Если стоимость товаров больше 100 у. е., то дается дополнительная скидка в 5 у. е"""

    def discount_5(self) -> float:
        if sum(self.cart.values()) > 100:
            discount = sum(self.cart.values()) - 5
            return discount

    """Метод, который выводит содержимое корзины, а также стоимость корзины до скидок и после скидок"""

    def info_total_shopping_cart(self) -> None:
        print(self.cart)
        print(self.total_shopping_cart_wo_discount())
        print(self.discount_3())
        print(self.discount_5())

    """Самый дорогой Продукт в корзине"""

    def the_most_expensive_product(self) -> None:
        max_product = max(self.cart, key=self.cart.get)
        print(max_product)
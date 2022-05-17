# Как это сделать так и не удалось понять:
# 1. Добавление Продукта в Корзину.
# 2. Очистка корзины.

# Тут не получилось победить тайпэррор  =(
# 6. Метод, который найдет самый дорогой Продукт в корзине (вывести название)



from dataclasses import dataclass



@dataclass
class ProductItem:
    product_name: str
    price_for_one: float
    product_qty: float

    def get_amount(self) -> float:  # цена за кол-во в одной строке
        return self.product_qty * self.price_for_one

    def print_info_product(self):
        print("Наименование     Цена за шт      Кол-во")
        print(self.product_name, self.price_for_one, self.product_qty, sep="             ")


@dataclass
class ShoppingCart:
    #    sale: float  # скидка
    product_items: list[ProductItem]  # список позиций в корзине

    def product_subtotal(self) -> float:  # подсчёт цены за все позиции без скидки
        subtotal: float = 0.0
        for item in self.product_items:
            subtotal += item.get_amount()
        return subtotal

    # def product_max_amount(self) -> float:  # ищем самую дорогую позицию в корзине
    #     max_amount = self.product_items[0]
    #     for index in self.product_items:
    #         if index < max_amount:
    #             max_amount == index
    #     return max_amount


    def qty_sub(self) -> float:  # подсчёт кол-во товара в корзине
        qty: float = 0.0
        for item in self.product_items:
            qty += item.product_qty
        return qty

    def qty_sale(self) -> float:  # скидка за кол-во товара в корзине
        sale_qty = 0.0
        if self.qty_sub() > 10:
            sale_qty = 3.0  # это в процентах
        return sale_qty

    def product_subtotal_sale(self) -> float:  # скидка за общую стоимость
        sale_subtotal_product = 0.0
        if self.product_subtotal() > 100:
            sale_subtotal_product = 5.0  # это в у.е.
        return sale_subtotal_product

    def get_sale(self) -> float:  # подсчёт цены за все позиции + все скидки
        return self.product_subtotal() - (self.product_subtotal() * self.qty_sale() / 100) \
               - self.product_subtotal_sale()

    def print_info_cart(self):
        print("Наименование     Цена за шт      Кол-во      Сумма")
        for item in self.product_items:
            print(item.product_name, item.price_for_one, item.product_qty, item.get_amount(),
                  sep="           ")
        print('---------------------------')

        print('Сумма без скидки:', self.product_subtotal())
        print("кол-во позиций всего: ", self.qty_sub())
        # print("Самая дорогая позиция: ", self.product_max_amount())
        print("Процент скидки: ", self.qty_sale())
        print("Доп.скидка в у.е: ", self.product_subtotal_sale())
        print('Сумма со скидкой:', self.get_sale())


apple = ProductItem(product_name="apple", price_for_one=13.5, product_qty=4.0)
banana = ProductItem(product_name="banana", price_for_one=25.0, product_qty=1.5)
meet = ProductItem(product_name="meet", price_for_one=100.0, product_qty=8.4)
juice = ProductItem(product_name="juice", price_for_one=17.3, product_qty=5.0)

products_item: list[ProductItem] = [apple, banana, meet, juice]

poz1 = ShoppingCart(products_item)
poz1.print_info_cart()

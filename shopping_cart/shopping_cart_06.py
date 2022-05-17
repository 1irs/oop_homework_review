from dataclasses import dataclass

@dataclass
class Product:
    name:str
    price_of_unit: float
    kol_prod_korz: float

    def get_sum_prod(self) -> float:
        sum_produ = self.price_of_unit * self.kol_prod_korz
        return sum_produ
       

    def print_info_prod(self):
        print (f"Наименование: {self.name}, цена за единицу: {self.price_of_unit} y.e. , количество продукта: {self.kol_prod_korz}, полная стоимость продукта: {self.get_sum_prod()} y.e. ")



@dataclass
class Korzina:
    products: list[Product]

    def prod_to_korz(self,dobavl: Product):
        self.products.append(dobavl)
        print(f"Добавленный товар: {dobavl.name}, стоимостью {dobavl.price_of_unit} y.e. в количестве {dobavl.kol_prod_korz} шт")

    def clear_korz(self):
        self.products.clear()

    def razlich_prod_korz(self) -> dict:
        d = {}
        for product in self.products:
            if product.name in d:
                d[product.name] += 1
            else:
                d[product.name] = 1
        print(f"Количество различных товаров {d}")
        return d

    def all_sum_korz(self) -> float:
        all_sum : float = 0.0
        for product in self.products:
            all_sum += product.get_sum_prod()
        print(f"Полная стоимость корзины: {all_sum} y.e.")
        return all_sum


    def skidka_prod(self) -> float:
        skidka: float = 0.0
        all_price_prod = self.all_sum_korz()
        kolvo_prod = len(self.products)
        if kolvo_prod > 10:
            skidka = all_price_prod * 0.03
        if all_price_prod > 100:
            skidka = skidka + 5
        print (f"Скидка составила {skidka} y.e.")
        return skidka



    def info_korzina(self):
        do_skid_korz = self.all_sum_korz()
        posle_skid_korz = do_skid_korz - self.skidka_prod()
        print(f"Содержимое корзины:")
        for prod in self.products:
            prod.print_info_prod()
        print(f"Стоимость корзины до скидок: {do_skid_korz} y.e. , стоимость корзины после скидок {posle_skid_korz} y.e.")

      

    def most_exp_product(self):
        max_product: Product = self.products[0]
        for p in self.products:
            if p.price_of_unit > max_product.price_of_unit:
                max_product = p
        print(f"Самый дорогой продукт: {max_product.name}")

 
product1 = Product('Сахар', 50, 2)
product2 = Product('Сахар', 50, 3)
product3 = Product('Соль', 70, 1)


product1.print_info_prod()
product2.print_info_prod()
product3.print_info_prod()

korzina1 = Korzina([product1, product2, product3, product1, product2, product3, product1, product2, product3, product1, product2, product3])
korzina1.prod_to_korz(product3)
len(korzina1.razlich_prod_korz())
korzina1.all_sum_korz()


korzina1.skidka_prod()

korzina1.info_korzina()

korzina1.most_exp_product()

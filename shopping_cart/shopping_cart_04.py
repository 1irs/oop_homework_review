class Product:
    def __init__(self, name: str, price: float, count: int) -> None:
        self.name = name
        self.price = price
        self.count = count

    def sum(self) -> float:
        return self.price * float(self.count)

    def info(self) -> str:
        return f"{self.name}\t\t\t\t\t{self.price} \t{self.count} \t\t== {self.sum()}"


class Chart:
    def __init__(self) -> None:
        self.cart: list[Product] = []
        self.total_amount_without_discount: float = 0.0
        self.total_amount_with_discount: float = 0.0
        self.unique: int = 0

    def add(self, product: Product) -> None:
        self.cart.append(product)

    def calculate_different(self) -> None:
        temp: list[str] = [item.name for item in self.cart]
        self.unique = len(set(temp))

    def calculate_chart_sum(self) -> [float, float]:
        for item in self.cart:
            self.total_amount_without_discount += item.sum()
        self.total_amount_with_discount = self.total_amount_without_discount

        self.calculate_different()
        if self.unique > 10:
            self.total_amount_with_discount = self.total_amount_with_discount * 0.97

        if self.total_amount_without_discount > 100.00:
            self.total_amount_with_discount = self.total_amount_with_discount - 5.00

        return self.total_amount_without_discount, self.total_amount_with_discount

    def info(self) -> None:
        print("Product\t\t\t\t\tPrice \tCount \tSum")
        for item in self.cart:
            print(f"{item.info()}")
        self.calculate_chart_sum()
        print(f"----------------------------------------------------\n"
              f"Total amount without discount \t {self.total_amount_without_discount}\n"
              f"Total amount with discount \t {self.total_amount_with_discount}\n")

    def most_expensive(self) -> None:
        prices = [item.price for item in self.cart]
        print(f"The most expensive product is  {max(prices)}")


if __name__ == '__main__':

    chase: list[Product] = [
        Product(name="Book", price=100.00, count=1),
        Product(name="Shirt", price=100.00, count=4),
        Product(name="Coat", price=200.00, count=1),
        Product(name="Shoes", price=200.00, count=1),
        Product(name="Shoes", price=100.00, count=2),
        Product(name="Shoes", price=300.00, count=2),
        Product(name="Pants", price=100.00, count=1),
        Product(name="Book", price=100.00, count=1),
        Product(name="Hoodie", price=500.00, count=4),
        Product(name="Sweater", price=100.00, count=1),
        Product(name="Shirt", price=100.00, count=4),
        Product(name="Coat", price=200.00, count=1),
        Product(name="Turtle", price=200.00, count=1),
        Product(name="Shoes", price=100.00, count=2),
        Product(name="Shoes", price=300.00, count=2),
        Product(name="Crew", price=100.00, count=1),
        Product(name="Jacket", price=100.00, count=1),
        Product(name="Jersey", price=200.00, count=4)
    ]

    chart = Chart()
    for item in chase:
        chart.add(item)
    chart.info()
    chart.most_expensive()





class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class DiscountStrategy:
    def calculate_discount(self, items):
        pass


class NoDiscount(DiscountStrategy):
    def calculate_discount(self, items):
        return 0


class TenPercentDiscount(DiscountStrategy):
    def calculate_discount(self, items):
        total_price = sum(item.price for item in items)
        if total_price > 100:
            return total_price * 0.1
        else:
            return 0


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def calculate_discount(self, items):
        return self.discount_amount


class ShoppingCart:
    def __init__(self, discount_strategy):
        self.items = []
        self.discount_strategy = discount_strategy

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_discount(self):
        return self.discount_strategy.calculate_discount(self.items)

    def calculate_total_price(self):
        return sum(item.price for item in self.items)

    def checkout(self):
        total_price = self.calculate_total_price()
        discount = self.calculate_discount()
        final_price = total_price - discount
        print(f"Total price: {total_price}")
        print(f"Discount applied: {discount}")
        print(f"Final price after discount: {final_price}")


if __name__ == "__main__":
    cart = ShoppingCart(FixedAmountDiscount(20))

    item1 = Item("Item 1", 50)
    item2 = Item("Item 2", 75)
    cart.add_item(item1)
    cart.add_item(item2)

    cart.checkout()
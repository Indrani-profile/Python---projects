from decimal import Decimal

class Invoice:
    def __init__(self, part_number, part_description, quantity, price_per_item):
        self._part_number = part_number
        self._part_description = part_description
        self.quantity = quantity  # Validate non-negative quantity
        self.price_per_item = price_per_item  # Validate non-negative price

    @property
    def part_number(self):
        return self._part_number

    @property
    def part_description(self):
        return self._part_description

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be non-negative")

    @property
    def price_per_item(self):
        return self._price_per_item

    @price_per_item.setter
    def price_per_item(self, price_per_item):
        if price_per_item >= 0:
            self._price_per_item = Decimal(price_per_item)
        else:
            raise ValueError("Price per item must be non-negative")

    def calculate_invoice(self):
        return self.quantity * self.price_per_item


item = Invoice("12345", "Widget", 5, 10.99)

print(f"Part Number: {item.part_number}")
print(f"Part Description: {item.part_description}")
print(f"Quantity: {item.quantity}")
print(f"Price Per Item: ${item.price_per_item:.2f}")
print(f"Invoice Amount: ${item.calculate_invoice():.2f}")
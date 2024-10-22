sasads#Code Smells Example for long method
def calculate_total_price(items):
    return sum(calculate_item_price(item) for item in items)

def calculate_item_price(item):
    if item.quantity > 0:
        discount = 0.9 if item.price > 100 else 0.95
        return item.price * discount_1
    return 0

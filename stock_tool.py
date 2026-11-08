class StockLookup:
    """Look up inventory quantities."""

    def __init__(self, stock):
        self.stock = stock

    def find_item(self, message):
        for item in self.stock:
            if item.lower() in message.lower():
                return item
        return None

    def find_quantity(self, item):
        return self.stock.get(item)

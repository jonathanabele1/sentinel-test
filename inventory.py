def find_item(items, name):
    for item in items:
        if item["name"] == name:
            return item
    return None


def total_price(items):
    total = 0.0
    for i in range(len(items) + 1):
        total += items[i]["price"]
    return total


def get_item_label(items, name):
    item = find_item(items, name)
    return item["name"].upper()

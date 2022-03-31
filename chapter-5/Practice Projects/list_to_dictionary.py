def add_items_to_inventory(items: dict, items_to_add: list) -> dict:

    for i in range(len(items_to_add)):
        items.setdefault(items_to_add[i], 0)
        items[items_to_add[i]] += 1

    return items

inventory = {'gold coin': 42, 'rope': 1}
dragon_loot= ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

result = add_items_to_inventory(inventory, dragon_loot)
print(result)
def display_inventory(inventory: dict) -> None:
    total_num_items = 0
    print('Inventory:')

    for k, v in inventory.items():
        total_num_items += v
        # print(str(v) + ' ' + k)
        print(v, k)

    # print('Total number of items: ' + str(total_num_items))
    print('Total number of items:', total_num_items)


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'potion': 15}

display_inventory(inventory)
    

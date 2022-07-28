lst = input().split()
items = {}
for i in range(0, len(lst), 2):

    material = lst[i + 1].lower()
    value = int(lst[i])

    if material not in items:
        items[material] = 0
    items[material] += value

    if items['shards'] >= 250:
        items['shards'] -= 250
        dict_filtered = dict(sorted(items.items(), key=lambda kv: (-kv[1], kv[0])))
        print(f"Shadowmourne obtained!")
    elif items['fragments'] >= 250:
        items['fragments'] -= 250
        print(f"Valanyr obtained!")
    elif items['motes'] >= 250:
        items['motes'] -= 250
        print(f"Dragonwrath obtained!")





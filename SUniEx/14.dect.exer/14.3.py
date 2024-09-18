countries = input().split(', ')
capitals = input().split(', ')

for k, v in zip(countries, capitals):
    print(f"{k} -> {v}")

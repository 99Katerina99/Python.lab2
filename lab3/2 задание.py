dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys_set = set(dct.keys())
values_set = set(dct.values())

combined_set = set(dct.keys())
combined_set.update(values_set)
# update([other]) рассматривается в источниках по ссылке Структура данных: словарь (dict)

print("Множество ключей:", keys_set)
print("Множество значений:", values_set)
print("Объединение множеств:",combined_set)
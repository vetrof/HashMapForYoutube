dictionary = {'a': "masha", "b": "misha", "c": "vasya"}


# Узнаем хеш-значение ключей
for key in dictionary:
    print(f"Key: {key}, Hash: {hash(key)}")

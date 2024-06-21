dictionary = {'a': "masha", 'b': "misha", 'c': "vasya"}

# Хеш-значения для ключей
hash_a = hash('a')
hash_b = hash('b')
hash_c = hash('c')

# Предположим, размер массива для простоты равен 10
size = 10

# Индексы в массиве
index_a = hash_a % size
index_b = hash_b % size
index_c = hash_c % size

print(f"Index for 'a': {index_a}")
print(f"Index for 'b': {index_b}")
print(f"Index for 'c': {index_c}")

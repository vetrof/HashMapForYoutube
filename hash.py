
def simple_hash(s, table_size=100):
    hash_value = 0
    for char in s:
        hash_value = (hash_value * 31 + ord(char)) % table_size
    return hash_value

# Пример использования
print(simple_hash('sobaka'))  # Пример вывода: 58
print(simple_hash('sobaka', table_size=10))  # Пример вывода: 8

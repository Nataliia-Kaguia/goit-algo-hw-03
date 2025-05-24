import random

def get_numbers_ticket(min_value, max_value, quantity):
    # Перевірка валідності параметрів
    if not (1 <= min_value <= max_value <= 1000) or quantity > (max_value - min_value + 1):
        return []

    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    
    # Повертаємо відсортований список
    return sorted(numbers)

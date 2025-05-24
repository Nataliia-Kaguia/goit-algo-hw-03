from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Перетворюємо рядок на об'єкт дати
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        # Отримуємо поточну дату
        today = datetime.today().date()
        # Розраховуємо різницю (в днях)
        delta = today - input_date
        # Повертаємо кількість днів
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

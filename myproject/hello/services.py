from datetime import datetime

def get_greeting_with_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Hello, world! Колосовська Дар'я Вікторівна ПР-3-2. Час відповіді: {current_time}"

import string
import random
from datetime import datetime, timedelta
import allure


class DataGenHelper:
    def __init__(self):
        pass

    @staticmethod
    @allure.step("Сгенерировать случайную дату")
    def generate_random_date():
        # Текущая дата
        now = datetime.now()

        # Начало периода: через месяц
        start_date = now + timedelta(days=0)

        # Конец периода: например, через 30 дней от текущей даты
        end_date = start_date + timedelta(days=30)

        # Случайное количество дней в диапазоне
        random_days = random.randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days=random_days)

        # Форматируем дату в нужный вид
        chosen_date = random_date.strftime('%d.%m.%Y')

        allure.attach(
            f"Дата: {chosen_date}",
            name="Выбранная дата",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.step(f"Выбрана дата: {chosen_date}")

        return chosen_date

    @staticmethod
    def random_email():
        domains = ["gmail.com", "yandex.ru", "mail.ru", "telekom.ru", "rambler.ru"]
        name_length = random.randint(5, 12)  # длина имени от 5 до 12 символов
        domain = random.choice(domains)
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
        return f"{name}@{domain}"

    @staticmethod
    def random_password():
        password_length = random.randint(6, 10)  # длина имени от 6 до 10 символов
        return ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
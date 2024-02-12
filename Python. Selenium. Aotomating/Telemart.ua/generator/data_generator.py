from data.user_data import UserData
# import random
from random import randint
from faker import Faker


# faker_en = Faker('En')
faker_ru = Faker('Ru')


def generate_user_data():
    return UserData(
        last_name=faker_ru.last_name(),
        first_name=faker_ru.first_name(),
        middle_name=faker_ru.middle_name(),
        phone=randint(100000000, 999999999),
        email=faker_ru.email(),
        password=randint(100000, 999999),
    )

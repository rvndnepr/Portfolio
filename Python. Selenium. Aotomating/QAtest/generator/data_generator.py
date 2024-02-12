from data.user_data import UserData
from data.user_data import PersonData
# import random
from random import randint
from faker import Faker


faker_en = Faker('En')
# faker_ru = Faker('Ru')


def generate_user_data():
    return UserData(
        gen_name=faker_en.first_name() + " " + faker_en.last_name(),
        gen_email=faker_en.email(),
        gen_cur_addr=faker_en.address(),
        gen_perm_addr=faker_en.address(),
    )

# def generate_user_data():
#     return UserData(
#         gen_name=faker_ru.first_name() + " " + faker_ru.last_name(),
#         gen_email=faker_ru.email(),
#         gen_cur_addr=faker_ru.address(),
#         gen_perm_addr=faker_ru.address(),
#     )


def generate_person_data():
    return PersonData(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        age=randint(20, 60),
        e_mail=faker_en.email(),
        salary=randint(500, 3000),
        department=faker_en.job()[:25]
    )

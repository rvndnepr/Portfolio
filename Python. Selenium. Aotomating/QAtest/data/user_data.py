class UserData:

    data_user_name = "User Test"
    data_user_email = "testemail@mailinator.com"
    data_user_cur_address = "Some address"
    data_user_perm_address = "Another address"

    def __init__(self, gen_name, gen_email, gen_cur_addr, gen_perm_addr):
        self.gen_name = gen_name
        self.gen_email = gen_email
        self.gen_cur_addr = gen_cur_addr
        self.gen_perm_addr = gen_perm_addr


class PersonData:
    def __init__(self, first_name, last_name, e_mail, age, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = str(age)
        self.e_mail = e_mail
        self.salary = str(salary)
        self.department = department

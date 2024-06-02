from math import sqrt
import datetime

#Exercize1
def snake_to_camel_and_vice_versa(str_to_convert: str) -> str:
    def split_str_by_upper_char(str_to_split: str) -> list:
        enumerated_chars = zip(range(0, len(str_to_split)), list(str_to_split))
        return list(filter(lambda index_char: index_char[1].isupper(), enumerated_chars))

    if str_to_convert.find('_') != -1:
        words = str_to_convert.split('_')
        new_words = list(map(lambda word: word[0].upper()+word[1:], words))
        return ''.join(new_words)
    else:
        enumerated_upper = split_str_by_upper_char(str_to_convert)
        words = []
        last_ind = 0
        for index, _ in enumerated_upper:
            if last_ind == index:
                continue
            res_word = str_to_convert[last_ind].lower() + str_to_convert[last_ind + 1:index]
            words.append(res_word)
            last_ind = index
        res_word = str_to_convert[last_ind].lower() + str_to_convert[last_ind + 1:]
        if len(str_to_convert) > 0:
            words.append(res_word)
        return '_'.join(words)

#Exersize2
def check_if_date_valid() -> bool:
    date = str(input('Enter date in DD.MM.YYYY format: '))
    day = 0
    month = 0
    year = 0
    try:
        [day, month, year] = date.split('.')
    except ValueError:
        return False
    try:
        datetime.date(int(year), int(month), int(day))
    except ValueError:
        return False
    return True

#Exersize3
def check_if_num_valid(num_to_check : int) -> bool:
    cur_num = 2
    while cur_num <= sqrt(num_to_check):
        if num_to_check % cur_num == 0:
            return True
        cur_num += 1
    return False

#Exersize4
def fill_users() -> None:
    def print_user_info_as_table(users_info: dict) -> None:
        print('|   ID   |   Name   |       Family       | Age |')
        for user_id, user_info in users_info.items():
            name_field_spaces = (10 - len(user_info[0]))*' ' if len(user_info[0]) <= 10 else ''
            name_field = user_info[0] + name_field_spaces
            family_field_spaces = (20 - len(user_info[1]))*' ' if len(user_info[1]) <= 20 else ''
            family_field = user_info[1] + family_field_spaces
            print(f'|{user_id}|{name_field}|{family_field}| {user_info[2]}  |')
    users_by_id = {}
    while True:
        user_name = str(input("Enter name: "))
        if len(user_name) == 0:
            break
        if user_name[0].islower():
            user_name = user_name[0].upper() + user_name[1:]
        user_family = str(input("Enter family: "))
        if len(user_family) == 0:
            break
        if user_family[0].islower():
            user_family = user_family[0].upper() + user_family[1:]
        age = int(input("Enter age (18-60): "))
        if not 18 <= age <= 60:
            break
        user_id = str(input("Enter unique id: "))
        if len(user_id) > 8:
            break
        user_id = user_id.zfill(8)
        if user_id in users_by_id:
            break
        users_by_id[user_id] = (user_name, user_family, age)
    print_user_info_as_table(users_by_id)

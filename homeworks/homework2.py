#Exercize1
def sum_numbers() -> None:
    number = int(input("Enter number: "))
    while not (9 >= number >= -9):
        res = 0
        should_subtract = False
        for num in str(number):
            if num == '-':
                should_subtract = True
                continue
            if should_subtract:
                should_subtract = False
                res -= int(num)
            else:
                res += int(num)
        number = res
    print(number)


#Exercize2
def find_tickets() -> None:
    rows = []
    print("Enter rows from screen")
    try:
        while row := list(map(int, input("Enter row places 1 or 0: ").split(sep=','))):
            rows.append(row)
    except ValueError:
        print("Entering stopped")
    if len(rows) == 0:
        return
    tickets_count = int(input('Enter number of tickets: '))
    for index, row in enumerate(rows):
        cur_len = 0
        for place in row:
            if place == 1:
                cur_len = 0
                continue
            else:
                cur_len += 1
            if cur_len >= tickets_count:
                print(f'Your row number: {index}')
                return
    else:
        print('No such rows')

#Exercize3
def RLE()->None:
    str_to_zip = str(input("Enter string to zip: "))
    if len(str_to_zip) == 0:
        return
    cur_symb = str_to_zip[0]
    cur_symb_counter = 1
    zipped_str = ''
    for symb in str_to_zip[1:]:
        if symb == cur_symb:
            cur_symb_counter += 1
        else:
            zipped_str += f'{cur_symb_counter}{cur_symb}'
            cur_symb_counter = 1
            cur_symb = symb
    zipped_str += f'{cur_symb_counter}{cur_symb}'
    print(zipped_str)

#Exercize4
def CaesarCipher()->None:
    letters = list("abcdefghijklmnopqrstuvwxyz")
    res_symbols = []
    str_to_code = str(input("Enter string to code: "))
    step = int(input("Enter step for cipher: "))
    for s in str_to_code:
        if s == ' ':
            res_symbols.append(' ')
            continue
        index = letters.index(s.lower()) + step
        if index >= len(letters):
            index = index % len(letters)
        print(index)
        res_symbols.append(letters[index].upper()) if s.isupper() else res_symbols.append(letters[index])
    res = str(res_symbols)
    print(res)

#Exercize5
def school() -> None:
    summary = {}
    while True:
        cur_str = str(input("Enter subject, family, grade: "))
        if len(cur_str) == 0:
            break
        if len(cur_str.split()) != 3:
            print('Invalid input')
            continue
        subject, family, grade = cur_str.split()
        if subject not in summary:
            summary[subject] = {}
        if family not in summary[subject]:
            summary[subject][family] = []
        summary[subject][family].append(int(grade))
    for subject in summary:
        print(subject)
        for family in summary[subject]:
            print(f'{family}:  {summary[subject][family]}')

while True:
    find_tickets()

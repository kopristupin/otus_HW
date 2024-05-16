#Exercise 1
def mirror_three_center_numbers() -> None:
    i = input("Enter number: ")
    if len(i) != 5 or i[0] == '0':
        print("Invalid number!")
        return
    print(i[0], i[3:0:-1], i[-1], sep='')
    return

#Exercise 2
def count_holidays() -> None:
    days_till_vacation = int(input("Enter days count till weekend: "))
    whole_weeks_count = int(days_till_vacation // 7)
    result_holidays = 0
    if whole_weeks_count >= 1:
        result_holidays += whole_weeks_count * 2
    residue_days = days_till_vacation % 7
    if residue_days > 5:
        result_holidays += 7 - residue_days
    print(result_holidays)

#Exercise 3
def from_arabic_to_roman_number() -> None:
    num = int(input("Enter number: "))
    arabic_to_roman = [ (1000, 'M'), (500, 'D'), (100, 'C'), (50 , 'L'), (10, 'X'),  (5 , 'V', ), (1, 'I')]
    result_str = ''
    residue = num
    for index, (arabic, roman) in enumerate(arabic_to_roman):
        cur_whole_num = int(residue / arabic)
        if cur_whole_num > 3:
            less_str = roman * (arabic_to_roman[index-1][0] - cur_whole_num) + arabic_to_roman[index-1][1]
            more_str = arabic_to_roman[index-1][1] * arabic_to_roman[index-1][0]
        else:
            result_str += roman * cur_whole_num
            residue = residue - cur_whole_num*arabic
    print('result : ', result_str)

#Exercise 4
def check_can_break() -> None:
    long = int(input("Enter long of chocoate: "))
    width = int(input("Enter width of chocoate: "))
    peace = int(input("Enter peace of chocoate to get: "))
    if peace > long * width:
        print("Not possible!")
        return
    if peace % long == 0:
        print("Possible!")
    elif peace % width == 0:
        print("Possible!")
    else:
        print("Not possible!")
    return

#Exercise 5
def check_if_valid_real_num() -> bool:
    num_str = str(input("Enter number to valid: "))
    nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    if len(num_str) == 0:
        return False
    dot_count = 0
    start_index = 0
    if num_str[0] == '-':
        start_index = 1
    for symb in num_str[start_index:]:
        if symb == '.':
            dot_count += 1
            if dot_count >= 2:
                return False
        elif symb not in nums:
            return False
    return True
        
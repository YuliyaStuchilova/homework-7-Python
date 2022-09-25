def book():
    people = list()
    second_name = input('Введите фамилию: ')
    people.append(second_name)
    first_name = input('Введите имя: ')
    people.append(first_name)
    patronymic = input('Введите отчество: ')
    people.append(patronymic)
    flag = True
    while flag:
        numder = input('Введите номер телефона: ')
        if len(numder) != 11:
            print('Количество цифр в номере неправильное, попробуйте снова: ')
        else:
            flag = False
    people.append(int(numder))

    return people

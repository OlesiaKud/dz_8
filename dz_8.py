# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 5. Программа должна иметь возможность удаления и добавления данных

def interfeis_contact(telefon_list_name_file = 'Telephone_list.txt'):
    print('Меню ТЕЛЕФОННОЙ КНИГИ:\n 1: поиск контакта, \n 2: добавление контакта, \n 3: удаление контакта, \n 4: редактирование контакта, \n 5: вывод всех контактов,\n 6: группы контактов, \n 0: выход.')
    interfeis_contact = int(input())
    match interfeis_contact:
        case 1:
            find_contact()
        case 2:         
            write_contact()
        case 3:            
            delete_contacts()
        case 4:       
            edit_contacts()
        case 5:
            print_contacts()
        case 6:
            print_group()
        case 0:
            return
        case _:
            interfeis_contact = int(input('Выберите:\n1-> поиск, 2-> добавление контакта, 3-> удаление контакта, 4-> редактирование, 5-> вывод всех контактов,6-> группы контактов 0-> выход.\n '))


def write_contact(telefon_list_name_file = 'Telephone_list.txt'):
    with open(telefon_list_name_file, 'a', encoding='UTF-8') as telefon_list:
        first_name = input("Введите фамилию: ")        
        last_name = input("Введите имя: ")
        telefon = input("Введите телефон: ")
        while len(telefon) != 11 or not telefon.isdigit():
            print('Вы ввели неправильный телефон')
            telefon = input("Введите телефон: ")
        print('Выберите группу: 1 - семья, 2 - коллеги, 3 - друзья, 0 - не назначено')
        group = int(input('Введите:'))
        match group:
            case 1:
                group_list = ('семья')
            case 2:
                group_list = ('коллеги')    
            case 3:
                group_list = ('друзья')
            case _:
                group_list = ('не установлено')
            
        telefon_list.write('\n' + last_name + ', ' +  first_name + ', ' +  telefon + ', ' + group_list)
    print()
    interfeis_contact()


def find_contact(telefon_list_name_file = 'Telephone_list.txt'):
    with open(telefon_list_name_file, 'r', encoding='UTF-8') as telefon_list:
        find_name = input('Поиск: ')
        lines = telefon_list.readlines()
        None_contact = True
        for i in lines:
            if find_name in i:
                print('Найден контакт:', i, end = '')
                None_contact = False
        if None_contact:
            print('Контакт не найден')
    print()
    interfeis_contact()


def print_contacts(telefon_list_name_file = 'Telephone_list.txt'):
    with open(telefon_list_name_file, 'r', encoding='UTF-8') as telefon_list:
        lines = telefon_list.readlines()
        for i in lines:
            print(i, end = '')
    print()
    interfeis_contact()


def delete_contacts(telefon_list_name_file = 'Telephone_list.txt'):
    print('\n Имя | Фамилия | Телефон')
    with open(telefon_list_name_file, 'r', encoding='utf-8') as telefon_list:
        telefon_list = telefon_list.read()
        print(telefon_list)
        print(' ')
        index_delete_data = int(input('Введите номер строки для удаления: ')) 
        tel_book_lines = telefon_list.split('\n')
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        print(f'Удалена запись: {del_tel_book_lines}\n')
        with open(telefon_list_name_file, 'w', encoding='utf-8') as data:
            data.write('\n'.join(tel_book_lines))
    print()
    interfeis_contact()


def edit_contacts(telefon_list_name_file = 'Telephone_list.txt'):
    print('\n Имя  | Фамилия   | Телефон')
    with open(telefon_list_name_file, 'r', encoding='utf-8') as telefon_list:
        telefon_list = telefon_list.read()
        print(telefon_list)
        print(' ')
        index_delete_data = int(input('Введите номер строки для редактирования: '))
        tel_book_lines = telefon_list.split('\n')
        edit_tel_book_lines = tel_book_lines[index_delete_data]
        elements = edit_tel_book_lines.split(' , ')
        last_name = input('Введите имя: ')
        first_name = input('Введите фамилию: ')        
        phone = input('Введите телефон: ')
        if len(first_name) == 0:
            first_name = elements[1]
            if len(last_name) == 0:
                last_name = elements[2]
                if len(phone) == 0:
                    phone = elements[2]
        edited_line = f'{last_name}, {first_name}, {phone}'
        tel_book_lines[index_delete_data] = edited_line
        print(f'Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n')
        with open(telefon_list_name_file, 'w', encoding='utf-8') as data:
            data.write('\n'.join(tel_book_lines))
    print()
    interfeis_contact()
def print_group(telefon_list_name_file = 'Telephone_list.txt'):
    # with open(telefon_list_name_file, 'r', encoding='utf-8') as telefon_list:
    #     telefon_list = telefon_list.read()
    #     print('Введите "коллеги", "семья", "друзья", чтобы отобразить состав интересующей вас группы')
    #     find_group = input('Поиск: ')
    #     lines = telefon_list.readlines()
    #     None_contact = True
    #     for i in lines:
    #         if find_group in i:
    #             print('Контакты группы:', i, end = '')
    #             None_contact = False
    #     if None_contact:
    #         print('Группа пуста.')

    #         def print_group(telefon_list_name_file='Telephone_list.txt'):
    with open(telefon_list_name_file, 'r', encoding='utf-8') as telefon_list_file:
        telefon_list = telefon_list_file.read()
        print('Введите "коллеги", "семья", "друзья", чтобы отобразить состав интересующей вас группы')
        find_group = input('Поиск: ')
        lines = telefon_list.split('\n')
        None_contact = True
        for i in lines:
            if find_group in i:
                print('Контакты группы:', i, end='')
                None_contact = False
        if None_contact:
            print('Группа пуста.')
    print()
    interfeis_contact()


interfeis_contact()
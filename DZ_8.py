# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

from csv import DictWriter, DictReader
from os.path import exists

def get_info():
    info = []
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('Неправильный номер. Номер должен состоять из 11 цифр.')
            else:
                flag = True
        except ValueError:
            print('Некорректный ввод. Введите номер в виде целого числа.')
    info.append(phone_number)
    return info


def create_file():
    if not exists('phone.csv'):
        with open('phone.csv', 'w', encoding='utf-8') as data:
            f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_n_writer.writeheader()


def write_file(lst):
    with open('phone.csv', 'a', encoding='utf-8', newline='') as f_n:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writerow(obj)


def read_file(file_name):
    phone_book = []
    if exists(file_name):
        with open(file_name, encoding='utf-8') as f_n:
            f_n_reader = DictReader(f_n)
            phone_book = list(f_n_reader)
    return phone_book


def record_info():
    lst = get_info()
    write_file(lst)


def update_contact():
    name_to_update = input('Введите имя или фамилию контакта для обновления: ')
    phone_records = read_file('phone.csv')
    updated_records = []
    updated = False
    for record in phone_records:
        if name_to_update in record['Имя'] or name_to_update in record['Фамилия']:
            new_last_name = input(
                f'Введите новую фамилию для {record["Фамилия"]} (оставьте пустым, если не хотите менять): ')
            new_first_name = input(f'Введите новое имя для {record["Имя"]} (оставьте пустым, если не хотите менять): ')
            new_phone_number = input(
                f'Введите новый номер телефона для {record["Номер"]} (оставьте пустым, если не хотите менять): ')
            if new_first_name:
                record['Имя'] = new_first_name
            if new_last_name:
                record['Фамилия'] = new_last_name
            if new_phone_number:
                record['Номер'] = new_phone_number
            updated = True
        updated_records.append(record)
    if updated:
        with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
            f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_n_writer.writeheader()
            f_n_writer.writerows(updated_records)
        print('Контакт успешно обновлен.')
    else:
        print('Контакт не найден.')


def delete_contact():
    name_to_delete = input('Введите имя или фамилию контакта для удаления: ')
    phone_records = read_file('phone.csv')
    updated_records = []
    deleted = False
    for record in phone_records:
        if name_to_delete in record['Имя'] or name_to_delete in record['Фамилия']:
            deleted = True
        else:
            updated_records.append(record)
    if deleted:
        with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
            f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_n_writer.writeheader()
            f_n_writer.writerows(updated_records)
        print('Контакт успешно удален.')
    else:
        print('Контакт не найден.')


def main():
    create_file()
    while True:
        command = input('Введите команду (q - выход, r - чтение, w - запись, u - обновление, d - удаление): ')
        if command == 'q':
            break
        elif command == 'r':
            phone_records = read_file('phone.csv')
            if not phone_records:
                print('Телефонная книга пуста.')
            else:
                for record in phone_records:
                    print(record)
        elif command == 'w':
            record_info()
        elif command == 'u':
            update_contact()
        elif command == 'd':
            delete_contact()


if __name__ == '__main__':
    main()

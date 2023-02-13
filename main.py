import re
import csv


def fixer(list):
    new_list = []
    phone_pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
    phone_sub = r'+7(\2)\3-\4-\5 \6\7'
    for contact in list:
        string = f'{contact[0]} {contact[1]} {contact[2]}'
        phone = re.sub(phone_pattern, phone_sub, contact[5])
        new_list.append(
            [string.split(' ')[0], string.split(' ')[1], string.split(' ')[2], contact[3], contact[4], phone,
             contact[6]])
    return new_list


def writer(list):
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list)
    return 'succesful'


def union(list):
    for contact in list:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in list:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "":
                    contact[2] = new_contact[2]
                if contact[3] == "":
                    contact[3] = new_contact[3]
                if contact[4] == "":
                    contact[4] = new_contact[4]
                if contact[5] == "":
                    contact[5] = new_contact[5]
                if contact[6] == "":
                    contact[6] = new_contact[6]
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    return result


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    print(writer(union(fixer(contacts_list))))
    
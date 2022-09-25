def find_people(documents, num_doc):
    # p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
    for document in documents:
        if document['number'] == num_doc:
            return document['name']
    else:
        return None


def find_shelf(directories, num_doc):
    # s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится
    for key, value in directories.items():
        if num_doc in value:
            return key
    else:
        return None


def print_all_docs(documents):
    # l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    for document in documents:
        print(document['type'] + ' "' + document['number'] + '" "' + document['name'] + '"')


def add_new_doc(documents, directories, num_doc, type_doc, name_doc, shelf_doc):
    # a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер,
    # тип, имя владельца и номер полки, на котором он будет храниться.
    if shelf_doc in directories.keys():
        documents.append({"type": type_doc, "number": num_doc, "name": name_doc})
        directories[shelf_doc].append(num_doc)
        return True
    else:
        return False


def delete_doc(documents, directories, num_doc):
    # d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
    delete_index = None
    for index, document in enumerate(documents):
        if document['number'] == num_doc:
            delete_index = index
            break

    if delete_index is None:
        result = 'Указанного документа нет в списке документов'
    else:
        documents.pop(delete_index)
        result = 'Документ удален из списка документов'

    delete_key = None
    for key, value in directories.items():
        if num_doc in value:
            delete_key = key

    result += '. '
    if delete_key is None:
        result += 'На полках не было указанного документа'
    else:
        directories.pop(key)
        result += 'Документ был удален с полки'

    return result


def move_doc(directories, num_doc, shelf_name):
    # m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    current_key = None
    for key, value in directories.items():
        if num_doc in value:
            current_key = key
            break

    if current_key is None:
        return 'не найден документ на текущих полках'

    if directories.get(shelf_name) is None:
        return 'не найдена новая полка'

    directories[current_key].remove(num_doc)
    directories[shelf_name].append(num_doc)
    return 'Полка успешно перемещена'


def add_shelf(directories, shelf_name):
    # as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
    if directories.get(shelf_name) is None:
        directories[shelf_name] = []
        return True
    else:
        return False


def main(documents, directories):
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'p':
            num_doc = input('Введите номер документа ')
            name = find_people(documents, num_doc)
            if name is None:
                print('В базе нет данных по данному номеру документа')
            else:
                print(f"имя: {name}")
        elif command == 's':
            num_doc = input('Введите номер документа ')
            shelf_number = find_shelf(directories, num_doc)
            if shelf_number is None:
                print('В базе нет данных по данному номеру документа')
            else:
                print(f'номер полки с указаннным документом: {shelf_number}')
        elif command == 'l':
            print_all_docs(documents)
        elif command == 'a':
            num_doc = input('Введите номер документа: ')
            type_doc = input('Укажите тип документа: ')
            name_doc = input('Укажите имя владельца: ')
            shelf_doc = input('Укажите номер полки, на которой он будет храниться: ')
            result = add_new_doc(documents, directories, num_doc, type_doc, name_doc, shelf_doc)
            if result:
                print('Документ успешно добавлен')
            else:
                print('Указанной полки не существует, документ не добавлен!')
        elif command == 'd':
            num_doc = input('Введите номер документа: ')
            result = delete_doc(documents, directories, num_doc)
            print(result)
        elif command == 'm':
            num_doc = input('Введите номер документа: ')
            shelf_name = input('Укажите полку, куда на перенести документ: ')
            result = move_doc(directories, num_doc, shelf_name)
            print(result)
        elif command == 'as':
            shelf_name = input('Укажите название полки: ')
            result = add_shelf(directories, shelf_name)
            if result:
                print('Полка успешно добавлена')
            else:
                print('Данная полка уже есть')


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

if __name__ == '__main__':
    main(documents, directories)
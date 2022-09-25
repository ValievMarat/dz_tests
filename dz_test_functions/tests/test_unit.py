import unittest
from main import find_people, find_shelf, add_new_doc, delete_doc, move_doc, add_shelf
from parameterized import parameterized

class TestFunction(unittest.TestCase):
    docs = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "invoice", "number": "11-3", "name": "Аркадий Ветров"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

    dirs = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': [],
        '5': ['11-3'],
        '6': ['008'],
        '7': ['009']
    }

    @parameterized.expand(
        [
            (docs, '10006', 'Аристарх Павлов'),
            (docs, '11-2', 'Геннадий Покемонов'),
            (docs, '333', None)
        ]
    )

    def test_find_people(self, documents, num_doc, result):
        calc_result = find_people(documents, num_doc)
        self.assertEqual(result, calc_result)


    @parameterized.expand(
        [
            (dirs, '10006', '2'),
            (dirs, '11-2', '1'),
            (dirs, '2207 876234', '1'),
            (dirs, '123', None)
        ]
    )
    def test_find_shelf(self, directories, num_doc, result):
        calc_result = find_shelf(directories, num_doc)
        self.assertEqual(result, calc_result)

    @parameterized.expand(
        [
            (docs, dirs, '451', 'passport', 'Ivanov', '1', True),
            (docs, dirs, '4564-2', 'passport', 'Petrov', '2', True),
            (docs, dirs, '1874', 'passport', 'Sidorov', '3', True),
            (docs, dirs, '232', 'passport', 'Valsev', '4', False)
        ]
    )
    def test_add_new_doc(self, documents, directories, num_doc, type_doc, name_doc, shelf_doc, result):
        calc_result = add_new_doc(documents, directories, num_doc, type_doc, name_doc, shelf_doc)
        self.assertEqual(result, calc_result)


    @parameterized.expand(
        [
             (docs, dirs, '11-3', 'Документ удален из списка документов. Документ был удален с полки'),
             (docs, dirs, '777', 'Указанного документа нет в списке документов. На полках не было указанного документа'),
             (docs, dirs, '5455 028765', 'Указанного документа нет в списке документов. Документ был удален с полки')
        ]
    )
    def test_delete_doc(self, documents, directories, num_doc, result):
        calc_result = delete_doc(documents, directories, num_doc)
        self.assertEqual(result, calc_result)

    dirs = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': [],
        '5': ['11-3'],
        '6': ['008'],
        '7': ['009']
    }
    @parameterized.expand(
        [
            (dirs, '010', '8', 'не найден документ на текущих полках'),
            (dirs, '008', '7', 'Полка успешно перемещена'),
            (dirs, '009', '6', 'Полка успешно перемещена')
        ]
    )
    def test_move_doc(self, directories, num_doc, shelf_name, result):
        calc_result = move_doc(directories, num_doc, shelf_name)
        self.assertEqual(result, calc_result)

    @parameterized.expand(
        [
            (dirs, '444', True),
            (dirs, '444', False),
             (dirs, '555', True)
        ]
    )
    def test_add_shelf(self, directories, shelf_name, result):
        calc_result = add_shelf(directories, shelf_name)
        self.assertEqual(result, calc_result)
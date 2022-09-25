import pytest
from main import YaDisk

fixture = [
    ('test_folder2', {'code': 201, 'message': ''}),
    ('test_folder2', {'code': 409, 'message': ''}),
    ('test_folder3', {'code': 201, 'message': ''}),
    ('', {'code': 400, 'message': 'Ошибка проверки поля "path": Это поле является обязательным.'})
]

class TestFunc:
    @pytest.mark.parametrize('folder_name, result', fixture)
    def test_create_folder(self, folder_name, result):
        yandex_disk = YaDisk()
        calc_result = yandex_disk.create_folder(folder_name)
        assert calc_result['code'] == result['code']
        assert calc_result['message'] == result['message']

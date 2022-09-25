import requests

class YaDisk:
    def __init__(self):
        with open('token_yadisk.txt') as file:
            self.token = file.read()

    def create_folder(self, folder_name: str):
        # создадим папку, в случае её отсутствия
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources'

        headers = {'Authorization': f'OAuth {self.token}',
                   'Content-Type': 'Application/json',
                   'Accept': 'application/json'}
        params = {'path': folder_name}
        resp = requests.put(url, params=params, headers=headers)
        status_code = resp.status_code
        text_status = ''
        if resp.status_code != 201 and resp.status_code != 409:
            text_status = resp.json()['message']
        return {'code': status_code,
                'message': text_status}

if __name__ == '__main__':
    yandex_disk = YaDisk()
    status = ''
    result = yandex_disk.create_folder('test_folder1')
    print(result)
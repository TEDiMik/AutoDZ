import requests


def loginbot(login, password):


        s = requests.Session()

        '''
        url надо получать на месте
        Через сетевой город
        '''
        url = 'https://auth.ir-tech.ru/core/connect/authorize?client_id=SGOContext&nonce=825e71f2-4cec-4bfb-885d-d4037a703e8a&response_type=code&scope=openid SGOContext&redirect_uri=http%3a%2f%2fsg.lyceum130.ru%2fasp%2fsso%2firtech%2fcallback%2flogin'



        data = {"":'',
                'idsrv.xsrf': 'iJCm7F7k6ZEdbQj1IR41l4msq6gLs_c8nLlGAmFOCgMrd1tE50e7nzEO3SaPo7p_zIjixn0khBVtQnNTfrk04_nuFd_SYBvi9QJzS9Tb1r0',
                'username': login,
                'password': password,
                'go': ''
        }
        r = s.post(url,data)
        print(r.text)
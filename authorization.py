import requests


def loginbot(login, password):


        s = requests.Session()

        url = 'https://auth.ir-tech.ru/core/login?signin=75281d38fa2a79e7fe5699913bc1c535'



        data = {"":'',
                'idsrv.xsrf': 'iJCm7F7k6ZEdbQj1IR41l4msq6gLs_c8nLlGAmFOCgMrd1tE50e7nzEO3SaPo7p_zIjixn0khBVtQnNTfrk04_nuFd_SYBvi9QJzS9Tb1r0',
                'username': login,
                'password': password,
                'go': ' '
        }
        r = s.post(url,data)
        print(r.text)
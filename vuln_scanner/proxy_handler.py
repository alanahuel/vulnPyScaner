def get_proxy():
    try:
        return {'http': 'http://proxy.example.com:8080'}
    except Exception as err:
        print(f'Error occurred while getting proxy: {err}')

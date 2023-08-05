import requests
from .link_handler import get_all_links
from .form_handler import get_all_forms
from .proxy_handler import get_proxy

def scan(url):
    try:
        proxy = get_proxy()
        response = requests.get(url, proxies=proxy)
        response.raise_for_status()

        links = get_all_links(response.text)
        forms = get_all_forms(response.text)

        return {"links": links, "forms": forms}

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occurred: {err}')

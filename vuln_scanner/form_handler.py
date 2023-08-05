from bs4 import BeautifulSoup

def get_all_forms(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        forms = soup.find_all('form')
        return forms
    except Exception as err:
        print(f'Error occurred while extracting forms: {err}')

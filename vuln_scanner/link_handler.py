from bs4 import BeautifulSoup

def get_all_links(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]
        return links
    except Exception as err:
        print(f'Error occurred while extracting links: {err}')

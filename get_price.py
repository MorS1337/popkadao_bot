import requests
import re
from bs4 import BeautifulSoup

def get_link_to_item(url: str) -> str:
    '''Из-за переадресации невозможно совершить парсинг,
       поэтому нужно получить ссылку на сам товар. 
       Функция берёт обычную ссылку и возвращает пригодную
       для парсинга ссылку'''
       
    #Делаем запрос get запрос и получаем html код
    response = requests.get(url)
    html_code = response.text

    # Извлекаем ссылку из HTML-кода с помощью регулярного выражения
    regex_pattern = r"https?://[^\s/$.?#].[^\s]*"
    extracted_urls = re.findall(regex_pattern, html_code)

    if extracted_urls:
        return extracted_urls[0]
    else:
        return None
    
# def get_item_price(url: str) -> int:
#     if url is not None:
#         with requests.Session() as session:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#                 'Accept-Language': 'ru-RU,ru;q=0.5',
#                 'Accept-Encoding': 'gzip, deflate, br',
#                 'Content-Type': 'application/x-www-form-urlencoded',
#                 'Cookie': '_m_h5_tk=39b16e41e561127260078bb4e4e5be19_1686652185104; _m_h5_tk_enc=0b348cc71ec2395be5147101f43ab717; _samesite_flag_=true; cookie2=1ccf9803293ce802a20e647fb4e6b8fb; t=de6749f523932bb9f8108bc15e707268; _tb_token_=033e70e3b7be; isg=BKCgHXAh0GuWD2yLp-_zpM-Oca5yqYRzWFH73hqxbLtOFUA_wrlUA3YkraWVpTxL',
#                 'Origin': 'https://h5.m.goofish.com',
#                 'Referer': 'https://h5.m.goofish.com',
#                 'Sec-Ch-Ua': "Not.A/Brand;v=8 Chromium;v=114, Brave;v=114"
#             }
#             session.headers.update(headers)
            
#             response = session.get(url)
#             html_code = response.content

#             soup = BeautifulSoup(html_code, 'lxml')
#             item_price = soup.find('span', class_="rax-text-v2 priceMod--soldPrice--20BWwRm")
#             print(soup.prettify())
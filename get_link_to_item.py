import requests
import re

def get_link_to_item(url: str) -> str:

    response = requests.get(url)
    html_code = response.text

    # Извлекаем ссылку из HTML-кода с помощью регулярного выражения
    regex_pattern = r"https?://[^\s/$.?#].[^\s]*"
    extracted_urls = re.findall(regex_pattern, html_code)

    if extracted_urls:
        return extracted_urls[0]
    else:
        raise Exception("Ссылка не найдена")
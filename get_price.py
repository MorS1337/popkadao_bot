import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Item

def get_shipping_info(driver: webdriver) -> str:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='rax-view-v2 priceMod--priceTagContainer']"))).text
    if '包邮' in element:
        return 'Free'
    return 'Paid'

def cut_brand_name(name: str) -> str:
    return name.split('/')[0]

def cut_image_url(url: str) -> str:
    return url[:-6]

def get_link_to_item(url: str) -> str:
    '''Из-за переадресации невозможно совершить парсинг,
       поэтому нужно получить ссылку на сам товар. 
       Функция берёт обычную ссылку и возвращает пригодную
       для парсинга ссылку'''
       
    # Делаем запрос get запрос и получаем html код
    response = requests.get(url)
    html_code = response.text

    # Извлекаем ссылку из HTML-кода с помощью регулярного выражения
    regex_pattern = r"https?://[^\s/$.?#].[^\s]*"
    extracted_urls = re.findall(regex_pattern, html_code)

    if extracted_urls:
        return extracted_urls[0]
    else:
        return None

def get_info(url: str) -> Item:
    # options
    options = webdriver.ChromeOptions()

    # disable webdriver
    options.add_argument("--disable-blink-features=AutomationControlled")

    # user-agent
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    
    # Wait for the iframe to be available and switch to it
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)
    
    try:
        price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='rax-view-v2 priceMod--priceTextWrap']"))).text
    except Exception as ex:
        print('Error finding price: ', ex)
        
    try:
        brand_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='rax-text-v2 spvListMod--valueName']"))).text
    except Exception as ex:
        brand_name = None
        print('Error finding brand name: ', ex)
    
    try: 
        description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='rax-text-v2 detailDesc--descText']"))).text
    except Exception as ex:
        print('Error finding description: ', ex)
        
    try:
        image_url = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='rax-view-v2 imageListMod--imageWrap'] img"))).get_attribute('src')
    except Exception as ex:
        image_url = None
        print('Error finding image URL: ', ex)
        
    try:
        shipping_price = get_shipping_info(driver)
    except Exception as ex:
        shipping_price = None
        print('Error finding shipping price: ', ex)
    
    driver.quit()
    
    return Item(
        description=description,
        price=price[2:],
        image_url=cut_image_url(image_url),
        brand_name=cut_brand_name(brand_name),
        shipping_price=shipping_price
    )

if __name__ == '__main__':
    url = get_link_to_item("https://m.tb.cn/h.gelpGFW?tk=V316WDDoIyw")
    print(get_info(url))

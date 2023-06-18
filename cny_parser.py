from bs4 import BeautifulSoup
import requests

def get_course(url: str) -> str:
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'lxml')
    
    course = soup.find('div', class_='course')
    return course.text
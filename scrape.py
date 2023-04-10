from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

driver.get('https://www.tripadvisor.com.br/Attractions-g2628648-Activities-c61-Vale_do_Paraiba_State_of_Sao_Paulo.html')

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

names = soup.find_all(class_='XfVdV o AIbhI')
names = [i.text for i in names]
names = [i[3:] for i in names]

desc = soup.find_all(class_='BKifx')
desc = [i.text for i in desc]


dic = {
    'Título': [i for i in names],
    'Descriçao': [i for i in desc]
}

print(pd.DataFrame(dic))

driver.quit()



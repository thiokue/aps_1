from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options


def get_data():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.tripadvisor.com.br/Attractions-g2628648-Activities-c61-Vale_do_Paraiba_State_of_Sao_Paulo.html')

    page = driver.page_source

    soup = BeautifulSoup(page, 'html.parser')

    names = soup.find_all(class_='XfVdV o AIbhI')
    names = [i.text for i in names]
    names = [i[3:] for i in names]

    desc = soup.find_all(class_='BKifx')
    desc = [i.text for i in desc]

    comments = soup.find_all('span', class_='biGQs _P pZUbB osNWb')
    comments = [i.text for i in comments]

    rating_raw = soup.find_all(class_='jVDab o W f u w JqMhy')
    rating = soup.find_all('svg', {'class': 'UctUV d H0 hzzSG'})
    rating = [i.get('aria-label') for i in rating]
    del rating[0]
    rating = [i[:3] for i in rating]

    dic = {
        'Título': [i for i in names],
        'Num Comentários': [i for i in comments],
        'Rating': [i for i in rating],
        'Descriçao': [i for i in desc],
    }

    df = pd.DataFrame(dic)
    df = df.reset_index(drop=True)


    driver.quit()
    return df.to_csv('tripAdvisor_Atividades_ao_ar_livre.csv')
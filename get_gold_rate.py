import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_gold_rate():

    url = "https://www.livechennai.com/gold_silverrate.asp"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'class': 'table-price'})

    data = []
    for row in table.find_all('tr')[1:]:
        row_data = [data.text.strip() for data in row.find_all('td')]
        data.append(row_data)

    headers = ['Date','1g of 24k gold','8g of 24k gold','1g of 22k gold','8g of 24k gold']
    price = []
    table_data = []
    for i in data:
        if "/" in i[0]:
            price.append(i)


    df = pd.DataFrame(price, columns=headers)

    return df

    # print(df)
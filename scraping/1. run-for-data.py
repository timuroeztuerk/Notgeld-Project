import time
import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
import csv

def process_product(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1').get_text(strip=True) if soup.find('h1') else ''
    price = soup.find(class_="price--content content--default").get_text(strip=True) if soup.find(class_="price--content content--default") else ''
    base_info = soup.find(class_="product--base-info list--unstyled").get_text(strip=True) if soup.find(class_="product--base-info list--unstyled") else ''
    table_contents = soup.find(class_="product--properties-table").get_text(strip=True)
    return {
        'url': product_url,
        'title': title,
        'price': price,
        'base_info': base_info,
        'table_contents': table_contents
    }

if __name__ == '__main__':
    start_time = time.time()

    product_urls = []
    with open("scraping/1923_notgeld.txt", "r") as f:
        for line in f:
            product_urls.append(line.strip())

    with Pool(processes=10) as pool:
        product_data_list = pool.map(process_product, product_urls)

    csv_columns = ['url', 'title', 'price', 'base_info', 'table_contents']
    csv_file = "scraping/product_data.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in product_data_list:
            writer.writerow(data)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds") # 318 seconds.
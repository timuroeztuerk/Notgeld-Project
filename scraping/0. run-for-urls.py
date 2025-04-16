import requests
from bs4 import BeautifulSoup
from multiprocessing import get_context, set_start_method

base_url = "https://www.gap-banknoten.de/widgets/listing/listingCount/sCategory/"

def fetch_url(page_number):
    url = f"{base_url}?p={page_number}&o=5&n=100000&c=230&loadProducts=1"
    resp = requests.get(url)
    urls = []
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        for product in soup.find_all(class_="product--info"):
            title = product.find(class_="product--title")
            if title and title.has_attr("href"):
                urls.append(title["href"])
    return urls

all_urls = []
def fetch_all_urls():
    global all_urls
    with get_context("spawn").Pool() as pool:
        results = pool.map(fetch_url, range(1, 80))
        for result in results:
            all_urls.extend(result)
    all_urls = list(set(all_urls))

def main():
    global all_urls
    if __name__ == "__main__":
        set_start_method("spawn")
        fetch_all_urls()
        print(f"Total unique URLs fetched: {len(all_urls)}")
        for url in all_urls:
            print(url)

if __name__ == "__main__":
    main()

# Save all urls to a file
with open("scraping/1923_notgeld.txt", "w") as f:
    for url in all_urls:
        f.write(url + "\n")
import requests
from bs4 import BeautifulSoup

main_sites = [
    'https://bts.ibighit.com',
    'https://www.bts_ARMY.com',
    'https://bts-diary.tumblr.com'
]

keywords = ["jeans", "shoes", "shirt", "jewelry", "ring", "necklace", "sneakers", "sandals", "perfume", "cologne", "hat"]

member_sites = {
    'RM': ['https://rm.bts.ibighit.com', 'https://rm-army.tumblr.com'],
}

headers = {'User-Agent': 'ARMYbot v1'}

for url in main_sites:
    try:
        response = requests.get(url, headers=headers)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        for keyword in keywords:
            results = soup.find_all(string=lambda t: keyword in t.lower())
            for result in results:
                print(f"Found '{keyword}' on {url}: {result}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

for member, urls in member_sites.items():
    for url in urls:
        try:
            response = requests.get(url, headers=headers)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')
            for keyword in keywords:
                results = soup.find_all(string=lambda t: keyword in t.lower())
                for result in results:
                    print(f"Found '{keyword}' on {member}'s site {url}: {result}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

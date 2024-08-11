import requests
from bs4 import BeautifulSoup

name = input("What to search:")

dorks = [
    'filetype:', 'ext:'
]

file_types = [
    'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt',
    'text', 'zip', 'rar', 'odp', 'ods', 'odt', 'kml', 'kmz', 'xml'
]

for dork in dorks:
    for file_type in file_types:
        query = f"{dork}{file_type} {name}"
        url = f"https://duckduckgo.com/html/?q={query}"

        try:
            print(f"Searching for: {query}")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            results = soup.find_all('a', class_='result__a', limit=5)

            if results:
                for result in results:
                    link = result['href']
                    print(link)
            else:
                print("No results found.")

        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print(f"Finished searching for {query}")
print("Done")

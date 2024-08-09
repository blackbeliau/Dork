from googlesearch import search

name = input("What to search:")
dorks = [
    'filetype:',
    'ext:'
]
types = [
    'pdf', 'doc', 'docx', 'xls', 'xlsx',
    'ppt', 'pptx', 'txt', 'text', 'zip',
    'rar', 'odp', 'ods', 'odt', 'kml',
    'kmz', 'xml'
]


try:
    query = f'{dorks}{types}{name}'
    print(f"Searching for: {query}")
    for result in search(query, num=5, stop=5, pause=5):
        print(result)
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Finished searching for {query}")

print("Done")

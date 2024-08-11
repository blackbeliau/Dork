from googlesearch import search

name = input("What to search:")

dorks = [
    'inlink:', 'intext:', 'intitle:', 'inurl:', 'in:', 'on:'
]

for dork in dorks:
    query = f"{dork} {name}"
    try:
        print(f"Searching for: {query}")
        for result in search(query, num=5, stop=5, pause=5):
            print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"Finished searching for {query}")
print("Done")

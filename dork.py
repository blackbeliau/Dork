from googlesearch import search

name = input("What to search:")
dorks = [
    'inlink:', 
    'intext:', 
    'intitle:', 
    'inurl:', 
    'in:', 
    'on:'
]

try:
    query = f' {dorks} {name}'
    print(f"Searching for: {query}")
    for result in search(f'{query}', num=5, stop=5, pause=5):
        print(result)
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Finished searching for {query}")

print("Done")

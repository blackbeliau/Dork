from googlesearch import search

nama = input("Nama Lengkap Target:")
dorks = [
    'filetype:',
    'ext:'
]
type = [
    'pdf',
    'doc',
    'docx',
    'xls',
    'xlsx',
    'ppt',
    'pptx',
    'txt',
    'text',
    'zip',
    'rar',
    'odp',
    'ods',
    'odt',
    'kml',
    'kmz',
    'xml'
]

for i in dorks:
  try:
      print(f"Searching for: {i}{type}{nama}")
      for result in search(f'{i}{type}{nama}', num=5, stop=5, pause=5):
          print(result)
      else:
          print(f"Still Finding For {nama}")
  except Exception as e:
      print(f"An error occurred: {e}")

print("Done")

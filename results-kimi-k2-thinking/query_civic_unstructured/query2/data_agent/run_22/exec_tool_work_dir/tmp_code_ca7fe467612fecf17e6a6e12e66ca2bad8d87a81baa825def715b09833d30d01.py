code = """import json, re

# Load data from temporary files
civic_docs = json.load(open('var_functions.query_db_36'))
funding = json.load(open('var_functions.query_db_8'))

projects = []
for doc in civic_docs:
  txt = doc.get('text', '')
  if 'Park' in txt and 'completed' in txt.lower() and '2022' in txt:
    for line in txt.split('\n'):
      line = line.strip()
      if 'Park' in line and len(line) < 120 and 'update' not in line.lower() and 'schedule' not in line.lower():
        if line not in projects:
          projects.append(line)

total = 0
matched = 0
for p in projects:
  pl = p.lower()
  for f in funding:
    if f['Project_Name'].lower() == pl:
      total += int(f['Amount'])
      matched += 1

result = {'total_funding': total, 'matches': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)

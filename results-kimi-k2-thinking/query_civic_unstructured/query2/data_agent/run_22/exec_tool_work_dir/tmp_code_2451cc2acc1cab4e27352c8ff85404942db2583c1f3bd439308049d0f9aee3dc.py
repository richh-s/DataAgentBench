code = """import json, re

docs = json.load(open('var_functions.query_db_36'))
funds = json.load(open('var_functions.query_db_8'))

found = []
for doc in docs:
  txt = doc.get('text', '')
  for line in txt.split('\n'):
    line = line.strip()
    if 'Park' in line and len(line) < 150:
      if 'update' not in line.lower() and 'schedule' not in line.lower():
        ctx = txt.split('\n')
        for l in ctx:
          if 'completed' in l.lower() and '2022' in l:
            if line not in found:
              found.append(line)
            break

total = 0
for p in found:
  pl = p.lower()
  for f in funds:
    fl = f['Project_Name'].lower()
    if pl == fl:
      total += int(f['Amount'])

print('__RESULT__:')
print(json.dumps({'total': total, 'projects': len(found)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)

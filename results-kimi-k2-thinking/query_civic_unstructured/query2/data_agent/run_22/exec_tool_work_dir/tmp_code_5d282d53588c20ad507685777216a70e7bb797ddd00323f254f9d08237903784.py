code = """import json

civic = json.load(open('var_functions.query_db_36'))
funding = json.load(open('var_functions.query_db_8'))

# Find park projects completed in 2022
projects = []
for doc in civic:
  t = doc.get('text', '')
  if 'Park' in t and '2022' in t and 'completed' in t.lower():
    for line in t.split('\n'):
      line = line.strip()
      if 'Park' in line and len(line) < 120:
        if 'update' not in line.lower() and 'schedule' not in line.lower():
          if line not in projects:
            projects.append(line)

# Calculate total funding
total = 0
for p in projects:
  pl = p.lower()
  for f in funding:
    if f['Project_Name'].lower() == pl:
      total += int(f['Amount'])

print('__RESULT__:')
print(json.dumps({'total': total, 'projects_matched': len(projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)

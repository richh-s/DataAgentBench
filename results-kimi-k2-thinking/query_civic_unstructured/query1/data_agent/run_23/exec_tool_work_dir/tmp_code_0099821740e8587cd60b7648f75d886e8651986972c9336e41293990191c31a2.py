code = """import json, re

f = open(var_functions.query_db:30, 'r')
funding = json.load(f)
f.close()

d = open(var_functions.query_db:31, 'r')
docs = json.load(d)
d.close()

fund = {}
for r in funding:
  try:
    amt = int(r.get('Amount',0))
    if amt > 50000:
      name = r.get('Project_Name','').strip()
      if name:
        fund[name.lower()] = name
  except:
    continue

print('Funded >50K: ' + str(len(fund)))

projs = []
for doc in docs:
  t = doc.get('text','')
  start = t.find('Capital Improvement Projects (Design)')
  if start == -1:
    continue
  
  end = len(t)
  for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
    p = t.find(marker, start+50)
    if start < p < end:
      end = p
  
  section = t[start:end]
  lines = section.split('\n')
  
  for i in range(len(lines)):
    line = lines[i].strip()
    if not line or len(line) < 10:
      continue
    
    if 'cid:' in line or 'Updates:' in line or 'Project Schedule:' in line or 'Page' in line:
      continue
    
    if line.isupper() and len(line.split()) <= 3:
      continue
    
    if line[0].isupper() and len(line.split()) >= 2:
      good = False
      for j in range(i+1, min(i+4, len(lines))):
        nxt = lines[j].lower()
        if 'updates:' in nxt or 'project schedule:' in nxt:
          good = True
          break
      
      if good or 'Project' in line or 'Improvements' in line or 'Drainage' in line or 'Repairs' in line:
        if line not in projs:
          projs.append(line)

print('Design projects: ' + str(len(projs)))

matches = []
for p in projs:
  pk = p.lower()
  if pk in fund:
    matches.append(p)
  else:
    for fk in fund:
      if pk in fk or fk in pk:
        pw = set(pk.split())
        fw = set(fk.split())
        if len(pw.intersection(fw)) >= 2:
          matches.append(p)
          break

unique = list(set(matches))
print('Matches: ' + str(len(unique)))

result = len(unique)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)

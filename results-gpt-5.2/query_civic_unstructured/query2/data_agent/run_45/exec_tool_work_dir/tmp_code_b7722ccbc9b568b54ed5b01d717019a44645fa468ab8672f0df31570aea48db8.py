code = """import re, json

# load mongo results (may be a json file path)
obj = var_call_HBmVCfCZr2ZNgGuyYKXf7Yf3
if isinstance(obj, str):
    import pathlib
    p = pathlib.Path(obj)
    data = json.loads(p.read_text())
else:
    data = obj

projects = []
for rec in data:
    text = rec.get('text','')
    # focus on lines near 'completed' and with 'Park'
    for m in re.finditer(r'(?im)^\s*([A-Z][A-Za-z0-9&/\-\'\u2019\u2013\u2014\(\)\., ]*Park[^\n]{0,80})\n(?:.*\n){0,6}.*?\bcompleted\b[^\n]*\b(2022)\b', text):
        name = m.group(1).strip()
        name = re.sub(r'\s{2,}', ' ', name)
        projects.append({'Project_Name': name, 'year': 2022, 'filename': rec.get('filename')})

# Also catch 'Park ... completed <month> 2022'
for rec in data:
    text = rec.get('text','')
    for m in re.finditer(r'(?im)^\s*([A-Z][A-Za-z0-9&/\-\'\u2019\u2013\u2014\(\)\., ]*Park[^\n]{0,120})\n(?:.*\n){0,8}.*?\bcompleted\b[^\n]{0,60}\b(2022)\b', text):
        name = re.sub(r'\s{2,}', ' ', m.group(1).strip())
        projects.append({'Project_Name': name, 'year': 2022, 'filename': rec.get('filename')})

# de-duplicate by project name
seen=set(); uniq=[]
for p in projects:
    k=p['Project_Name']
    if k not in seen:
        seen.add(k); uniq.append(p)

print('__RESULT__:')
print(json.dumps(uniq))"""

env_args = {'var_call_tEb2QUBsxnJuTQFmoMn6ttnX': ['Funding'], 'var_call_iIVaQT6kP5WyVCoQ1lJTuaP0': ['civic_docs'], 'var_call_HBmVCfCZr2ZNgGuyYKXf7Yf3': 'file_storage/call_HBmVCfCZr2ZNgGuyYKXf7Yf3.json'}

exec(code, env_args)

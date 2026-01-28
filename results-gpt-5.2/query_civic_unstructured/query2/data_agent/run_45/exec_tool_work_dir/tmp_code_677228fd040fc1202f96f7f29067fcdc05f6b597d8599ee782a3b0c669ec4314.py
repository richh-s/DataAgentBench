code = """import re, json, pathlib

obj = var_call_HBmVCfCZr2ZNgGuyYKXf7Yf3
if isinstance(obj, str):
    data = json.loads(pathlib.Path(obj).read_text())
else:
    data = obj

projects = []
pattern = re.compile(r'(?im)^\s*([A-Z][A-Za-z0-9&/\-\u2019\u2013\u2014\(\)\., ]*Park[^\n]{0,120})\n(?:.*\n){0,8}.*?\bcompleted\b[^\n]{0,60}\b(2022)\b')

for rec in data:
    text = rec.get('text','')
    for m in pattern.finditer(text):
        name = re.sub(r'\s{2,}', ' ', m.group(1).strip())
        projects.append({'Project_Name': name, 'year': 2022, 'filename': rec.get('filename')})

seen=set(); uniq=[]
for p in projects:
    if p['Project_Name'] not in seen:
        seen.add(p['Project_Name']); uniq.append(p)

print('__RESULT__:')
print(json.dumps(uniq))"""

env_args = {'var_call_tEb2QUBsxnJuTQFmoMn6ttnX': ['Funding'], 'var_call_iIVaQT6kP5WyVCoQ1lJTuaP0': ['civic_docs'], 'var_call_HBmVCfCZr2ZNgGuyYKXf7Yf3': 'file_storage/call_HBmVCfCZr2ZNgGuyYKXf7Yf3.json'}

exec(code, env_args)

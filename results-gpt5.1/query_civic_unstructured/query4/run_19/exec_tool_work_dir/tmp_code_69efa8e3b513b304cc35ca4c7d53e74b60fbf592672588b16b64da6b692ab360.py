code = """import re, json, pandas as pd, pathlib

# Load full civic docs
path = var_call_NBHqGG6djrM5dO1twYnHOdsi
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]
text_all = '\n'.join(texts)

lines = text_all.split('\n')
projects = []
current_project = None

for line in lines:
    l = line.strip()
    if not l:
        continue
    if re.match(r'^[A-Z0-9].*(Project|Improvements|Repairs|Resurfacing|Drainage|Canyon|Park|Facility)', l):
        current_project = {'Project_Name': l, 'context': []}
        projects.append(current_project)
    elif current_project is not None:
        current_project['context'].append(l)

for p in projects:
    ctx = ' '.join(p['context'])
    m = re.search(r'(Begin Construction|Start|Project Schedule)[^\.]*?(Spring|Summer|Fall|Winter)?\s*-?,?\s*(20\d{2})', ctx, re.IGNORECASE)
    if m:
        season = m.group(2)
        year = m.group(3)
        if season:
            p['st'] = year + '-' + season.capitalize()
        else:
            p['st'] = year
    else:
        m2 = re.search(r'(Spring|Summer|Fall|Fall|Winter)\s+20(\d{2})', ctx, re.IGNORECASE)
        if m2:
            p['st'] = '20' + m2.group(2) + '-' + m2.group(1).capitalize()

spring_2022_projects = [p for p in projects if p.get('st') == '2022-Spring']

spring_project_names = [p['Project_Name'] for p in spring_2022_projects]

result = {
    'spring_2022_projects': spring_project_names,
    'count': len(spring_project_names)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NBHqGG6djrM5dO1twYnHOdsi': 'file_storage/call_NBHqGG6djrM5dO1twYnHOdsi.json', 'var_call_krn7MeS1mlZ43AbNoU9i9hBT': 'file_storage/call_krn7MeS1mlZ43AbNoU9i9hBT.json'}

exec(code, env_args)

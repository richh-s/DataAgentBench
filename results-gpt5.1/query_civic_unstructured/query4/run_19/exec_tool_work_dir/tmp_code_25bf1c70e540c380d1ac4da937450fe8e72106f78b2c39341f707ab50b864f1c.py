code = """import re, json, pandas as pd

# Load full civic docs
import pathlib, json as js
path = var_call_NBHqGG6djrM5dO1twYnHOdsi
with open(path, 'r') as f:
    civic_docs = js.load(f)

texts = [d['text'] for d in civic_docs]
text_all = '\n'.join(texts)

# Heuristic: A project line starts at line beginning and contains keywords like 'Project' or typical project phrases.
lines = text_all.split('\n')
projects = []
current_project = None

for line in lines:
    l = line.strip()
    if not l:
        continue
    # Detect project name lines - simplistic: capitalized words followed by 'Project' or 'Improvements' or 'Repairs' etc.
    if re.match(r'^[A-Z0-9].*(Project|Improvements|Repairs|Resurfacing|Drainage|Canyon|Park|Facility)', l):
        # Start new project
        current_project = {'Project_Name': l, 'context': []}
        projects.append(current_project)
    elif current_project is not None:
        current_project['context'].append(l)

# Extract start times from context using patterns like 'Begin Construction: <date>' or similar, or things that look like seasons/years
for p in projects:
    ctx = ' '.join(p['context'])
    # Look for patterns containing 'Begin Construction' or 'Start' etc
    m = re.search(r'(Begin Construction|Start|Project Schedule)[^\.]*?(Spring|Summer|Fall|Winter)?\s*-?,?\s*(20\d{2})', ctx, re.IGNORECASE)
    if m:
        season = m.group(2)
        year = m.group(3)
        if season:
            p['st'] = f"{year}-{season.capitalize()}"
        else:
            p['st'] = year
    else:
        # Also look for generic season-year like 'Spring 2022'
        m2 = re.search(r'(Spring|Summer|Fall|Winter)\s+20(\d{2})', ctx, re.IGNORECASE)
        if m2:
            p['st'] = f"20{m2.group(2)}-{m2.group(1).capitalize()}"

# Filter projects that started in Spring 2022
spring_2022_projects = [p for p in projects if p.get('st') == '2022-Spring']

spring_project_names = [p['Project_Name'] for p in spring_2022_projects]

result = {
    'spring_2022_projects': spring_project_names,
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NBHqGG6djrM5dO1twYnHOdsi': 'file_storage/call_NBHqGG6djrM5dO1twYnHOdsi.json', 'var_call_krn7MeS1mlZ43AbNoU9i9hBT': 'file_storage/call_krn7MeS1mlZ43AbNoU9i9hBT.json'}

exec(code, env_args)

code = """import re, json, pandas as pd

path_docs = var_call_VxNC30sVrc848Jc2xbezVvfo
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]
projects = []
for text in texts:
    lines = text.split('\n')
    for i, line in enumerate(lines):
        name = line.strip()
        if not name:
            continue
        if not re.search(r'Project|Improvements|Repairs|Park|Road|Storm|Drain|Bridge|Water|Signals|Playground|Facility|Median|Canyon|Crosswalk|Biofilter|Skate', name):
            continue
        context = '\n'.join(lines[i+1:i+8])
        m = re.search(r'Begin Construction:\s*([A-Za-z]+)\s*(\d{4})', context)
        if not m:
            continue
        month, year = m.group(1), m.group(2)
        st = year + '-' + month
        projects.append({'Project_Name': name, 'st': st})

spring_months = {'March', 'April', 'May'}
spring2022_projects = [p for p in projects if p['st'].startswith('2022-') and p['st'].split('-')[1] in spring_months]

unique = {}
for p in spring2022_projects:
    unique[p['Project_Name']] = p
spring2022_projects = list(unique.values())

funding = var_call_VVcrYx9JsKDhSyfUs4oZY5Mn

proj_names = {p['Project_Name'] for p in spring2022_projects}
fund_spring = [row for row in funding if row['Project_Name'] in proj_names]

total_funding = sum(int(row['Amount']) for row in fund_spring)
num_projects = len({row['Project_Name'] for row in fund_spring})

result = {'num_projects_started_spring_2022': num_projects, 'total_funding_spring_2022': total_funding}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_VxNC30sVrc848Jc2xbezVvfo': 'file_storage/call_VxNC30sVrc848Jc2xbezVvfo.json', 'var_call_VVcrYx9JsKDhSyfUs4oZY5Mn': 'file_storage/call_VVcrYx9JsKDhSyfUs4oZY5Mn.json'}

exec(code, env_args)

code = """import re, json, pandas as pd

path_docs = var_call_NH9TRMIi9mXbw6RuQJH8LI33
with open(path_docs, 'r') as f:
    docs = json.load(f)

texts = [d['text'] for d in docs]

project_pattern = re.compile('^(?P<name>.+?(Project|Improvements|Repairs|Repair|Maintenance|Biofilter|Benches and Arbors Renovation|Water Treatment Facility Phase 2|Water Treatment Facility|Canyon Road Traffic Study|Playground|Shade Structure|Storm Drainage Improvements|Storm Drain Repairs|Storm Drain Improvements))\\s*$', re.IGNORECASE)

projects = []
for text in texts:
    for line in text.split('\n'):
        line_stripped = line.strip()
        m = project_pattern.match(line_stripped)
        if m:
            name = m.group('name').strip()
            projects.append({'Project_Name': name})

project_names = sorted(set(p['Project_Name'] for p in projects))

proj_dates = {}
for text in texts:
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if ('Begin Construction' in line_clean) or ('Advertise' in line_clean) or ('Complete Design' in line_clean):
            context = '\n'.join(lines[max(0, i-5):i+1])
            for pname in project_names:
                if pname in context:
                    m1 = re.search('(Spring\\s*2022|2022[- ]Spring)', line_clean, re.IGNORECASE)
                    if m1 and pname not in proj_dates:
                        proj_dates[pname] = {'st': m1.group(1)}

spring2022_projects = list(proj_dates.keys())

funding = pd.DataFrame(var_call_EG2KUIK4OARbtijkvsxkXFnc)
funding['Amount'] = funding['Amount'].astype(int)

funding_spring = funding[funding['Project_Name'].isin(spring2022_projects)]

result = {
    'projects_started_spring_2022_count': int(funding_spring['Project_Name'].nunique()),
    'total_funding_spring_2022': int(funding_spring['Amount'].sum()),
    'projects': sorted(funding_spring['Project_Name'].unique().tolist())
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_NH9TRMIi9mXbw6RuQJH8LI33': 'file_storage/call_NH9TRMIi9mXbw6RuQJH8LI33.json', 'var_call_EG2KUIK4OARbtijkvsxkXFnc': 'file_storage/call_EG2KUIK4OARbtijkvsxkXFnc.json'}

exec(code, env_args)

code = """import re, json, pandas as pd

path_docs = var_call_uUG7DGtLoV6XHPagfZcMkhtr
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]

funding = pd.DataFrame(var_call_auNOjWAz2Q7H8bH30JHFr8Dt)
funding['Amount'] = funding['Amount'].astype(int)

project_names = set()
for text in texts:
    for line in text.split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        if re.search(r'(Project|Improvements|Repairs|Park|Road|Bridge|Drainage|Storm Drain)', line_stripped):
            if len(line_stripped.split()) <= 2:
                continue
            project_names.add(line_stripped)

projects_spring_2022 = set()
for text in texts:
    for pname in project_names:
        if pname in text:
            for m in re.finditer(re.escape(pname), text):
                start = max(0, m.start()-200)
                end = min(len(text), m.end()+200)
                context = text[start:end]
                if '2022' in context and any(mon in context for mon in ['March', 'April', 'May', 'Spring']):
                    projects_spring_2022.add(pname)

fund_spring = funding[funding['Project_Name'].isin(projects_spring_2022)]
result = {
    'num_projects_started_spring_2022': int(fund_spring['Project_Name'].nunique()),
    'total_funding_spring_2022': int(fund_spring['Amount'].sum())
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_uUG7DGtLoV6XHPagfZcMkhtr': 'file_storage/call_uUG7DGtLoV6XHPagfZcMkhtr.json', 'var_call_auNOjWAz2Q7H8bH30JHFr8Dt': 'file_storage/call_auNOjWAz2Q7H8bH30JHFr8Dt.json'}

exec(code, env_args)

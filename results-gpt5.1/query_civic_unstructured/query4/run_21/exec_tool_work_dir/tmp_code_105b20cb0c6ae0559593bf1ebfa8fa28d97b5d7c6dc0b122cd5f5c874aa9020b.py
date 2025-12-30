code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_uUG7DGtLoV6XHPagfZcMkhtr
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]

# Load funding
funding = pd.DataFrame(var_call_auNOjWAz2Q7H8bH30JHFr8Dt)
funding['Amount'] = funding['Amount'].astype(int)

# Very simple project extraction: assume each line that looks like a project title is a project name.
project_names = set()
for text in texts:
    for line in text.split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        # Heuristic: lines ending with 'Project' or containing 'Improvements' or 'Repairs' etc.
        if re.search(r'(Project|Improvements|Repairs|Park|Road|Bridge|Drainage|Storm Drain)', line_stripped):
            # avoid obviously non-title lines
            if len(line_stripped.split()) <= 2:
                continue
            project_names.add(line_stripped)

# Now we look for any occurrences of year 2022 and spring months near project names to infer start date.
projects_spring_2022 = set()
for text in texts:
    for pname in project_names:
        if pname in text:
            # search around occurrences
            for m in re.finditer(re.escape(pname), text):
                start = max(0, m.start()-200)
                end = min(len(text), m.end()+200)
                context = text[start:end]
                if '2022' in context:
                    # spring months
                    if any(mon in context for mon in ['March', 'April', 'May', 'Spring']):
                        projects_spring_2022.add(pname)

# Match with funding table by exact Project_Name
fund_spring = funding[funding['Project_Name'].isin(projects_spring_2022)]
result = {
    'num_projects_started_spring_2022': int(fund_spring['Project_Name'].nunique()),
    'total_funding_spring_2022': int(fund_spring['Amount'].sum())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uUG7DGtLoV6XHPagfZcMkhtr': 'file_storage/call_uUG7DGtLoV6XHPagfZcMkhtr.json', 'var_call_auNOjWAz2Q7H8bH30JHFr8Dt': 'file_storage/call_auNOjWAz2Q7H8bH30JHFr8Dt.json'}

exec(code, env_args)

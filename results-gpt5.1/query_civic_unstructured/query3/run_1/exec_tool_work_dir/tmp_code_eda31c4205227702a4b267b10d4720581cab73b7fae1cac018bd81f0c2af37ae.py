code = """import re, json
from pathlib import Path

# Load full civic docs result
path_docs = Path(var_call_rzxNukdDZfQ2KkjVUEVPATIs)
with open(path_docs, 'r') as f:
    docs = json.load(f)

# naive project extraction: lines that look like project titles
project_keywords = re.compile(r"(emergency|FEMA)", re.I)
projects = set()
for doc in docs:
    text = doc.get('text','')
    for line in text.split('\n'):
        if project_keywords.search(line):
            # clean line
            name = line.strip().strip('-').strip()
            if len(name) > 3:
                projects.add(name)

# Load funding table (already a list of records)
funding = var_call_LpcCzxjb4ZsKydfzWAcdcL4c

# match funding records whose Project_Name contains emergency/FEMA or matches extracted names loosely
results = []
for row in funding:
    pname = row['Project_Name']
    if project_keywords.search(pname):
        results.append({
            'Project_Name': pname,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']) if isinstance(row['Amount'], str) and row['Amount'].isdigit() else row['Amount'],
            'Status': None
        })

# deduplicate by Project_Name/Funding_Source/Amount
seen = set()
unique = []
for r in results:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'])
    if key not in seen:
        seen.add(key)
        unique.append(r)

out = json.dumps(unique)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rzxNukdDZfQ2KkjVUEVPATIs': 'file_storage/call_rzxNukdDZfQ2KkjVUEVPATIs.json', 'var_call_LpcCzxjb4ZsKydfzWAcdcL4c': 'file_storage/call_LpcCzxjb4ZsKydfzWAcdcL4c.json', 'var_call_lIFvh1lBVDy6RnCtOYNPanDD': ['civic_docs'], 'var_call_g9FfNpykuJJYJWazsGvPMLOK': ['Funding']}

exec(code, env_args)

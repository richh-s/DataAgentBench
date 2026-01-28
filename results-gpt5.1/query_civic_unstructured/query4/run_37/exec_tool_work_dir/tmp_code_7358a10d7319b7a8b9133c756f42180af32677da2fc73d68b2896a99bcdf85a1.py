code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
with open(var_call_YzvAo0AkQIJlVXmVBCFoYNd9, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_frE35AG2dXVdIIzZfCil2g5a)
funding['Amount'] = funding['Amount'].astype(int)

texts = ' '.join(d['text'] for d in civic_docs)

# crude heuristic: project names are funding Project_Name occurrences in text
projects = []
for name in funding['Project_Name'].unique():
    if name in texts:
        # search for a nearby "Begin Construction" or "Start" date containing 2022-Spring or March-May 2022
        pattern = re.compile(re.escape(name)+r"(.{0,200})", re.IGNORECASE)
        for m in pattern.finditer(texts):
            ctx = m.group(0)
            # look for date tokens
            if re.search(r"2022[- ]?(Spring|March|April|May)", ctx, re.IGNORECASE):
                projects.append(name)
                break

spring22_projects = sorted(set(projects))

sub = funding[funding['Project_Name'].isin(spring22_projects)]
result = {
    'projects_started_spring_2022_count': int(sub['Project_Name'].nunique()),
    'total_funding_spring_2022': int(sub['Amount'].sum()),
    'projects': spring22_projects
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_YzvAo0AkQIJlVXmVBCFoYNd9': 'file_storage/call_YzvAo0AkQIJlVXmVBCFoYNd9.json', 'var_call_frE35AG2dXVdIIzZfCil2g5a': 'file_storage/call_frE35AG2dXVdIIzZfCil2g5a.json'}

exec(code, env_args)

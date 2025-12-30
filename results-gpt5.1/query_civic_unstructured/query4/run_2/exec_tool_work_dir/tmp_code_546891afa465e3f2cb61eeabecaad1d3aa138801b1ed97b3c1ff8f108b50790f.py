code = """import re, json, pandas as pd
from pathlib import Path

path = Path(var_call_O9LaAXEpm1buZqQZ3oVdAosE)
with path.open() as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_jkJ2459nSv6WwDHMegLnE2YH)
funding['Amount'] = funding['Amount'].astype(int)

projects = []
for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    current_name = None
    for line in lines:
        if re.match(r'^[A-Z0-9].*(Project|Improvements|Repairs|Facility|Park|Study|Signs|Siren|Road|Drainage)$', line):
            current_name = line
        elif current_name:
            m = re.search(r'Begin Construction:\s*([A-Za-z0-9\-, ]+)', line)
            if not m:
                m = re.search(r'Start(?: Date)?:\s*([A-Za-z0-9\-, ]+)', line)
            if m:
                projects.append({'Project_Name': current_name, 'st': m.group(1).strip()})
                current_name = None

proj_df = pd.DataFrame(projects).drop_duplicates()

mask_2022 = proj_df['st'].str.contains('2022', case=False, na=False)
mask_spring_word = proj_df['st'].str.contains('Spring', case=False, na=False)
mask_months = proj_df['st'].str.contains('March|April|May|03|04|05', case=False, na=False)
proj_spring_2022 = proj_df[mask_2022 & (mask_spring_word | mask_months)]

merged = proj_spring_2022.merge(funding, on='Project_Name', how='inner')

result = {
    'projects_spring_2022': merged['Project_Name'].unique().tolist(),
    'count_projects_spring_2022': int(merged['Project_Name'].nunique()),
    'total_funding_spring_2022': int(merged['Amount'].sum())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_O9LaAXEpm1buZqQZ3oVdAosE': 'file_storage/call_O9LaAXEpm1buZqQZ3oVdAosE.json', 'var_call_jkJ2459nSv6WwDHMegLnE2YH': 'file_storage/call_jkJ2459nSv6WwDHMegLnE2YH.json'}

exec(code, env_args)

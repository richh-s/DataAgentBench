code = """import json, re, pandas as pd
from pathlib import Path

with open(var_call_gH6yrLHaT9EceBFgFwItcxCB, 'r') as f:
    civic_docs = json.load(f)

funding_records = var_call_8yOfDHTkI5FC7LD9KiMwsEMV
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

texts = '\n'.join(doc['text'] for doc in civic_docs)
lines = re.split(r'\n+', texts)

projects = []
for i, line in enumerate(lines):
    if 'Park' in line or 'park' in line:
        context_lines = lines[max(0, i-5):i+6]
        context = ' '.join(context_lines)
        if re.search(r'completed[^0-9]*2022', context, re.IGNORECASE):
            name = line.strip('• -')
            if name:
                projects.append(name)

unique_projects = list(dict.fromkeys(projects))

park_funding = 0
matched_projects = []
for pname in unique_projects:
    base = pname.split(' Project')[0]
    for fpn in funding_df['Project_Name']:
        if base and base in fpn:
            amt = int(funding_df.loc[funding_df['Project_Name'] == fpn, 'Amount'].iloc[0])
            park_funding += amt
            matched_projects.append({'civic_name': pname, 'funding_name': fpn, 'amount': amt})

result = {
    'total_park_funding_completed_2022': park_funding,
    'matches': matched_projects,
    'identified_projects': unique_projects
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_gH6yrLHaT9EceBFgFwItcxCB': 'file_storage/call_gH6yrLHaT9EceBFgFwItcxCB.json', 'var_call_8yOfDHTkI5FC7LD9KiMwsEMV': 'file_storage/call_8yOfDHTkI5FC7LD9KiMwsEMV.json'}

exec(code, env_args)

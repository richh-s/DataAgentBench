code = """import json, re, pandas as pd
from pathlib import Path

# Load full civic docs
with open(var_call_gH6yrLHaT9EceBFgFwItcxCB, 'r') as f:
    civic_docs = json.load(f)

funding_records = var_call_8yOfDHTkI5FC7LD9KiMwsEMV
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

texts = ' '.join(doc['text'] for doc in civic_docs)

# Very simple heuristic: extract lines that look like project entries mentioning parks and completed in 2022
lines = re.split(r'\n+', texts)
projects = []
for line in lines:
    if 'Park' in line or 'park' in line:
        # check nearby context for completion year 2022
        idx = lines.index(line)
        context = ' '.join(lines[max(0, idx-5):idx+6])
        if re.search(r'completed[^0-9]*2022', context, re.IGNORECASE):
            name = line.strip('\u2022 -')
            projects.append(name)

unique_projects = list(dict.fromkeys(projects))

# Match these names approximately to Funding.Project_Name by substring
park_funding = 0
matched_projects = []
for pname in unique_projects:
    for fpn in funding_df['Project_Name']:
        if pname.split(' Project')[0] in fpn:
            amt = int(funding_df.loc[funding_df['Project_Name'] == fpn, 'Amount'].iloc[0])
            park_funding += amt
            matched_projects.append({'civic_name': pname, 'funding_name': fpn, 'amount': amt})

result = {'total_park_funding_completed_2022': park_funding, 'matches': matched_projects, 'identified_projects': unique_projects}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_gH6yrLHaT9EceBFgFwItcxCB': 'file_storage/call_gH6yrLHaT9EceBFgFwItcxCB.json', 'var_call_8yOfDHTkI5FC7LD9KiMwsEMV': 'file_storage/call_8yOfDHTkI5FC7LD9KiMwsEMV.json'}

exec(code, env_args)

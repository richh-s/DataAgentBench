code = """import re, json, pandas as pd
from pathlib import Path
import json as _json

path_docs = Path(var_call_1Hq9LeBQZAzakZYT8jDdIACF)
with open(path_docs, 'r') as f:
    docs = _json.load(f)
texts = [d['text'] for d in docs]
full_text = '\n'.join(texts)

projects = []
current_project = None
for line in full_text.split('\n'):
    line = line.strip()
    if not line:
        continue
    if re.search(r"\b(Park|Playground)\b", line) and len(line.split()) < 10:
        current_project = {'Project_Name': line, 'raw': ''}
        projects.append(current_project)
        continue
    if current_project is not None:
        current_project['raw'] += ' ' + line

for p in projects:
    raw = p['raw']
    p['topic'] = 'park' if re.search(r"\bpark\b", raw, re.I) or re.search(r"\bPlayground\b", p['Project_Name']) else ''
    status = None
    if re.search(r"Construction was completed,? 2022", raw, re.I) or re.search(r"completed November 2022", raw, re.I):
        status = 'completed'
    elif re.search(r"Construction was completed,? 2023", raw, re.I):
        status = 'completed'
    elif re.search(r"currently under construction", raw, re.I):
        status = 'construction'
    if status:
        p['status'] = status
    m = re.search(r"Construction was completed,? ([A-Za-z]+ \d{4})", raw)
    if not m:
        m = re.search(r"completed (November 2022)", raw)
    p['et'] = m.group(1) if m else ''

park_2022 = [p for p in projects if p.get('topic')=='park' and p.get('status')=='completed' and '2022' in p.get('et','')]

path_fund = Path(var_call_ibPf7LgNwrB6qXSc0QnOzmX4)
with open(path_fund, 'r') as f:
    funding = _json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

matched_amounts = []
for p in park_2022:
    pname = p['Project_Name']
    m = fund_df[fund_df['Project_Name'].str.lower()==pname.lower()]
    if m.empty:
        m = fund_df[fund_df['Project_Name'].str.lower().str.contains(pname.lower())]
    if not m.empty:
        total = int(m['Amount'].sum())
        matched_amounts.append(total)

total_funding = int(sum(matched_amounts)) if matched_amounts else 0

result = {"total_funding_park_projects_completed_2022": total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1Hq9LeBQZAzakZYT8jDdIACF': 'file_storage/call_1Hq9LeBQZAzakZYT8jDdIACF.json', 'var_call_ibPf7LgNwrB6qXSc0QnOzmX4': 'file_storage/call_ibPf7LgNwrB6qXSc0QnOzmX4.json'}

exec(code, env_args)

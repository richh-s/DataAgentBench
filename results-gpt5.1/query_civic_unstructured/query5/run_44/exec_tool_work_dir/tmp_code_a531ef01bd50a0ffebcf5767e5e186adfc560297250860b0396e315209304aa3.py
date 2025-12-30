code = """import re, json, pandas as pd

path = var_call_pGSJRcC2kBfVhOWku4BNeQtq
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = [d.get('text','') for d in civic_docs]

projects = []
for text in texts:
    for line in text.split('\n'):
        if not line.strip():
            continue
        if ('Project' in line) or ('Improvements' in line) or ('Repairs' in line) or ('Warning Sirens' in line) or ('Storm Drain' in line) or ('Canyon' in line):
            projects.append(line.strip())

projects = sorted(set(projects))

DISASTER_KEYWORDS = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'Emergency', 'Disaster', 'Warning Sirens', 'Warning Signs', 'Storm Drain', 'Slope Repairs', 'Culvert Repairs', 'Retaining Wall', 'Bridge Repairs', 'Guardrail Replacement']

def is_disaster(name):
    n = name.lower()
    for kw in DISASTER_KEYWORDS:
        if kw.lower() in n:
            return True
    return False

projects_2022 = set()
for text in texts:
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if '2022' in line:
            for j in range(max(0, i-3), min(len(lines), i+4)):
                cand = lines[j].strip()
                if cand and (('Project' in cand) or ('Improvements' in cand) or ('Repairs' in cand) or ('Warning Sirens' in cand) or ('Storm Drain' in cand)):
                    projects_2022.add(cand)

funding = var_call_KblT4S5rbCHfovaP6AUwG4WE
if isinstance(funding, str) and funding.endswith('.json'):
    with open(funding, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding

fund_df = pd.DataFrame(funding_records)
fund_df['Project_Name_norm'] = fund_df['Project_Name'].str.strip()

start2022_disaster_funded = []
for proj in projects_2022:
    if not is_disaster(proj):
        continue
    for _, row in fund_df.iterrows():
        if (row['Project_Name_norm'] in proj) or (proj in row['Project_Name_norm']):
            start2022_disaster_funded.append(row.to_dict())

if start2022_disaster_funded:
    df_d = pd.DataFrame(start2022_disaster_funded).drop_duplicates(subset=['Funding_ID'])
    df_d['Amount'] = pd.to_numeric(df_d['Amount'])
    total = int(df_d['Amount'].sum())
else:
    total = 0

result = {"total_disaster_funding_started_2022": total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pGSJRcC2kBfVhOWku4BNeQtq': 'file_storage/call_pGSJRcC2kBfVhOWku4BNeQtq.json', 'var_call_KblT4S5rbCHfovaP6AUwG4WE': 'file_storage/call_KblT4S5rbCHfovaP6AUwG4WE.json', 'var_call_Z4TKzBugIFAq6cWU9kKrjPSa': ['civic_docs'], 'var_call_fYRTNna40YQlbi9AgmQnrldQ': ['Funding']}

exec(code, env_args)

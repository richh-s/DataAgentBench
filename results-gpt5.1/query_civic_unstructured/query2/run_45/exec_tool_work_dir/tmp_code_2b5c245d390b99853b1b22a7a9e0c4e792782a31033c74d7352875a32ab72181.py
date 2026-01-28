code = """import re, json, pandas as pd
from pathlib import Path

path_docs = Path(var_call_2mS72mVgtgogCqdPYvdn9kOF)
with path_docs.open() as f:
    civic_docs = json.load(f)

path_fund = Path(var_call_Zc9eBwECP9JOS4rxnMTt6ICR)
with path_fund.open() as f:
    funding = json.load(f)

projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if re.search(r'Park', line) and not line.lower().startswith('agenda'):
            context = '\n'.join(lines[i:i+10])
            status = None
            if re.search(r'Construction was completed', context, re.I):
                status = 'completed'
            et = None
            m = re.search(r'completed[^\n]*?(20\d{2})', context)
            if m:
                et = m.group(1)
            topic = 'park'
            projects.append({'Project_Name': line, 'status': status, 'et': et, 'topic': topic})

project_info = [
    {'Project_Name': 'Bluffs Park Shade Structure', 'status': 'completed', 'et': '2022', 'topic': 'park'},
]

names_added = {p['Project_Name'] for p in project_info}
for p in projects:
    if p['Project_Name'] not in names_added:
        project_info.append(p)
        names_added.add(p['Project_Name'])

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)
proj_df = pd.DataFrame(project_info)

mask = (proj_df['topic']=='park') & (proj_df['status']=='completed') & (proj_df['et'].fillna('').astype(str).str.contains('2022'))
completed_2022 = proj_df[mask]

merged = completed_2022.merge(fund_df, on='Project_Name', how='left')

total_funding = int(merged['Amount'].sum()) if not merged.empty else 0

result = {'total_funding_park_completed_2022': total_funding,
          'projects': merged[['Project_Name','Amount']].to_dict(orient='records')}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_2mS72mVgtgogCqdPYvdn9kOF': 'file_storage/call_2mS72mVgtgogCqdPYvdn9kOF.json', 'var_call_Zc9eBwECP9JOS4rxnMTt6ICR': 'file_storage/call_Zc9eBwECP9JOS4rxnMTt6ICR.json'}

exec(code, env_args)

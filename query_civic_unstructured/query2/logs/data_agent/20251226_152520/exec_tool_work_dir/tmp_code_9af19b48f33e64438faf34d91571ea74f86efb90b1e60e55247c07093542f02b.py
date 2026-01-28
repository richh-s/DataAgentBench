code = """import pandas as pd
import json
with open(var_call_bPcE3LudUpjycDhxee3F8lOo, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_r9xTUGs5GyNvgnOSuND8xnvo, 'r') as f:
    funding = json.load(f)
# For each line in each doc, look for completed park projects in 2022
park_projects_2022 = set()
for doc in civic_docs:
    text = doc['text'].lower()
    lines = text.split('\n')
    for line in lines:
        if 'park' in line and 'complete' in line and '2022' in line:
            pname = line.strip().replace('(cid:190)', '').replace('(cid:131)', '').replace(':', '').replace('\n', '').strip()
            park_projects_2022.add(pname)
        if 'completed' in line and '2022' in line and 'park' in line:
            pname = line.strip().replace(':', '').replace('\n', '').strip()
            park_projects_2022.add(pname)
known_names = ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Repair', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Trancas Canyon Park Slope Stabilization Project']
for kpn in known_names:
    park_projects_2022.add(kpn)
park_projects_2022 = {x for x in park_projects_2022 if x}
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)
funding_total = 0
match_names = []
for pname in park_projects_2022:
    matches = fund_df[fund_df['Project_Name'].str.lower().str.contains(pname.lower())]
    if not matches.empty:
        funding_total += matches['Amount'].sum()
        match_names.extend(matches['Project_Name'].tolist())
result = {'total_funding': int(funding_total), 'matched_projects': match_names}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_x5F47YMAEN3CzvCobsr4iAPz': ['civic_docs'], 'var_call_bPcE3LudUpjycDhxee3F8lOo': 'file_storage/call_bPcE3LudUpjycDhxee3F8lOo.json', 'var_call_r9xTUGs5GyNvgnOSuND8xnvo': 'file_storage/call_r9xTUGs5GyNvgnOSuND8xnvo.json'}

exec(code, env_args)

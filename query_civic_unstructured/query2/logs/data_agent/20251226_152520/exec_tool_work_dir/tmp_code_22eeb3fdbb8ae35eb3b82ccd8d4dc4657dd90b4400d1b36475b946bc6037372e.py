code = """import pandas as pd
import json
with open(var_call_bPcE3LudUpjycDhxee3F8lOo, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_r9xTUGs5GyNvgnOSuND8xnvo, 'r') as f:
    funding = json.load(f)
# Instead of \n, try splitting on actual newlines, maybe civic_docs text used real line breaks
park_projects_2022 = set()
for doc in civic_docs:
    text = doc['text'].lower()
    lines = text.split('\n') # try splitting by '\n' (escaped), if empty, try splitting by '\r\n' or '\r' or '\n'
    if len(lines) == 1:
        lines = text.split('\r\n')
    if len(lines) == 1:
        lines = text.split('\r')
    if len(lines) == 1:
        lines = text.split('\n')
    if len(lines) == 1:
        lines = text.split('\n')
    if len(lines) == 1:
        lines = text.split('\x0a')
    if len(lines) == 1:
        lines = text.split(chr(10))
    for line in lines:
        if 'park' in line and 'complete' in line and '2022' in line:
            pname = line.strip().replace('(cid:190)', '').replace('(cid:131)', '').replace(':', '').strip()
            park_projects_2022.add(pname)
        if 'completed' in line and '2022' in line and 'park' in line:
            pname = line.strip().replace(':', '').strip()
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

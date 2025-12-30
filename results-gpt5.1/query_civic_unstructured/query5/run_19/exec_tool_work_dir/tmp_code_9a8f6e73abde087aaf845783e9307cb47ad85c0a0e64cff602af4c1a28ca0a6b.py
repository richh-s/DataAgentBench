code = """import re, json, pandas as pd

path_civic = var_call_rivsLzTAoSXwdTdTRTtqBtKE
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

texts = [d.get('text','') for d in civic_docs]

projects = []
for text in texts:
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        if any(k in line for k in ['(FEMA', '(CalOES', '(CalJPIA', 'Disaster', 'disaster', 'Recovery']):
            name = line
            dates = re.findall(r'20\d{2}[^\s,;:.]*', line)
            st = dates[0] if dates else ''
            projects.append({'Project_Name': name, 'st': st})

proj_2022 = {p['Project_Name'] for p in projects if '2022' in p.get('st','') or '2022' in p['Project_Name']}

path_fund = var_call_eU7qpCwDnQJy26Pm2BNJS5Q8
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

fund_df['is_disaster'] = fund_df['Project_Name'].str.contains('\(FEMA|\(CalOES|\(CalJPIA', regex=True)

mask = fund_df['is_disaster'] & fund_df['Project_Name'].isin(proj_2022)

total = int(fund_df.loc[mask, 'Amount'].sum())

import json as json_mod
result = json_mod.dumps(total)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_rivsLzTAoSXwdTdTRTtqBtKE': 'file_storage/call_rivsLzTAoSXwdTdTRTtqBtKE.json', 'var_call_eU7qpCwDnQJy26Pm2BNJS5Q8': 'file_storage/call_eU7qpCwDnQJy26Pm2BNJS5Q8.json'}

exec(code, env_args)

code = """import json, re
import pandas as pd

def load_json_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_json_maybe_path(var_call_xVHLNlkl7NhAAKUdKQsBsvoQ)
docs = load_json_maybe_path(var_call_6neKI2D2f3w76geKxf2wQCYH)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

project_info = {}

for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text:
        continue
    idx = text.find('Disaster Recovery Projects')
    sub = text[idx:]
    mstop = re.search(r'\n\s*Capital Improvement Projects\b', sub)
    if mstop and mstop.start() > 0:
        sub = sub[:mstop.start()]

    for pname in fund_df['Project_Name']:
        if pname in project_info:
            continue
        if pname in sub:
            pos = sub.find(pname)
            window = sub[pos:pos+800]
            started_2022 = False
            if re.search(r'Begin\s+Construction\s*:\s*[^\n]*2022', window, flags=re.I):
                started_2022 = True
            if re.search(r'Begin\s*[:\-]\s*[^\n]*2022', window, flags=re.I):
                started_2022 = True
            if re.search(r'Start\s*[:\-]\s*[^\n]*2022', window, flags=re.I):
                started_2022 = True
            project_info[pname] = {'disaster': True, 'started_2022': started_2022}

started_2022_projects = [p for p, info in project_info.items() if info.get('disaster') and info.get('started_2022')]

sum_amount = fund_df.loc[fund_df['Project_Name'].isin(started_2022_projects), 'total_amount'].sum()

out = {
    'total_funding': int(sum_amount),
    'currency': 'USD',
    'project_count': int(len(started_2022_projects)),
    'projects': started_2022_projects
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xVHLNlkl7NhAAKUdKQsBsvoQ': 'file_storage/call_xVHLNlkl7NhAAKUdKQsBsvoQ.json', 'var_call_6neKI2D2f3w76geKxf2wQCYH': 'file_storage/call_6neKI2D2f3w76geKxf2wQCYH.json'}

exec(code, env_args)

code = """import json, re
import pandas as pd

path_f = var_call_FMwDEtUVPMSv1YXUZS5QvdAB
with open(path_f,'r',encoding='utf-8') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['total_amount'] = pd.to_numeric(df_f['total_amount'], errors='coerce').fillna(0)

path_d = var_call_HiIFfJEyctbf5jTngoAE41tK
with open(path_d,'r',encoding='utf-8') as f:
    docs = json.load(f)

projects = set(df_f['Project_Name'].dropna().astype(str).tolist())

def is_disaster_name(name):
    n = name.lower()
    return any(k in n for k in ['fema', 'caloes', 'caljpia', 'disaster'])

start_2022 = set()

for doc in docs:
    text = (doc.get('text','') or '').replace('\r','')
    lines = text.split('\n')
    current_section = None
    for i, line in enumerate(lines):
        l = line.strip()
        if re.search(r'^Disaster\s+Projects', l, flags=re.I):
            current_section = 'disaster'
        elif re.search(r'^Capital\s+Improvement\s+Projects', l, flags=re.I):
            current_section = 'capital'

        if (not l) or (len(l) > 200):
            continue

        hits = [p for p in projects if p in l]
        if not hits:
            continue

        window = '\n'.join(lines[i:i+60])
        for p in hits:
            disaster = (current_section == 'disaster') or is_disaster_name(p)
            if not disaster:
                continue
            if re.search(r'(Begin\s+(Construction|Design)|Start\w*|Construction\s+Start)[^\n]*2022', window, flags=re.I):
                start_2022.add(p)
            elif re.search(r'Begin\s+(Construction|Design)[^\n]*(Spring|Summer|Fall|Winter)\s+2022', window, flags=re.I):
                start_2022.add(p)

if len(start_2022) == 0:
    total = 0
else:
    total = int(df_f[df_f['Project_Name'].isin(start_2022)]['total_amount'].sum())

out = {
    'total_funding_disaster_projects_started_2022': total,
    'project_count': int(len(start_2022)),
    'projects': sorted(start_2022)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6DLUpRaIY1SPqmT30d4H3t5B': ['Funding'], 'var_call_0InSU5dLuPTxDHHjiypsT5e3': ['civic_docs'], 'var_call_FMwDEtUVPMSv1YXUZS5QvdAB': 'file_storage/call_FMwDEtUVPMSv1YXUZS5QvdAB.json', 'var_call_HiIFfJEyctbf5jTngoAE41tK': 'file_storage/call_HiIFfJEyctbf5jTngoAE41tK.json'}

exec(code, env_args)

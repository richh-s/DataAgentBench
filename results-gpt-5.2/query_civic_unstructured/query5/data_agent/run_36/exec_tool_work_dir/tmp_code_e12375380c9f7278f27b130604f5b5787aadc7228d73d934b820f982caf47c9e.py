code = """import json, re
import pandas as pd

# Load funding per project
path_f = var_call_FMwDEtUVPMSv1YXUZS5QvdAB
with open(path_f,'r',encoding='utf-8') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['total_amount'] = pd.to_numeric(df_f['total_amount'], errors='coerce').fillna(0)

# Load 2022 civic docs
path_d = var_call_HiIFfJEyctbf5jTngoAE41tK
with open(path_d,'r',encoding='utf-8') as f:
    docs = json.load(f)

projects = set(df_f['Project_Name'].dropna().astype(str).tolist())

# Find disaster projects and whether they started in 2022
# Heuristics:
# 1) Project must appear in a "Disaster" section OR name contains FEMA/CalOES/CalJPIA markers.
# 2) Start in 2022 if in the nearby schedule lines we see Begin Design/Begin Construction/Start with 2022

def is_disaster_name(name):
    n = name.lower()
    return any(k in n for k in ['fema', 'caloes', 'caljpia', 'disaster'])

start_2022 = set()

for doc in docs:
    text = doc.get('text','')
    # normalize bullets
    t = text.replace('\r','')

    # Split into lines for locality
    lines = t.split('\n')
    current_section = None
    for i, line in enumerate(lines):
        l = line.strip()
        if re.search(r'^Disaster\s+Projects', l, flags=re.I):
            current_section = 'disaster'
        elif re.search(r'^Capital\s+Improvement\s+Projects', l, flags=re.I):
            current_section = 'capital'

        # Check for any project names on this line (exact substring match)
        # Only test plausible header lines (not empty, not too long)
        if not l or len(l) > 200:
            continue
        hits = [p for p in projects if p in l]
        for p in hits:
            # determine if disaster
            disaster = (current_section=='disaster') or is_disaster_name(p)
            if not disaster:
                continue
            # search window of next 40 lines for start indicators with 2022
            window = '\n'.join(lines[i:i+60])
            if re.search(r'(Begin\s+(Construction|Design)|Start\w*|Construction\s+Start)[^\n]*2022', window, flags=re.I):
                start_2022.add(p)
            elif re.search(r'Begin\s+(Construction|Design)[^\n]*Spring\s+2022', window, flags=re.I):
                start_2022.add(p)
            elif re.search(r'Begin\s+(Construction|Design)[^\n]*Summer\s+2022', window, flags=re.I):
                start_2022.add(p)
            elif re.search(r'Begin\s+(Construction|Design)[^\n]*Fall\s+2022', window, flags=re.I):
                start_2022.add(p)
            elif re.search(r'Begin\s+(Construction|Design)[^\n]*Winter\s+2022', window, flags=re.I):
                start_2022.add(p)

# Sum funding for these projects
if len(start_2022)==0:
    total = 0
else:
    df_sel = df_f[df_f['Project_Name'].isin(start_2022)].copy()
    total = int(df_sel['total_amount'].sum())

out = {
    'total_funding_disaster_projects_started_2022': total,
    'project_count': int(len(start_2022)),
    'projects': sorted(list(start_2022))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6DLUpRaIY1SPqmT30d4H3t5B': ['Funding'], 'var_call_0InSU5dLuPTxDHHjiypsT5e3': ['civic_docs'], 'var_call_FMwDEtUVPMSv1YXUZS5QvdAB': 'file_storage/call_FMwDEtUVPMSv1YXUZS5QvdAB.json', 'var_call_HiIFfJEyctbf5jTngoAE41tK': 'file_storage/call_HiIFfJEyctbf5jTngoAE41tK.json'}

exec(code, env_args)

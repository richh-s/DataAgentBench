code = """import json, re
import pandas as pd

# load funding
funding_src = var_call_kAouEibCTtkVw0VUYXWS6GfF
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_src

# load docs
docs_src = var_call_FGFm4xF9ssYwbktsB4XKDTFZ
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)

# Build a fast lookup for project names
proj_names = fund_df['Project_Name'].dropna().astype(str).unique().tolist()

# Precompute lower text for docs
docs_texts = [d.get('text','') or '' for d in docs]

# Determine which projects are disaster-related and started in 2022
# Heuristic: project appears in a section titled 'Disaster Recovery Projects' or line contains '(FEMA'/'CalOES'/'CalJPIA' with disaster context.
# Start in 2022: within ~400 chars after occurrence we find 'Begin'/'Start' and '2022', or a schedule line with 'Begin Construction'/'Begin' and '2022'.

def is_disaster_context(window:str)->bool:
    w = window.lower()
    if 'disaster recovery project' in w or 'disaster recovery projects' in w:
        return True
    # common signals
    if 'fema' in w or 'caloes' in w or 'caljpia' in w:
        # but could be in capital list too; still disaster-related per hint
        return True
    if 'woolsey' in w or 'fire' in w or 'storm' in w or 'debris' in w:
        return True
    return False

def started_in_2022(window:str)->bool:
    w = window
    # look for explicit schedule begin/start lines containing 2022
    patterns = [r'(?i)\b(begin\s+construction|begin\s+work|begin|start(?:ed)?|commence(?:d)?)\b[^\n]{0,80}2022',
                r'(?i)2022[^\n]{0,80}\b(begin\s+construction|begin\s+work|begin|start(?:ed)?)\b']
    for p in patterns:
        if re.search(p, w):
            return True
    # also accept date formats like 2022-Spring etc near begin/start keywords
    if re.search(r'(?i)\b(begin\s+construction|begin|start)\b[^\n]{0,120}2022\s*[-–]\s*(spring|summer|fall|winter|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)', w):
        return True
    return False

qualifying = set()

for name in proj_names:
    name_l = name.lower()
    # search across docs
    for txt in docs_texts:
        t_l = txt.lower()
        idx = t_l.find(name_l)
        if idx == -1:
            continue
        # window around occurrence
        start = max(0, idx-600)
        end = min(len(txt), idx+1200)
        window = txt[start:end]
        # also consider earlier heading within window
        if not is_disaster_context(window):
            continue
        if started_in_2022(window):
            qualifying.add(name)
        # If found, no need to keep scanning same doc for this project
    
# If none found by window begin/start lines, fallback: any project name explicitly contains '2022' and is disaster-related
# and appears under disaster context anywhere.
if len(qualifying)==0:
    for name in proj_names:
        if '2022' not in name:
            continue
        for txt in docs_texts:
            if name.lower() in (txt.lower()):
                start = max(0, txt.lower().find(name.lower())-600)
                end = min(len(txt), txt.lower().find(name.lower())+1200)
                window = txt[start:end]
                if is_disaster_context(window):
                    qualifying.add(name)

qual_df = fund_df[fund_df['Project_Name'].isin(list(qualifying))]

total = int(qual_df['Amount'].sum())

out = {
    'total_funding': total,
    'currency': 'USD',
    'num_projects': int(qual_df['Project_Name'].nunique()),
    'projects': sorted(qual_df['Project_Name'].unique().tolist())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_kAouEibCTtkVw0VUYXWS6GfF': 'file_storage/call_kAouEibCTtkVw0VUYXWS6GfF.json', 'var_call_FGFm4xF9ssYwbktsB4XKDTFZ': 'file_storage/call_FGFm4xF9ssYwbktsB4XKDTFZ.json'}

exec(code, env_args)

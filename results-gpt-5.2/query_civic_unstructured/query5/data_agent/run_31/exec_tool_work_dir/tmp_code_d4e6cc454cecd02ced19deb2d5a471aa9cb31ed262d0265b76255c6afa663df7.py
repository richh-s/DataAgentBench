code = """import json, re
import pandas as pd

funding_src = var_call_kAouEibCTtkVw0VUYXWS6GfF
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_src

docs_src = var_call_FGFm4xF9ssYwbktsB4XKDTFZ
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)
proj_names = fund_df['Project_Name'].dropna().astype(str).unique().tolist()

docs_texts = [d.get('text','') or '' for d in docs]

def is_disaster_context(window: str) -> bool:
    w = window.lower()
    return (
        ('disaster recovery project' in w) or ('disaster recovery projects' in w) or
        ('fema' in w) or ('caloes' in w) or ('caljpia' in w) or
        ('woolsey' in w) or ('fire' in w) or ('debris' in w) or
        ('storm' in w)
    )

def started_in_2022(window: str) -> bool:
    pats = [
        r'(?i)\b(begin\s+construction|begin\s+work|begin|start(?:ed)?|commence(?:d)?)\b[^\n]{0,80}2022',
        r'(?i)2022[^\n]{0,80}\b(begin\s+construction|begin\s+work|begin|start(?:ed)?)\b'
    ]
    for p in pats:
        if re.search(p, window):
            return True
    if re.search(r'(?i)\b(begin\s+construction|begin|start)\b[^\n]{0,120}2022\s*[-\u2013]\s*(spring|summer|fall|winter)', window):
        return True
    return False

qualifying = set()

for name in proj_names:
    name_l = name.lower()
    for txt in docs_texts:
        t_l = txt.lower()
        idx = t_l.find(name_l)
        if idx == -1:
            continue
        start = max(0, idx - 600)
        end = min(len(txt), idx + 1200)
        window = txt[start:end]
        if not is_disaster_context(window):
            continue
        if started_in_2022(window):
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

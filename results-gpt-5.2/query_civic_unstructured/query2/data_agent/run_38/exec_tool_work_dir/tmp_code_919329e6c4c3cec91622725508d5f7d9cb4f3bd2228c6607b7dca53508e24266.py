code = """import json, re, pandas as pd

# load civic docs
civic_src = var_call_dihoTiXYyBaE6uMNg3idDH2s
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# load funding
fund_src = var_call_XkdifSp8ULCYsZ5zhen5qjPO
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_src

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)

proj_names = set(fund_df['Project_Name'].dropna().astype(str).tolist())
sorted_names = sorted(proj_names, key=len, reverse=True)

completed_2022_parks = set()

# regex patterns (avoid literal newlines in regex char class)
patterns = [
    r'completed[^\\r\\n]{0,120}2022',
    r'construction was completed[^\\r\\n]{0,120}2022',
    r'was completed[^\\r\\n]{0,120}2022',
]

for doc in civic_docs:
    text = doc.get('text','') or ''
    tl = text.lower()
    if 'completed' not in tl:
        continue
    for name in sorted_names:
        if not name:
            continue
        idx = text.find(name)
        if idx < 0:
            continue
        window = text[max(0, idx-500): min(len(text), idx+1200)]
        wl = window.lower()
        park_related = (('park' in name.lower()) or ('playground' in name.lower()) or ('skate' in name.lower()) or bool(re.search(r'\bpark\b|\bplayground\b|\bskate\b', wl)))
        if not park_related:
            continue
        comp_2022 = any(re.search(pat, wl, flags=re.IGNORECASE) for pat in patterns)
        if comp_2022:
            completed_2022_parks.add(name)

sel = fund_df[fund_df['Project_Name'].isin(completed_2022_parks)]
total = int(sel['Amount'].sum())

out = {
    'total_funding': total,
    'project_count': int(sel['Project_Name'].nunique()),
    'projects': sorted(sel['Project_Name'].unique().tolist())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hu7GlRU1DsdOd4UDUxLjY9GF': ['Funding'], 'var_call_ChrD81iyTicuslPx6JYjPPIP': ['civic_docs'], 'var_call_dihoTiXYyBaE6uMNg3idDH2s': 'file_storage/call_dihoTiXYyBaE6uMNg3idDH2s.json', 'var_call_XkdifSp8ULCYsZ5zhen5qjPO': 'file_storage/call_XkdifSp8ULCYsZ5zhen5qjPO.json'}

exec(code, env_args)

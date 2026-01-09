code = """import json
import re
import pandas as pd

funding_src = var_call_MATmXTyx00IPkd9ngwSRe6T9
if isinstance(funding_src, str):
    with open(funding_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_src

docs_src = var_call_qgSlxLkDKo4GNQDWKtbKc6x8
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip())

exclude = set([
    'capital improvement projects (design)',
    'capital improvement projects (construction)',
    'capital improvement projects (not started)',
    'disaster recovery projects (design)',
    'disaster recovery projects (construction)',
    'disaster recovery projects (not started)',
    'recommended action',
    'discussion',
    'project updates',
    'project schedule',
    'estimated schedule',
    'project description',
    'updates'
])

proj_name_re = re.compile(r"^(?!\s)([A-Za-z0-9].{2,120}?)\s*$")
park_completed_2022 = set()

for d in docs:
    text = d.get('text') or ''
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        m = proj_name_re.match(ln)
        if not m:
            continue
        name = norm(m.group(1))
        if name.lower() in exclude:
            continue
        window = "\n".join(lines[i:i+25]).lower()
        if ('park' not in name.lower()) and (' park' not in window) and ('playground' not in window) and ('skate park' not in window):
            continue
        if ('completed' in window) and ('2022' in window):
            park_completed_2022.add(name)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)
fund_df['Project_Name'] = fund_df['Project_Name'].map(norm)

matched = fund_df[fund_df['Project_Name'].isin(park_completed_2022)]

out = {
    'total_funding': int(matched['Amount'].sum()),
    'num_projects_matched': int(matched['Project_Name'].nunique()),
    'projects': sorted(matched['Project_Name'].unique().tolist())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MATmXTyx00IPkd9ngwSRe6T9': 'file_storage/call_MATmXTyx00IPkd9ngwSRe6T9.json', 'var_call_qgSlxLkDKo4GNQDWKtbKc6x8': 'file_storage/call_qgSlxLkDKo4GNQDWKtbKc6x8.json'}

exec(code, env_args)

code = """import json, re, pandas as pd

funding_path = var_call_FT2hoBbHQtKAyB2AQwXp0ILh
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

paths = [var_call_4sLbDZbrcMzakYjtHFhooCkR, var_call_T2kSqayaM7aWQK8JXxTv3PZM]
all_docs = []
for p in paths:
    with open(p, 'r', encoding='utf-8') as f:
        all_docs.extend(json.load(f))
docs_df = pd.DataFrame(all_docs).drop_duplicates(subset=['filename'])
texts = docs_df['text'].fillna('').tolist()

proj_started_2022 = set()

def extract_disaster_section(text):
    m = re.search(r'Disaster Recovery Projects.*?(?=\n\s*Capital Improvement Projects|\Z)', text, flags=re.IGNORECASE|re.DOTALL)
    return m.group(0) if m else ''

begin_pat = re.compile(r'\n([A-Z0-9][^\n]{2,120}?)\n(?:.*\n){0,25}?\bBegin\s+Construction\s*:\s*[^\n]*\b2022\b', re.IGNORECASE)
start_pat = re.compile(r'\n([A-Z0-9][^\n]{2,120}?)\n(?:.*\n){0,25}?\b(Begin|Start)\b[^\n]*:\s*[^\n]*\b2022\b', re.IGNORECASE)

for t in texts:
    sec = extract_disaster_section(t)
    if not sec:
        continue
    for pat in (begin_pat, start_pat):
        for m in pat.finditer(sec):
            name = m.group(1).strip()
            name = re.sub(r'^[\-•\s]+', '', name).strip()
            if re.search(r'Projects|Project Schedule|Updates|DISCUSSION|RECOMMENDED ACTION', name, re.IGNORECASE):
                continue
            proj_started_2022.add(name)

started_df = pd.DataFrame({'Project_Name': sorted(proj_started_2022)})
joined = started_df.merge(fund_df, on='Project_Name', how='left')
joined['total_amount'] = joined['total_amount'].fillna(0).astype(int)

total = int(joined['total_amount'].sum())

out = {
    'total_funding_disaster_projects_started_2022': total,
    'matched_projects_count': int((joined['total_amount']>0).sum()),
    'identified_projects_count': int(len(joined)),
    'matched_projects': joined.loc[joined['total_amount']>0, ['Project_Name','total_amount']].sort_values('Project_Name').to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FT2hoBbHQtKAyB2AQwXp0ILh': 'file_storage/call_FT2hoBbHQtKAyB2AQwXp0ILh.json', 'var_call_4sLbDZbrcMzakYjtHFhooCkR': 'file_storage/call_4sLbDZbrcMzakYjtHFhooCkR.json', 'var_call_T2kSqayaM7aWQK8JXxTv3PZM': 'file_storage/call_T2kSqayaM7aWQK8JXxTv3PZM.json', 'var_call_FnijSSj6nh8yvZ54zK4z4Cm3': ['Funding']}

exec(code, env_args)

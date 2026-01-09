code = """import json, re, pandas as pd

civic_src = var_call_RGCkESsm5awQiYuc9YRmgOGc
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    civic_docs = json.load(open(civic_src,'r',encoding='utf-8'))
else:
    civic_docs = civic_src

fund_src = var_call_q2Vs19CbfEIddwfQrj4SQtyA
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    funding = json.load(open(fund_src,'r',encoding='utf-8'))
else:
    funding = fund_src

fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

skip_re = re.compile(r'^(Public Works|Agenda|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION|DISCUSSION|Capital Improvement Projects|Disaster Recovery Projects|Page \d+ of \d+|Agenda Item)', re.I)

projects = []
for d in civic_docs:
    lines = [ln.strip() for ln in d.get('text','').splitlines()]
    for idx, ln in enumerate(lines):
        if not ln or len(ln) > 120 or skip_re.match(ln):
            continue
        block = "\\n".join(lines[idx:idx+40])
        if re.search(r'Project Schedule', block, re.I) or re.search(r'Estimated Schedule', block, re.I):
            m = re.search(r'Begin (?:Construction|construction)\s*:\s*([^\n\r]+)', block)
            st = m.group(1).strip().strip('.') if m else None
            projects.append({'Project_Name': ln, 'st': st})

proj_df = pd.DataFrame(projects).drop_duplicates()
if proj_df.empty:
    out = {'projects_started_spring_2022': 0, 'total_funding': 0, 'projects': []}
else:
    spring_mask = proj_df['st'].fillna('').str.contains(r'(?i)spring\s*,?\s*2022|2022\s*-\s*spring|2022\s*spring', regex=True)
    started = proj_df.loc[spring_mask, ['Project_Name','st']].copy()
    if started.empty:
        out = {'projects_started_spring_2022': 0, 'total_funding': 0, 'projects': []}
    else:
        merged = started.merge(fund_df, on='Project_Name', how='left') if not fund_df.empty else started.assign(total_amount=0)
        if 'total_amount' not in merged.columns:
            merged['total_amount'] = 0
        merged['total_amount'] = merged['total_amount'].fillna(0).astype(int)
        out = {
            'projects_started_spring_2022': int(started.shape[0]),
            'total_funding': int(merged['total_amount'].sum()),
            'projects': merged[['Project_Name','st','total_amount']].to_dict('records')
        }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3yumKNq3xfmLwDpRS5PqJRxw': ['Funding'], 'var_call_gznRid3cvqOesy5arqDDcNkg': ['civic_docs'], 'var_call_RGCkESsm5awQiYuc9YRmgOGc': 'file_storage/call_RGCkESsm5awQiYuc9YRmgOGc.json', 'var_call_q2Vs19CbfEIddwfQrj4SQtyA': 'file_storage/call_q2Vs19CbfEIddwfQrj4SQtyA.json'}

exec(code, env_args)

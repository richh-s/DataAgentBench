code = """import json, re, pandas as pd

# Load civic docs
civic_src = var_call_RGCkESsm5awQiYuc9YRmgOGc
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# Load funding aggregation
fund_src = var_call_q2Vs19CbfEIddwfQrj4SQtyA
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_src

fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Parse projects + start dates from text (heuristic for Malibu agenda format)
projects = []
for d in civic_docs:
    text = d.get('text','')
    # split by lines
    lines = [ln.strip() for ln in text.splitlines()]
    i = 0
    while i < len(lines):
        ln = lines[i]
        # project name candidates: non-empty, not bullet headers, limited length
        if ln and len(ln) <= 120 and not re.match(r'^(Public Works|Agenda|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION|DISCUSSION|Capital Improvement Projects|Disaster Recovery Projects|Page \d+ of \d+|Agenda Item)', ln, re.I):
            # look ahead for 'Project Schedule' block within next 25 lines
            block = '\n'.join(lines[i:i+40])
            if re.search(r'Project Schedule', block, re.I) or re.search(r'Estimated Schedule', block, re.I):
                # extract begin construction/advertise etc
                m = re.search(r'Begin (?:Construction|construction)\s*:\s*([^\n\r]+)', block)
                if m:
                    st = m.group(1).strip().strip('.')
                else:
                    # sometimes 'Advertise: Spring 2022' could be start proxy; but question asks started in Spring 2022
                    st = None
                projects.append({'Project_Name': ln, 'st': st})
        i += 1

proj_df = pd.DataFrame(projects).drop_duplicates()

# Determine started in Spring 2022: st contains Spring 2022 OR 2022-Spring OR Spring, 2022
spring_mask = proj_df['st'].fillna('').str.contains(r'(?i)spring\s*,?\s*2022|2022\s*-\s*spring|2022\s*spring')
started = proj_df.loc[spring_mask, ['Project_Name','st']].copy()

# Join to funding
if started.empty or fund_df.empty:
    result = {'projects_started_spring_2022': int(started.shape[0]), 'total_funding': 0, 'projects': started.to_dict('records')}
else:
    merged = started.merge(fund_df, on='Project_Name', how='left')
    merged['total_amount'] = merged['total_amount'].fillna(0).astype(int)
    total_funding = int(merged['total_amount'].sum())
    result = {
        'projects_started_spring_2022': int(started.shape[0]),
        'total_funding': total_funding,
        'projects': merged[['Project_Name','st','total_amount']].to_dict('records')
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3yumKNq3xfmLwDpRS5PqJRxw': ['Funding'], 'var_call_gznRid3cvqOesy5arqDDcNkg': ['civic_docs'], 'var_call_RGCkESsm5awQiYuc9YRmgOGc': 'file_storage/call_RGCkESsm5awQiYuc9YRmgOGc.json', 'var_call_q2Vs19CbfEIddwfQrj4SQtyA': 'file_storage/call_q2Vs19CbfEIddwfQrj4SQtyA.json'}

exec(code, env_args)

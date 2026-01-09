code = """import json, pandas as pd, re

with open(var_call_FT2hoBbHQtKAyB2AQwXp0ILh, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

with open(var_call_DewMycyZ7empJ9BQW3GMz5ep, 'r', encoding='utf-8') as f:
    docs = json.load(f)

started = set()
pat = re.compile(r"(?is)\n([^\n]{2,150})\n(?:.*\n){0,20}?Begin Construction\s*:\s*[^\n]*2022")
for d in docs:
    text = d.get('text','')
    for m in pat.finditer(text):
        name = m.group(1).strip()
        span_start = max(0, m.start()-800)
        context = text[span_start:m.start()]
        if re.search(r"(?i)Disaster", context) or re.search(r"(?i)\b(FEMA|CalOES|CalJPIA)\b", name):
            name = re.sub(r"^[\-•\s]+", "", name).strip()
            if not re.search(r"(?i)Project Schedule|Updates|Projects", name):
                started.add(name)

started_df = pd.DataFrame({'Project_Name': sorted(started)})
joined = started_df.merge(fund_df, on='Project_Name', how='left')
joined['total_amount'] = joined['total_amount'].fillna(0).astype(int)

total = int(joined['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'total': total, 'matched_projects': joined[joined.total_amount>0][['Project_Name','total_amount']].to_dict(orient='records'), 'identified_projects': sorted(started)}))"""

env_args = {'var_call_FT2hoBbHQtKAyB2AQwXp0ILh': 'file_storage/call_FT2hoBbHQtKAyB2AQwXp0ILh.json', 'var_call_4sLbDZbrcMzakYjtHFhooCkR': 'file_storage/call_4sLbDZbrcMzakYjtHFhooCkR.json', 'var_call_T2kSqayaM7aWQK8JXxTv3PZM': 'file_storage/call_T2kSqayaM7aWQK8JXxTv3PZM.json', 'var_call_FnijSSj6nh8yvZ54zK4z4Cm3': ['Funding'], 'var_call_DewMycyZ7empJ9BQW3GMz5ep': 'file_storage/call_DewMycyZ7empJ9BQW3GMz5ep.json'}

exec(code, env_args)

code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_Fwfwondyax8aJgQAxiu1Z0wz)
rows = json.loads(path.read_text())

data = []
for r in rows:
    info = r['Patents_info']
    # extract assignee (simple heuristic around 'owned by' or 'assigned to' or 'holds the')
    assignee = None
    if 'owned by ' in info:
        assignee = info.split('owned by ')[1].split(' and')[0].strip('. ')
    elif 'assigned to ' in info:
        assignee = info.split('assigned to ')[1].split(' and')[0].strip('. ')
    elif 'holds the' in info:
        # pattern 'UNIV CALIFORNIA holds the TW patent filing'
        assignee = info.split(' holds')[0].split('.')[-1].strip()
    if not assignee or assignee == 'UNIV CALIFORNIA':
        continue
    cits = json.loads(r['citation']) if r['citation'] else []
    for c in cits:
        pub = c.get('publication_number')
        if not pub:
            continue
        data.append({'citing_assignee': assignee, 'cited_pub': pub, 'cpc_json': r['cpc']})

# dedupe
df = pd.DataFrame(data).drop_duplicates()

# collect unique CPC codes attached to these citing patents (primary subclasses = first=true)
records = []
for _, row in df.iterrows():
    cpc_list = json.loads(row['cpc_json']) if row['cpc_json'] else []
    prim_codes = sorted({c['code'] for c in cpc_list if c.get('first')})
    for code in prim_codes:
        records.append({'citing_assignee': row['citing_assignee'], 'cpc_code': code})

cpc_df = pd.DataFrame(records).drop_duplicates()

# prepare list of unique CPC symbols to look up definitions
unique_codes = sorted(cpc_df['cpc_code'].unique().tolist()) if not cpc_df.empty else []

result = {
  'assignee_cpc_pairs': cpc_df.to_dict(orient='records'),
  'unique_cpc_codes': unique_codes
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_ouQvxxEZDd7K4vYQsF91JoEf': [], 'var_call_Fwfwondyax8aJgQAxiu1Z0wz': 'file_storage/call_Fwfwondyax8aJgQAxiu1Z0wz.json'}

exec(code, env_args)

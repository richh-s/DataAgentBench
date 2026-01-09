code = """import json, re
import pandas as pd

# Load large result
path = var_call_GP3q5hBbWt1xhMg7tN2QF7Xe
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

rows = []
for r in recs:
    pi = r.get('Patents_info') or ''
    # citing assignee: pattern 'belonging to X' in Patents_info
    m = re.search(r'belonging to ([^\n\.]+)', pi)
    assignee = m.group(1).strip() if m else None
    if not assignee:
        continue
    if assignee.upper() == 'UNIV CALIFORNIA':
        continue

    # determine if citation includes UNIV CALIFORNIA (already filtered in SQL)
    cpc_text = r.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_text)
    except Exception:
        cpcs = []

    # primary CPC: where first==true; else take first code
    primary_codes = [c.get('code') for c in cpcs if isinstance(c, dict) and c.get('first') is True and c.get('code')]
    if not primary_codes:
        primary_codes = [c.get('code') for c in cpcs if isinstance(c, dict) and c.get('code')]
        primary_codes = primary_codes[:1]

    for code in primary_codes:
        subclass = code
        # reduce to subclass: first 4 chars letter+2digits+letter then digits after? subclass like A61P
        m2 = re.match(r'^([A-HY][0-9]{2}[A-Z])', subclass)
        subclass4 = m2.group(1) if m2 else None
        if subclass4:
            rows.append({'citing_assignee': assignee, 'cpc_subclass': subclass4})


df = pd.DataFrame(rows).dropna().drop_duplicates()

# output list of unique subclasses to query titles
subclasses = sorted(df['cpc_subclass'].unique().tolist())
print('__RESULT__:')
print(json.dumps({'pairs': df.to_dict(orient='records'), 'subclasses': subclasses}))"""

env_args = {'var_call_5JRPmd7DqQz8QNCSKdFQGVw6': [], 'var_call_GP3q5hBbWt1xhMg7tN2QF7Xe': 'file_storage/call_GP3q5hBbWt1xhMg7tN2QF7Xe.json'}

exec(code, env_args)

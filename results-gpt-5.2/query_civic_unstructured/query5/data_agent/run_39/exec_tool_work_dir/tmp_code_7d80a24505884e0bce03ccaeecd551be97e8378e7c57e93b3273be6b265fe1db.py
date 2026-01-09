code = """import json, re, pandas as pd

# Load docs with disaster section
src = var_call_ap71z49cYr1RQ54nqmrvOar2
if isinstance(src, str) and src.endswith('.json'):
    with open(src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = src

# Load funding totals per project
fund_src = var_call_0mwA7xPw4fLVn1WGDZnXmja6
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund_rows = json.load(f)
else:
    fund_rows = fund_src
fund_df = pd.DataFrame(fund_rows)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

started = set()

# Simple robust scan: within each doc, find occurrences of 'Disaster Recovery Projects' then extract nearby 'Begin Construction: ...2022' lines; take preceding non-empty line as project name.
for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text and 'Disaster recovery projects' not in text:
        continue
    lines = text.splitlines()
    in_disaster = False
    prev_nonempty = ''
    for ln in lines:
        s = ln.strip()
        if re.search(r'Disaster Recovery Projects', s, flags=re.I):
            in_disaster = True
            prev_nonempty = ''
            continue
        if in_disaster and re.search(r'^Capital Improvement Projects', s, flags=re.I):
            in_disaster = False
        if not s:
            continue
        if in_disaster:
            if re.search(r'Begin\s+Construction\s*:\s*.*2022', s, flags=re.I):
                # project name is prev_nonempty (skip if it's a label)
                if prev_nonempty and not re.search(r'(Project Schedule|Updates|Estimated Schedule|Project Description)', prev_nonempty, flags=re.I):
                    started.add(prev_nonempty)
        prev_nonempty = s

matched = {name: int(fund_map.get(name,0)) for name in started if name in fund_map}

total = int(sum(matched.values()))

out = {'total_funding_usd': total, 'projects_started_2022': sorted(list(matched.keys())), 'num_projects': len(matched)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AcRQ6OtasNM9MGboFNwd7qNq': ['civic_docs'], 'var_call_XQWZ4a4IsKyRlEwdyWL5OCqE': ['Funding'], 'var_call_jroWgJMT8F7cCBC0f826dx5I': 'file_storage/call_jroWgJMT8F7cCBC0f826dx5I.json', 'var_call_0mwA7xPw4fLVn1WGDZnXmja6': 'file_storage/call_0mwA7xPw4fLVn1WGDZnXmja6.json', 'var_call_ap71z49cYr1RQ54nqmrvOar2': 'file_storage/call_ap71z49cYr1RQ54nqmrvOar2.json'}

exec(code, env_args)

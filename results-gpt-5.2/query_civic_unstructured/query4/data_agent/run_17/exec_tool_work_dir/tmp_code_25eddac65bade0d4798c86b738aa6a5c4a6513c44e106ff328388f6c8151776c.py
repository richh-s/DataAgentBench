code = """import json, re
import pandas as pd

with open(var_call_GcV2Cqql11NSEN3ZlEEH8fYP, 'r', encoding='utf-8') as f:
    docs = json.load(f)

with open(var_call_B8i9KzeWghvmclogSXmtIm7J, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

start_re = re.compile(r'(?im)^\s*(?:Begin\s+Construction|Award\s+Contract\s+and\s+Begin\s+Construction|Begin\s+Design|Start(?:\s+Construction)?|Construction\s+Start)\s*:\s*([^\n\r]+)')

spring_phrase_re = re.compile(r'(?i)Spring[^\n\r]*2022')

exclude_line = re.compile(r'(?i)^(capital improvement projects|disaster projects|disaster recovery projects|project schedule|estimated schedule|updates|project description)$')

projects = set()

for d in docs:
    lines = d.get('text','').splitlines()
    for i, line in enumerate(lines):
        m = start_re.match(line)
        if not m:
            continue
        if not spring_phrase_re.search(m.group(1) or ''):
            continue
        for j in range(i-1, max(-1, i-40), -1):
            s = lines[j].strip()
            if not s or ':' in s:
                continue
            if len(s) < 5 or len(s) > 120:
                continue
            if exclude_line.match(s):
                continue
            if re.match(r'(?i)^(page\s+\d+\s+of\s+\d+|agenda item)', s):
                continue
            projects.add(s)
            break

proj_list = sorted(projects)
joined = fund_df[fund_df['Project_Name'].isin(proj_list)] if proj_list else fund_df.iloc[0:0]

total_funding = int(joined['total_amount'].sum()) if not joined.empty else 0

out = {'count': int(len(proj_list)), 'total_funding_usd': total_funding, 'projects': proj_list}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5FRoyKoaGE92xUhwFnjuJHFV': 'file_storage/call_5FRoyKoaGE92xUhwFnjuJHFV.json', 'var_call_B8i9KzeWghvmclogSXmtIm7J': 'file_storage/call_B8i9KzeWghvmclogSXmtIm7J.json', 'var_call_C0VOOFKGG33dRWa4HHxU2gC1': {'count': 0, 'total_funding_usd': 0, 'projects': []}, 'var_call_GcV2Cqql11NSEN3ZlEEH8fYP': 'file_storage/call_GcV2Cqql11NSEN3ZlEEH8fYP.json'}

exec(code, env_args)

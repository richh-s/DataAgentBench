code = """import json, re
import pandas as pd

# Load docs
with open(var_call_5FRoyKoaGE92xUhwFnjuJHFV, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding sums
with open(var_call_B8i9KzeWghvmclogSXmtIm7J, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Find lines like 'Begin Construction: Spring 2022' and take nearest preceding project title line.
begin_re = re.compile(r'(?im)^\s*Begin\s+Construction\s*:\s*Spring\s+2022\b')

def extract_projects_started_spring2022(text):
    projects = []
    for m in begin_re.finditer(text):
        start_idx = m.start()
        # look back up to 40 lines
        prefix = text[:start_idx].splitlines()[-80:]
        # choose last plausible title line
        for line in reversed(prefix):
            s = line.strip()
            if not s:
                continue
            if ':' in s:
                continue
            if len(s) < 5 or len(s) > 120:
                continue
            if re.match(r'(?i)^(capital improvement projects|disaster recovery projects|project schedule|estimated schedule|updates|project description)$', s):
                continue
            if re.match(r'(?i)^(page\s+\d+\s+of\s+\d+|agenda item)', s):
                continue
            projects.append(s)
            break
    return projects

spring_projects = set()
for d in docs:
    spring_projects.update(extract_projects_started_spring2022(d.get('text','')))

spring_list = sorted(spring_projects)
joined = fund_df[fund_df['Project_Name'].isin(spring_list)] if spring_list else fund_df.iloc[0:0]

total_funding = int(joined['total_amount'].sum()) if not joined.empty else 0

out = {
    'count': int(len(spring_list)),
    'total_funding_usd': total_funding,
    'projects': spring_list
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5FRoyKoaGE92xUhwFnjuJHFV': 'file_storage/call_5FRoyKoaGE92xUhwFnjuJHFV.json', 'var_call_B8i9KzeWghvmclogSXmtIm7J': 'file_storage/call_B8i9KzeWghvmclogSXmtIm7J.json'}

exec(code, env_args)

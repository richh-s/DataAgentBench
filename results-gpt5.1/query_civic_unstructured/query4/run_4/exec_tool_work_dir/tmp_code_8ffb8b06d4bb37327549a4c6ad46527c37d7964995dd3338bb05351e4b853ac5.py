code = """import re, json, pandas as pd
path_docs = var_call_OTTl0MX24CZOAaWynRBL61aT
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]
path_fund = var_call_IftL3JDnUJXNCXCiNw68kJfU
with open(path_fund, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
pattern = re.compile(r'^(?P<name>.+?)\n[\s\S]*?Project Schedule:[\s\S]*?Begin Construction:\s*(?P<st>.+)$', re.MULTILINE)
projects = []
for text in texts:
    for match in pattern.finditer(text):
        name = match.group('name').strip()
        st = match.group('st').strip()
        projects.append({'Project_Name': name, 'st': st})
proj_df = pd.DataFrame(projects).drop_duplicates()
spring_months = ['March', 'April', 'May', '03', '04', '05']

def is_spring_2022(s):
    s = s or ''
    if '2022' not in s:
        return False
    if 'Spring' in s:
        return True
    for m in spring_months:
        if m in s:
            return True
    return False

proj_df = proj_df[proj_df['st'].apply(is_spring_2022)]
merged = proj_df.merge(fund_df, on='Project_Name', how='inner')
merged['Amount'] = merged['Amount'].astype(int)
result = {'num_projects_spring_2022': int(merged['Project_Name'].nunique()), 'total_funding_spring_2022': int(merged['Amount'].sum())}
out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_OTTl0MX24CZOAaWynRBL61aT': 'file_storage/call_OTTl0MX24CZOAaWynRBL61aT.json', 'var_call_IftL3JDnUJXNCXCiNw68kJfU': 'file_storage/call_IftL3JDnUJXNCXCiNw68kJfU.json'}

exec(code, env_args)

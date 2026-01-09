code = """import json, re, pandas as pd

# load funding totals
with open(var_call_lgQzBPI1GW1CUv0bwkSRuNj2, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# load docs
with open(var_call_kD0HQUvbN7JFMNHrDSHvWWAr, 'r') as f:
    docs = json.load(f)

# Find disaster projects started in 2022 by scanning for patterns in text
# We'll look for lines containing a project name that also includes FEMA/CalOES/CalJPIA or appears under Disaster Recovery section,
# and nearby a schedule line containing 2022.

def get_lines(text):
    return [ln.strip() for ln in text.splitlines()]

def likely_project_name(ln):
    if not ln:
        return False
    if ln.lower().startswith(('page ', 'agenda item', 'public works', 'agenda report')):
        return False
    if ln.endswith(':'):
        return False
    if len(ln) > 120:
        return False
    if re.search(r'(?i)recommended action|discussion|subject', ln):
        return False
    # avoid bullet lines
    if ln.startswith(('(cid', '•', '-', '(cid:')):
        return False
    return True

projects = {}  # name -> st

for d in docs:
    lines = get_lines(d.get('text',''))
    for idx, ln in enumerate(lines):
        if not likely_project_name(ln):
            continue
        window = '\n'.join(lines[idx:idx+30])
        # require disaster hint near
        if not re.search(r'(?i)disaster recovery projects|\bfema\b|caloes|caljpia', window + ' ' + ln):
            continue
        # find start/schedule token with 2022
        m = re.search(r'(?i)(begin construction|start|advertise|final design|complete design)\s*[:\-]\s*([^\n]{0,80}2022[^\n]{0,80})', window)
        st = None
        if m:
            st = re.sub(r'\s+', ' ', m.group(2)).strip()
        else:
            m2 = re.search(r'(2022[^\n]{0,40})', window)
            if m2:
                st = re.sub(r'\s+', ' ', m2.group(1)).strip()
        if st and ln not in projects:
            projects[ln] = st

proj_df = pd.DataFrame([{'Project_Name':k, 'st':v} for k,v in projects.items()])

# join with funding
merged = proj_df.merge(fund_df, on='Project_Name', how='inner')

out = {
  'total_funding_disaster_projects_started_2022': int(merged['total_amount'].sum()),
  'matched_projects_count': int(len(merged)),
  'matched_projects': merged[['Project_Name','st','total_amount']].sort_values('Project_Name').to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AANdMbvLJ8dHbieBcxTKvsNY': ['Funding'], 'var_call_Th2Urt5XiWHHxMjZkGfStPZG': ['civic_docs'], 'var_call_lgQzBPI1GW1CUv0bwkSRuNj2': 'file_storage/call_lgQzBPI1GW1CUv0bwkSRuNj2.json', 'var_call_kD0HQUvbN7JFMNHrDSHvWWAr': 'file_storage/call_kD0HQUvbN7JFMNHrDSHvWWAr.json'}

exec(code, env_args)

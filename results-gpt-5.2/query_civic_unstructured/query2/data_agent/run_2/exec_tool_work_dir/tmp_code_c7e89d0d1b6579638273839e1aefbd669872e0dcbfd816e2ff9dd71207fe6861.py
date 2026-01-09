code = """import json, re, pandas as pd

def load_json_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

docs = load_json_maybe_path(var_call_Vtkar1isgHg5NYjEr20jrsBI)
fund = load_json_maybe_path(var_call_z3Uc0TUUYnFKnmYOips0lfcE)

status_headers = [
    'Capital Improvement Projects (Design)',
    'Capital Improvement Projects (Construction)',
    'Capital Improvement Projects (Not Started)',
    'Disaster Recovery Projects (Design)',
    'Disaster Recovery Projects (Construction)',
    'Disaster Recovery Projects (Not Started)',
    'Disaster Recovery Projects (Active)',
    'Disaster Recovery Projects'
]

projects = []
for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    current_section = None
    for i, ln in enumerate(lines):
        if ln in status_headers:
            if 'Construction' in ln:
                current_section = 'construction'
            elif 'Design' in ln:
                current_section = 'design'
            elif 'Not Started' in ln:
                current_section = 'not started'
            else:
                current_section = None
            continue
        if current_section is None:
            continue
        if not ln or ln.lower().startswith('page ') or ln.lower().startswith('agenda item'):
            continue
        if ln.endswith(':'):
            continue
        if ln.startswith('(cid') or ln.startswith('•') or ln.startswith('-'):
            continue
        if len(ln) < 5:
            continue
        nxt = ' '.join(lines[i+1:i+8]).lower()
        if not (('updates' in nxt) or ('project description' in nxt) or ('project schedule' in nxt) or ('estimated schedule' in nxt)):
            continue
        proj = ln
        window = ' '.join(lines[i:i+40])
        et = None
        status = None
        m = re.search(r'Complete Construction:\s*([^\n]+?)(?:\s{2,}|$)', window, flags=re.I)
        if m:
            et = m.group(1).strip().strip('.')
        m2 = re.search(r'Construction was completed\s*,?\s*([^\n]+?)(?:\.|\sNotice of completion|$)', window, flags=re.I)
        if m2:
            et = m2.group(1).strip().strip('.')
            status = 'completed'
        if status is None and ('was completed' in window.lower() or ('notice of completion' in window.lower() and '2022' in window)):
            status = 'completed'
        projects.append({'Project_Name': proj, 'section': current_section, 'status': status, 'et': et, 'filename': d.get('filename')})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])
proj_df['is_park'] = proj_df['Project_Name'].str.contains(r'\bpark\b', case=False, regex=True)
proj_df['completed_2022'] = proj_df['status'].eq('completed') & proj_df['et'].fillna('').str.contains('2022', case=False)

# fallback: if status completed and window had 2022 but et missing, can't recover now; ignore.
eligible = proj_df[proj_df['is_park'] & proj_df['completed_2022']][['Project_Name']].drop_duplicates()

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

merged = eligible.merge(fund_df, on='Project_Name', how='left')
merged['total_amount'] = merged['total_amount'].fillna(0)

total = int(merged['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding_completed_2022_park_projects': total, 'projects': merged.to_dict(orient='records')}))"""

env_args = {'var_call_Vtkar1isgHg5NYjEr20jrsBI': 'file_storage/call_Vtkar1isgHg5NYjEr20jrsBI.json', 'var_call_z3Uc0TUUYnFKnmYOips0lfcE': 'file_storage/call_z3Uc0TUUYnFKnmYOips0lfcE.json'}

exec(code, env_args)

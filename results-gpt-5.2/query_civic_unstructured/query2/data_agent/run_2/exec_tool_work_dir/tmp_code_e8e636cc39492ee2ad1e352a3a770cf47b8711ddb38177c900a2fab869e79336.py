code = """import json, re, pandas as pd

def load_json_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

docs = load_json_maybe_path(var_call_Vtkar1isgHg5NYjEr20jrsBI)
fund = load_json_maybe_path(var_call_z3Uc0TUUYnFKnmYOips0lfcE)

# Parse projects from docs: capture name + status section + end date line
status_headers = ['Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)',
                  'Disaster Recovery Projects (Design)', 'Disaster Recovery Projects (Construction)', 'Disaster Recovery Projects (Not Started)',
                  'Disaster Recovery Projects (Active)', 'Disaster Recovery Projects']

header_re = re.compile(r'^(%s)\s*$' % ('|'.join(re.escape(h) for h in status_headers)), re.M)

# Pattern: project name line followed within next 0-400 chars by either 'Complete Construction:' or 'Construction was completed'
# We'll extract per line-based scanning under current status.
projects = []
for d in docs:
    text = d.get('text','')
    # split into lines for easier parsing
    lines = [ln.strip() for ln in text.splitlines()]
    current_status = None
    for i, ln in enumerate(lines):
        if ln in status_headers:
            if 'Construction' in ln:
                current_status = 'construction'
            elif 'Design' in ln:
                current_status = 'design'
            elif 'Not Started' in ln:
                current_status = 'not started'
            else:
                current_status = None
            continue
        # detect project name: non-empty, not bullet, not page, and followed by 'Updates' or 'Project Description' etc.
        if current_status is None:
            continue
        if not ln or ln.lower().startswith('page ') or ln.lower().startswith('agenda item'):
            continue
        if ln.startswith('(cid') or ln.startswith('(cid') or ln.startswith('•') or ln.startswith('-'):
            continue
        # heuristic: project names often contain letters and not end with ':'
        if len(ln) < 5 or ln.endswith(':'):
            continue
        # require that within next few lines appears 'Updates' or 'Project Description' or 'Project Schedule'
        nxt = ' '.join(lines[i+1:i+8]).lower()
        if not (('updates' in nxt) or ('project description' in nxt) or ('project schedule' in nxt) or ('estimated schedule' in nxt)):
            continue
        proj = ln
        # find completion evidence in nearby lines (next 25)
        window = ' '.join(lines[i:i+40])
        et = None
        completed = False
        m = re.search(r'Complete Construction:\s*([^\n]+?)(?:\s{2,}|$)', window, flags=re.I)
        if m:
            et = m.group(1).strip().strip('.')
        m2 = re.search(r'Construction was completed\s*,?\s*([^\n]+?)(?:\.|\sNotice of completion|$)', window, flags=re.I)
        if m2:
            et = m2.group(1).strip().strip('.')
            completed = True
        m3 = re.search(r'Construction was completed\s*([^\n]+?)(?:\.|$)', window, flags=re.I)
        if m3 and not et:
            et = m3.group(1).strip().strip('.')
            completed = True
        # infer completed if et mentions 2022 and phrases indicate completed
        if completed or ('was completed' in window.lower()) or ('notice of completion' in window.lower() and '2022' in window):
            status = 'completed'
        else:
            status = None
        projects.append({'Project_Name': proj, 'status_section': current_status, 'status_inferred': status, 'et': et, 'source_file': d.get('filename')})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name','source_file'])

# Determine park-related: project name contains 'park' OR nearby mention? We'll use name contains park.
proj_df['is_park'] = proj_df['Project_Name'].str.contains(r'\bpark\b', case=False, regex=True)

# Determine completed in 2022: status_inferred completed and et contains '2022'
proj_df['completed_2022'] = proj_df['status_inferred'].eq('completed') & proj_df['et'].fillna('').str.contains('2022', case=False)

# There may be completed projects without et captured; look for 'completed' and '2022' in same window not captured.
# quick pass: if project is in construction section and within 40 lines has 'completed' and '2022'
completed_extra = []
for d in docs:
    lines = [ln.strip() for ln in d.get('text','').splitlines()]
    current_status = None
    for i, ln in enumerate(lines):
        if ln in status_headers:
            current_status = 'construction' if 'Construction' in ln else None
            continue
        if current_status!='construction':
            continue
        if not ln or ln.lower().startswith('page ') or ln.lower().startswith('agenda item'):
            continue
        nxt = ' '.join(lines[i+1:i+8]).lower()
        if not (('updates' in nxt) or ('project description' in nxt) or ('project schedule' in nxt) or ('estimated schedule' in nxt)):
            continue
        proj = ln
        window = ' '.join(lines[i:i+40]).lower()
        if 'completed' in window and '2022' in window:
            completed_extra.append({'Project_Name': proj})
extra_set = set(pd.DataFrame(completed_extra)['Project_Name'].tolist()) if completed_extra else set()
proj_df.loc[proj_df['Project_Name'].isin(list(extra_set)), 'completed_2022'] = True

# Unique projects meeting criteria
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

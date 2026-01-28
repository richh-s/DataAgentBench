code = """import json, re, pandas as pd

# Load funding sums
funding_path = var_call_JFNSJn88SwwPbW3ARaj7PbSk
with open(funding_path,'r',encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# Load civic docs
docs_path = var_call_4NLqzXah9v790slRX2YcYvTs
with open(docs_path,'r',encoding='utf-8') as f:
    docs = json.load(f)

# Extract disaster project section items with schedule start lines
# Heuristic: find lines between 'Disaster Recovery Projects' and next major section, then parse project blocks.
projects = []
for d in docs:
    text = d.get('text','')
    if 'Disaster Recovery Projects' not in text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    # find indices of headers
    for i,ln in enumerate(lines):
        if re.search(r'\bDisaster Recovery Projects\b', ln):
            start_i = i
            break
    else:
        continue
    # take next ~300 lines
    sub = lines[start_i:start_i+400]
    # remove empty
    sub = [ln for ln in sub if ln]

    current = None
    in_schedule = False
    for ln in sub:
        # project name candidate: line that matches funding project names roughly (we'll map later), but simplest:
        # treat lines with no colon and not bullet and not common words as name when followed by 'Updates' or 'Project Schedule'
        if ln in ['Updates:', 'Project Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Project Schedule (pending the MOU extension approval):']:
            in_schedule = (ln.startswith('Project Schedule') or 'Schedule' in ln)
            continue
        # detect a new project header: not starting with bullet markers and not containing ':' and reasonably short
        if not re.search(r'^(\(cid:|[•\-]|\d+\.|Page\s+\d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION|Capital Improvement Projects)', ln) and ':' not in ln:
            # likely a header if next tokens are Title Case and length < 120
            if len(ln) <= 120 and any(ch.isalpha() for ch in ln):
                # exclude generic headings
                if ln.lower() in ['disaster recovery projects','capital improvement projects','construction','design','not started']:
                    continue
                # start new project
                current = {'Project_Name': ln, 'st': None}
                in_schedule = False
                projects.append(current)
                continue
        if current is None:
            continue
        if 'Begin Construction' in ln or 'Begin construction' in ln or re.search(r'\bStart\b', ln):
            # capture date after colon
            m = re.search(r':\s*(.*)$', ln)
            if m:
                current['st'] = m.group(1).strip()
        if in_schedule and current.get('st') is None and re.search(r'\bBegin Construction\b', ln, re.I):
            m = re.search(r':\s*(.*)$', ln)
            if m:
                current['st'] = m.group(1).strip()

# Determine which extracted projects are disaster-related: assume all in that section are disaster.
proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

# Filter start year 2022: st contains '2022'
proj_2022 = proj_df[proj_df['st'].fillna('').str.contains('2022')]

# Join with funding by exact name
joined = proj_2022.merge(fund_df, on='Project_Name', how='inner')

total = int(joined['total_amount'].sum())

out = {
    'total_funding': total,
    'project_count': int(joined.shape[0]),
    'projects': joined[['Project_Name','st','total_amount']].sort_values('Project_Name').to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JFNSJn88SwwPbW3ARaj7PbSk': 'file_storage/call_JFNSJn88SwwPbW3ARaj7PbSk.json', 'var_call_4NLqzXah9v790slRX2YcYvTs': 'file_storage/call_4NLqzXah9v790slRX2YcYvTs.json'}

exec(code, env_args)

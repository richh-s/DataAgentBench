code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_pvJShtqIdgjHoyyWmysUP8iU)
fund = load_records(var_call_9cXbeBzbNaOXIHYfXpfQYeX9)

# Parse project blocks from documents that contain Disaster Recovery Projects lists.
projects = []
for d in docs:
    text = d.get('text','')
    if 'Disaster Recovery Projects' not in text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    cur_section = None
    cur_type = None
    i = 0
    while i < len(lines):
        ln = lines[i]
        if re.search(r'^Disaster Recovery Projects\b', ln):
            cur_type = 'disaster'
            cur_section = None
            i += 1
            continue
        if re.search(r'^Capital Improvement Projects\b', ln):
            cur_type = 'capital'
            cur_section = None
            i += 1
            continue
        m = re.search(r'\((Design|Construction|Not Started)\)', ln)
        if m:
            cur_section = m.group(1).lower()
            i += 1
            continue
        if cur_type == 'disaster' and ln and not ln.startswith('(cid') and not re.match(r'^(Page \d+ of \d+|Agenda Item|RECOMMENDED ACTION:|DISCUSSION:|Subject:|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Updates:|Project Schedule:|Estimated Schedule:)$', ln):
            # Candidate project name line: occurs before '(cid:190) Updates:' or similar bullets
            # Avoid common headings
            if ln.lower() in {'disaster recovery projects', 'disaster recovery projects (design)', 'disaster recovery projects (construction)', 'disaster recovery projects (not started)'}:
                i += 1
                continue
            # Heuristic: next non-empty line contains 'Updates' bullet or 'Project Description'
            j = i+1
            nxt = ''
            while j < len(lines) and nxt == '':
                nxt = lines[j].strip()
                j += 1
            if 'Updates' in nxt or 'Project Description' in nxt or nxt.startswith('(cid:190)'):
                projects.append({'Project_Name': ln, 'type': 'disaster', 'section': cur_section, 'source_file': d.get('filename')})
                i += 1
                continue
        i += 1

# Deduplicate by exact name
proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

# Extract start year 2022 by searching within each doc text around project name for schedule lines
started_2022 = []
for _, row in proj_df.iterrows():
    pname = row['Project_Name']
    # find occurrences in docs
    for d in docs:
        txt = d.get('text','')
        if pname not in txt:
            continue
        idx = txt.find(pname)
        window = txt[idx: idx+2000]
        # Look for 'Begin Construction' or 'Begin' or 'Start' with 2022, or schedule entries with 2022.
        if re.search(r'Begin Construction:\s*[^\n]*2022', window, flags=re.IGNORECASE) or re.search(r'Begin (?:Work|Construction)\s*[:\-]?\s*[^\n]*2022', window, flags=re.IGNORECASE) or re.search(r'\bStart(?:ed)?\b[^\n]*2022', window, flags=re.IGNORECASE):
            started_2022.append(pname)
            break
        # Also accept any schedule line containing 2022-Spring/Fall etc near 'Project Schedule'
        if re.search(r'Project Schedule[\s\S]{0,500}?2022', window, flags=re.IGNORECASE):
            # ensure it's a start-like milestone
            if re.search(r'(Begin|Start)\s*(?:Construction|Work)?\s*:\s*[^\n]*2022', window, flags=re.IGNORECASE):
                started_2022.append(pname)
                break

started_2022 = sorted(set(started_2022))

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# sum funding for started_2022 projects
sum_amount = int(fund_df[fund_df['Project_Name'].isin(started_2022)]['total_amount'].sum())

out = {'total_funding_started_2022_disaster_projects': sum_amount, 'projects_count': len(started_2022), 'projects': started_2022}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WforWNGckDLZNcgvbG8AKAU6': ['Funding'], 'var_call_QfAvDZ3qPtBCuw0ojwVBpNT6': ['civic_docs'], 'var_call_pvJShtqIdgjHoyyWmysUP8iU': 'file_storage/call_pvJShtqIdgjHoyyWmysUP8iU.json', 'var_call_9cXbeBzbNaOXIHYfXpfQYeX9': 'file_storage/call_9cXbeBzbNaOXIHYfXpfQYeX9.json'}

exec(code, env_args)

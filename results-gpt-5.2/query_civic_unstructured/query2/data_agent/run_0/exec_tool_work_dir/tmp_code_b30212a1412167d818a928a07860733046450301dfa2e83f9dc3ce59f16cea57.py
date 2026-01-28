code = """import json, re
import pandas as pd

# Load civic docs (may be in a json file)
docs_src = var_call_uimwfzwWJBpsV8m3WbZCAK8D
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

fund_src = var_call_VmLgdKiy6567QWf43xxaq9P4
if isinstance(fund_src, str):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund = json.load(f)
else:
    fund = fund_src

fund_df = pd.DataFrame(fund)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype('int64')

# Parse projects with statuses and schedules from text blocks
projects = {}

status_headers = [
    (re.compile(r'\bCapital Improvement Projects\s*\(Design\)', re.I), 'design'),
    (re.compile(r'\bCapital Improvement Projects\s*\(Construction\)', re.I), 'construction'),
    (re.compile(r'\bCapital Improvement Projects\s*\(Not Started\)', re.I), 'not started'),
    (re.compile(r'\bDisaster Recovery Projects\s*\(Design\)', re.I), 'design'),
    (re.compile(r'\bDisaster Recovery Projects\s*\(Construction\)', re.I), 'construction'),
    (re.compile(r'\bDisaster Recovery Projects\s*\(Not Started\)', re.I), 'not started'),
]

# simplistic topic detection
park_kw = re.compile(r'\bpark\b|\bplayground\b|\bbluffs\b|\bskate\b', re.I)

for d in docs:
    text = d.get('text','') or ''
    if not text:
        continue

    # Split into lines for scanning
    lines = [ln.strip() for ln in text.splitlines()]

    current_status = None
    current_project = None

    # Track project blocks
    for i, ln in enumerate(lines):
        # update status based on headers
        for pat, st in status_headers:
            if pat.search(ln):
                current_status = st
                current_project = None
                break

        # Identify candidate project name lines: non-empty, not bullet, not header, title-ish
        if current_status is None:
            continue

        # Consider project name if line has letters, not too long, and not starting with punctuation
        if ln and len(ln) <= 120 and re.search(r'[A-Za-z]', ln):
            if re.match(r'^(Page \d+ of \d+|Agenda Item|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION|DISCUSSION|Project Description:|Project Updates:|Project Schedule:|Estimated Schedule:|Updates:)$', ln, re.I):
                continue
            if re.match(r'^(\(cid:|cid:|\u2022|\*|\-|\d+\.|[A-Z]{2,}\b)', ln):
                # skip many bullet artifacts, all-caps headings
                pass

        # Project names in these docs appear as standalone line followed by Updates/Schedule
        # Heuristic: if next few lines contain 'Updates' or 'Project Schedule' treat current line as project name
        lookahead = ' '.join(lines[i:i+6]).lower()
        if ln and 'updates' in lookahead and 'project' not in ln.lower() and not ln.lower().startswith(('updates','project')):
            # further require it to resemble a named project: contains road/park/etc or year
            if re.search(r'(road|park|playground|bluffs|skate|trail|walkway|canyon|drain|storm|pch|biofilter|signals|water|bridge|culvert|guardrail|street|ave|drive|center|facility|median)', ln, re.I) or re.search(r'\b20\d{2}\b', ln):
                current_project = ln
                proj = projects.get(current_project, {'Project_Name': current_project, 'status': set(), 'et': set(), 'topic_is_park': False})
                proj['status'].add(current_status)
                if park_kw.search(current_project):
                    proj['topic_is_park'] = True
                projects[current_project] = proj
                continue

        # capture completion dates lines for current project
        if current_project:
            m = re.search(r'\b(Complete(?:d)?\s+Construction|Construction\s+was\s+completed)\s*[:\-]?\s*(.*)$', ln, re.I)
            if m:
                date_part = m.group(2).strip()
                if date_part:
                    projects[current_project]['et'].add(date_part)

# Build dataframe
proj_df = pd.DataFrame([{**v, 'status': sorted(list(v['status'])), 'et': sorted(list(v['et']))} for v in projects.values()])
if proj_df.empty:
    total = 0
else:
    # Determine completed in 2022: any status includes 'construction' and et contains 2022 OR status explicitly 'completed'
    def completed_2022(row):
        # some projects may have status 'completed' in other docs; our parsing uses construction/not started/design.
        et_join = ' | '.join(row.get('et', []) if isinstance(row.get('et', []), list) else [])
        return ('2022' in et_join)

    proj_df['completed_2022'] = proj_df.apply(completed_2022, axis=1)
    proj_df['park_related'] = proj_df['topic_is_park']

    completed_parks = proj_df[proj_df['completed_2022'] & proj_df['park_related']]

    # Join to funding
    merged = completed_parks.merge(fund_df, on='Project_Name', how='left')
    total = int(merged['Amount'].fillna(0).sum())

result = {'total_funding_completed_2022_park_projects': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uimwfzwWJBpsV8m3WbZCAK8D': 'file_storage/call_uimwfzwWJBpsV8m3WbZCAK8D.json', 'var_call_VmLgdKiy6567QWf43xxaq9P4': 'file_storage/call_VmLgdKiy6567QWf43xxaq9P4.json'}

exec(code, env_args)

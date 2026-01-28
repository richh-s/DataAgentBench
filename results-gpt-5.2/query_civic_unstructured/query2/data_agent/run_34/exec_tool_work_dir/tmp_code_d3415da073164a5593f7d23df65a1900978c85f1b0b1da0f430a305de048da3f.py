code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

civic_docs = load_json_maybe(var_call_3K7hEc85tmIapV7kNVXe0blH)
funding = load_json_maybe(var_call_u7VKhrByYEe1IOOvkFi0EPhw)

# Build funding map
fund_df = pd.DataFrame(funding)
if fund_df.empty:
    total = 0
else:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# Parse projects from docs: look for sections and lines with end/completion + completed status.
projects = []

# patterns for headings: statuses
status_headers = {
    'completed': re.compile(r'^\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*\(\s*Completed\s*\)\s*$', re.I),
    'design': re.compile(r'^\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*\(\s*Design\s*\)\s*$', re.I),
    'construction': re.compile(r'^\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*\(\s*Construction\s*\)\s*$', re.I),
    'not started': re.compile(r'^\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*\(\s*Not Started\s*\)\s*$', re.I)
}

complete_line = re.compile(r'(Construction was completed|Complete Construction|Completed)\s*[:\-]?\s*([^\n\r]+)', re.I)

# heuristic for project name line: non-empty and not bullet marker, often title case, no colon.

def is_project_name_line(line):
    s=line.strip()
    if not s: return False
    if len(s)<3: return False
    if s.lower().startswith('page '): return False
    if s.lower().startswith('agenda item'): return False
    if s.startswith('(cid'): return False
    if s.endswith(':'): return False
    if 'Updates' in s or 'Project Schedule' in s or 'Project Description' in s: return False
    if re.match(r'^[•\-\*]+', s): return False
    # avoid obvious narrative lines
    if s.lower().startswith(('to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion', 'staff will')):
        return False
    # likely a project name if contains Park or Playground etc and not too long
    return True

for doc in civic_docs:
    text = doc.get('text','')
    if not text: continue
    lines = text.splitlines()
    current_status = None
    last_project = None
    for ln in lines:
        # update status header
        for st,pat in status_headers.items():
            if pat.match(ln):
                current_status = st
                last_project = None
                break
        s=ln.strip()
        if is_project_name_line(ln):
            # treat as potential project name within a status section
            if current_status in ('completed','design','construction','not started'):
                last_project = s
        m = complete_line.search(ln)
        if m and last_project:
            endtxt = m.group(2).strip()
            projects.append({'Project_Name': last_project, 'status': 'completed' if current_status=='completed' else current_status, 'end_text': endtxt})

proj_df = pd.DataFrame(projects).drop_duplicates()

# Filter: park-related (Project_Name contains park/playground/bluffs/legacy/skate) AND completed in 2022
park_pat = re.compile(r'\b(park|playground|bluffs|legacy|skate)\b', re.I)

def is_completed_2022(row):
    et = str(row.get('end_text',''))
    return '2022' in et

if not proj_df.empty:
    proj_df = proj_df[proj_df['Project_Name'].apply(lambda x: bool(park_pat.search(str(x))))]
    proj_df = proj_df[proj_df.apply(is_completed_2022, axis=1)]

# Join with funding totals
if proj_df.empty or fund_df.empty:
    total_funding = 0
    matched = []
else:
    merged = proj_df.merge(fund_df, on='Project_Name', how='inner')
    total_funding = int(merged['total_amount'].sum())
    matched = merged[['Project_Name','total_amount','end_text']].drop_duplicates().to_dict('records')

out = {'total_funding': total_funding, 'matched_projects': matched}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KcYHlncOaFoH06aDA133uxk6': ['Funding'], 'var_call_vce97t2PfwFA5ltMgxq0udMD': ['civic_docs'], 'var_call_3K7hEc85tmIapV7kNVXe0blH': 'file_storage/call_3K7hEc85tmIapV7kNVXe0blH.json', 'var_call_u7VKhrByYEe1IOOvkFi0EPhw': 'file_storage/call_u7VKhrByYEe1IOOvkFi0EPhw.json'}

exec(code, env_args)

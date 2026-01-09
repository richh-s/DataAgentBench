code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_records(var_call_YgUR6tR7zkFTdknoL5kz9DLG)
docs = load_records(var_call_ColyzPVLwrm6y70pEszOjYFI)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Parse civic docs for Disaster Recovery Projects section and extract project schedule lines
projects = {}  # name -> {'type': 'disaster', 'st': '...'}

# Patterns
header_pat = re.compile(r'^\s*Disaster\s+Recovery\s+Projects\s*(?:\(|\b)', re.IGNORECASE)
cap_header_pat = re.compile(r'^\s*Capital\s+Improvement\s+Projects', re.IGNORECASE)
status_header_pat = re.compile(r'^\s*Disaster\s+Recovery\s+Projects\s*\((Design|Construction|Not Started)\)', re.IGNORECASE)

# Project name is a non-empty line not starting with bullet/dot, followed by optional lines, then Project Schedule/Estimated Schedule then Begin Construction/Construction Start
begin_pat = re.compile(r'\b(Begin\s+Construction|Construction\s+Start)\s*:\s*(.+)$', re.IGNORECASE)
# sometimes schedule item like 'Start Construction:'
begin_pat2 = re.compile(r'\b(Start\s+Construction)\s*:\s*(.+)$', re.IGNORECASE)

for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    in_disaster = False
    current_project = None
    in_schedule = False
    for ln in lines:
        if not ln:
            continue
        if cap_header_pat.match(ln):
            # leaving disaster section if capital header encountered after being in disaster
            if in_disaster:
                in_disaster = False
                current_project = None
                in_schedule = False
        if status_header_pat.match(ln) or header_pat.match(ln):
            in_disaster = True
            current_project = None
            in_schedule = False
            continue
        if not in_disaster:
            continue
        # end if another major section begins
        if re.match(r'^\s*Staff\s+has\s+also\b', ln, re.IGNORECASE):
            in_disaster = False
            current_project = None
            in_schedule = False
            continue

        # detect schedule section starts
        if re.match(r'^\s*(Project\s+Schedule|Estimated\s+Schedule)\b', ln, re.IGNORECASE):
            in_schedule = True
            continue
        # if a new project name line: heuristic: line has letters, not starting with '(' or 'Page' or 'Agenda Item' or bullet char
        if re.match(r'^(Page\s+\d+\b|Agenda\s+Item\b)', ln, re.IGNORECASE):
            continue
        if ln.startswith(('-', '•','(cid')):
            # bullets, ignore
            pass
        # New project: title case-ish and not a schedule line, not updates, not recommended action
        if not in_schedule and not re.match(r'^(Updates|Project\s+Description|Discussion|Recommended\s+Action)\b', ln, re.IGNORECASE):
            # likely a project name if it matches one in funding table; else still may be project
            # We'll set current_project if line is in funding list OR looks like a standalone title (no colon)
            if ':' not in ln and len(ln) <= 120:
                current_project = ln
                in_schedule = False
                if current_project not in projects:
                    projects[current_project] = {'type':'disaster', 'st': None}
                continue

        if in_schedule and current_project:
            m = begin_pat.search(ln) or begin_pat2.search(ln)
            if m:
                st = m.group(2).strip()
                if projects.get(current_project, {}).get('st') is None:
                    projects[current_project] = {'type':'disaster', 'st': st}
                continue
            # if we reach a new project name while in_schedule, we'll switch when encountered above

# Now filter disaster projects with start containing '2022'
disaster_2022 = [name for name,info in projects.items() if info.get('st') and '2022' in info['st']]

# Join with funding totals
fund_2022 = fund_df[fund_df['Project_Name'].isin(disaster_2022)]

total = int(fund_2022['total_amount'].sum())

out = {
    'total_funding_disaster_projects_started_2022': total,
    'num_projects': int(fund_2022.shape[0]),
    'projects': fund_2022.sort_values('Project_Name')[['Project_Name','total_amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YgUR6tR7zkFTdknoL5kz9DLG': 'file_storage/call_YgUR6tR7zkFTdknoL5kz9DLG.json', 'var_call_ColyzPVLwrm6y70pEszOjYFI': 'file_storage/call_ColyzPVLwrm6y70pEszOjYFI.json'}

exec(code, env_args)

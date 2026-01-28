code = """import json, re, pandas as pd

# Load civic docs (Mongo query result)
path_docs = var_call_stLTAlnZKaVMrSFSE0TWNscH
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding totals per project
path_funding = var_call_f6sEqVQUCGI0kANW1XaoTmoW
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

text_all = "\n".join(d.get('text','') for d in docs)

# Extract Disaster Recovery Projects section
# Capture until next major heading (e.g., 'Staff has also' or end)
pattern = re.compile(r"Disaster\s+Recovery\s+Projects\s*(?:\(.*?\))?\s*(?:\n|\r\n)+(?P<section>.*)", re.IGNORECASE | re.DOTALL)
match = pattern.search(text_all)
section = match.group('section') if match else text_all

# Cut off at a likely next unrelated heading
cut_markers = [r"Staff has also", r"Capital Improvement Projects", r"Public Works Quarterly", r"Page \d+ of \d+", r"RECOMMENDED ACTION"]
for cm in cut_markers:
    m2 = re.search(cm, section, flags=re.IGNORECASE)
    if m2:
        section = section[:m2.start()]
        break

# Funding project names that look like disaster related in Funding table
# We'll use civic-doc extracted list to avoid over-including capital.

def parse_projects_with_start(section_text):
    lines = [ln.strip() for ln in section_text.splitlines()]
    projects = []
    current = None
    for ln in lines:
        if not ln:
            continue
        # project name lines: not starting with bullet and not containing ':' and relatively short
        if (not ln.startswith(('(cid', '•', '-', '(cid:')) and ':' not in ln and len(ln) < 120 
            and re.search(r"\bProject\b", ln, re.IGNORECASE) or re.search(r"Repairs\b|Repair\b|Improvements\b|Stabilization\b|Warning\b|Drain\b|Culvert\b|Bridge\b|Slope\b", ln, re.IGNORECASE)):
            # Heuristic: likely a title if next lines include Updates/Project Schedule
            if re.match(r"^(?:Updates|Project Schedule|Estimated Schedule|Project Description)\b", ln, flags=re.IGNORECASE):
                continue
            # avoid generic headings
            if re.match(r"^(Disaster Recovery Projects|Design|Construction|Not Started)$", ln, flags=re.IGNORECASE):
                continue
            # start new project
            if current:
                projects.append(current)
            current = {'Project_Name': ln, 'block': ''}
            continue
        if current:
            current['block'] += ln + "\n"
    if current:
        projects.append(current)

    # Extract start date tokens from block
    for p in projects:
        blk = p['block']
        # look for 'Begin Construction:' or 'Start' like patterns
        st = None
        m = re.search(r"Begin\s+Construction\s*:\s*([^\n\r]+)", blk, flags=re.IGNORECASE)
        if m:
            st = m.group(1).strip()
        else:
            m = re.search(r"Start\s*(?:Date)?\s*:\s*([^\n\r]+)", blk, flags=re.IGNORECASE)
            if m:
                st = m.group(1).strip()
        p['st'] = st
    return projects

projects = parse_projects_with_start(section)
proj_df = pd.DataFrame(projects)

# Filter for projects started in 2022: st contains '2022'
if proj_df.empty:
    started_2022 = pd.DataFrame(columns=['Project_Name'])
else:
    started_2022 = proj_df[proj_df['st'].fillna('').str.contains('2022', case=False, na=False)].copy()

# Join funding totals
if started_2022.empty or fund_df.empty:
    total = 0
else:
    merged = started_2022.merge(fund_df, on='Project_Name', how='left')
    total = int(merged['total_amount'].fillna(0).sum())

result = {'total_funding_disaster_projects_started_2022': total, 'projects_count': int(started_2022.shape[0]), 'projects': started_2022['Project_Name'].tolist()}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_stLTAlnZKaVMrSFSE0TWNscH': 'file_storage/call_stLTAlnZKaVMrSFSE0TWNscH.json', 'var_call_f6sEqVQUCGI0kANW1XaoTmoW': 'file_storage/call_f6sEqVQUCGI0kANW1XaoTmoW.json'}

exec(code, env_args)

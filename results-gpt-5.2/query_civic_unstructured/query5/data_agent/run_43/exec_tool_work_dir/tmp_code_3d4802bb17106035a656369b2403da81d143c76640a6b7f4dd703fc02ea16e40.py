code = """import json, re, pandas as pd

# Load funding totals per project
path_funding = var_call_9LRTw9p8CQH1knoR8Etwuoh7
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)
df_fund = pd.DataFrame(funding)
df_fund['total_amount'] = pd.to_numeric(df_fund['total_amount'])

# Load civic docs
path_docs = var_call_h1mBTWtOiYwb2M6jHJYUJtJl
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Find disaster recovery section and extract project names with schedule lines containing 2022 start
# We'll identify blocks under 'Disaster Recovery Projects' then parse lines.

disaster_projects_started_2022 = set()

# helpers
start_markers = [
    re.compile(r'\bBegin\s+Construction\s*:\s*(.*)', re.IGNORECASE),
    re.compile(r'\bBegin\s+Design\s*:\s*(.*)', re.IGNORECASE),
    re.compile(r'\bStart\s+(?:Construction|Design|Project)\s*:?\s*(.*)', re.IGNORECASE),
    re.compile(r'\bBegin\s+Bid\s*:?\s*(.*)', re.IGNORECASE),
    re.compile(r'\bAdvertise\s*:\s*(.*)', re.IGNORECASE),
]

def looks_like_project(line):
    if not line: return False
    if len(line) < 4: return False
    bad = {'updates:', 'project schedule:', 'estimated schedule:', 'project description:', 'capital improvement projects', 'disaster recovery projects'}
    low = line.strip().lower().rstrip(':')
    if low in bad: return False
    # exclude bullets/page
    if low.startswith('page ') or low.startswith('agenda item'):
        return False
    # mostly words, may include parentheses
    if re.search(r'\b(cid:|\u2022|\*|\-\s)$', line.strip()):
        return False
    return True

for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text and 'DISASTER RECOVERY PROJECTS' not in text:
        continue
    # Split into lines
    lines = [ln.strip() for ln in text.splitlines()]
    # Find indices where disaster section starts
    for i, ln in enumerate(lines):
        if re.search(r'^Disaster Recovery Projects', ln, re.IGNORECASE):
            start_i = i
            break
    else:
        continue
    # end at next major header (Capital Improvement Projects or end)
    end_i = len(lines)
    for j in range(start_i+1, len(lines)):
        if re.search(r'^Capital Improvement Projects', lines[j], re.IGNORECASE):
            end_i = j
            break
    section = lines[start_i:end_i]

    current_project = None
    for ln in section:
        if not ln:
            continue
        # if line looks like a project name (not bullets and not headers) and not starting with (cid etc)
        if looks_like_project(ln) and not re.search(r'^(\(|cid:|\u2022|\*|\-)', ln, re.IGNORECASE):
            # treat as project line if it doesn't contain ':' and is Title Case-ish
            if ':' not in ln and not re.search(r'\bUpdates\b|\bSchedule\b|\bDescription\b', ln, re.IGNORECASE):
                # store as current project candidate
                current_project = ln
                continue
        # look for schedule start lines
        if current_project:
            for pat in start_markers:
                m = pat.search(ln)
                if m:
                    val = (m.group(1) or '').strip()
                    if '2022' in val:
                        disaster_projects_started_2022.add(current_project)
                    break

# As fallback: disaster projects often have FEMA/CalOES etc in name. Also, some docs may list schedule as "Start: 2022" without marker; try any line with 2022 in same project block.
# We'll scan disaster sections for pattern: project name line followed within next 8 lines any '2022'

def scan_window(section_lines, window=8):
    found = set()
    for idx, ln in enumerate(section_lines):
        if looks_like_project(ln) and ':' not in ln and not re.search(r'Updates|Schedule|Description', ln, re.IGNORECASE):
            proj = ln
            w = ' '.join(section_lines[idx+1:idx+1+window])
            if '2022' in w and re.search(r'\b(2022)\b', w):
                # ensure it's start-ish
                if re.search(r'Begin|Start|Advertise|Kickoff', w, re.IGNORECASE):
                    found.add(proj)
    return found

for d in docs:
    text = d.get('text','') or ''
    if not re.search(r'Disaster Recovery Projects', text, re.IGNORECASE):
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    # locate section as above
    for i, ln in enumerate(lines):
        if re.search(r'^Disaster Recovery Projects', ln, re.IGNORECASE):
            start_i = i
            break
    else:
        continue
    end_i = len(lines)
    for j in range(start_i+1, len(lines)):
        if re.search(r'^Capital Improvement Projects', lines[j], re.IGNORECASE):
            end_i = j
            break
    section = [ln for ln in lines[start_i:end_i] if ln]
    disaster_projects_started_2022 |= scan_window(section)

# Join with funding totals
if len(disaster_projects_started_2022)==0:
    total = 0
    projects = []
else:
    df = df_fund[df_fund['Project_Name'].isin(list(disaster_projects_started_2022))]
    total = int(df['total_amount'].sum())
    projects = sorted(df['Project_Name'].tolist())

out = {
    'total_funding': total,
    'project_count_with_funding': len(projects),
    'projects_with_funding': projects
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9LRTw9p8CQH1knoR8Etwuoh7': 'file_storage/call_9LRTw9p8CQH1knoR8Etwuoh7.json', 'var_call_h1mBTWtOiYwb2M6jHJYUJtJl': 'file_storage/call_h1mBTWtOiYwb2M6jHJYUJtJl.json', 'var_call_QAfQ96K2TyjqYPSUtKzbHIiG': ['Funding'], 'var_call_cxMIsGphe9S0zjJQjPqUmEqF': ['civic_docs']}

exec(code, env_args)

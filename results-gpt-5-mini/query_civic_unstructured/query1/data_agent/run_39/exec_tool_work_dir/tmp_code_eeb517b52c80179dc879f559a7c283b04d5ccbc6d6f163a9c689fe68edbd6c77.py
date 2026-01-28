code = """import json, re

# Load data from storage-provided file paths
with open(var_call_UrVWWvuVBu7aCx5TM44vQ0Us, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_rJvMltsJV2QTMqPnwUhjH4If, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Helper normalize function: lowercase, remove non-alphanumeric, collapse spaces
def normalize(name):
    s = name.lower()
    s = re.sub(r"\(.*?\)", "", s)  # remove parenthetical suffixes like (FEMA Project)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Extract project names under the 'Capital Improvement Projects (Design)' sections
design_projects = []
end_markers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Capital Improvement Projects (Not Started)",
]
for doc in civic_docs:
    text = doc.get('text','')
    # find the design section
    idx = text.find('Capital Improvement Projects (Design)')
    if idx == -1:
        # try small variations
        idx = text.find('Capital Improvement Projects (Design)')
    if idx == -1:
        continue
    sub = text[idx:]
    # cut off at the next major capital heading if present
    end_idx = None
    for em in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Construction)']:
        p = sub.find(em)
        if p != -1:
            end_idx = p
            break
    if end_idx is not None:
        sub = sub[:end_idx]
    lines = sub.splitlines()
    # skip the first header line
    for line in lines[1:]:
        s = line.strip()
        if not s:
            continue
        # skip markup/annotation lines
        if s.startswith('('):
            continue
        low = s.lower()
        if any(tok in low for tok in ['updates', 'update:', 'project schedule', 'project schedule:', 'project description', 'estimated schedule', 'page', 'agenda item', 'item', 'to:', 'prepared by', 'approved by']):
            continue
        # skip lines that look like labels
        if low.startswith('public works') or low.startswith('subject:'):
            continue
        # Heuristic: Accept lines that contain letters and not too short
        if len(s) < 4:
            continue
        # Some lines include trailing markers like '\u2014' or unexpected headers; clean
        cleaned = s
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        # Avoid picking up section subheadings like 'Page 1 of 6' or 'Agenda Report'
        if re.match(r'^page \d+', cleaned.lower()):
            continue
        # Accept probable project names (avoid lines that are all caps and short)
        design_projects.append(cleaned)

# Deduplicate while preserving order
seen = set()
design_projects_clean = []
for p in design_projects:
    if p not in seen:
        seen.add(p)
        design_projects_clean.append(p)

# Prepare funding lookup
funding_list = funding_records
# Normalize and sum amounts by funding record normalized name
for fr in funding_list:
    # ensure Amount numeric
    try:
        fr['Amount_num'] = int(fr.get('Amount') if fr.get('Amount') is not None else 0)
    except:
        try:
            fr['Amount_num'] = int(float(fr.get('Amount')))
        except:
            fr['Amount_num'] = 0
    fr['norm_name'] = normalize(fr.get('Project_Name',''))

# For each design project, find matching funding records (by normalized name equality or containment)
results = []
for pj in design_projects_clean:
    pj_norm = normalize(pj)
    matched = [fr for fr in funding_list if (fr['norm_name'] == pj_norm or pj_norm in fr['norm_name'] or fr['norm_name'] in pj_norm)]
    total = sum(fr['Amount_num'] for fr in matched)
    results.append({'project_name': pj, 'project_norm': pj_norm, 'matched_count': len(matched), 'total_funding': total, 'matched_funding_records': [fr['Project_Name'] for fr in matched]})

# Count how many have total_funding > 50000
qualifying = [r for r in results if r['total_funding'] > 50000]
count = len(qualifying)

# Prepare JSON-serializable output
out = {'count': count, 'projects': [{'project_name': r['project_name'], 'total_funding': r['total_funding'], 'matched_funding_records': r['matched_funding_records']} for r in qualifying]}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_OUkZSJ1mMI3iVG7p9nck62Mp': ['civic_docs'], 'var_call_oySWtNUKYQ4qKIdZk8OsqWnb': ['Funding'], 'var_call_UrVWWvuVBu7aCx5TM44vQ0Us': 'file_storage/call_UrVWWvuVBu7aCx5TM44vQ0Us.json', 'var_call_rJvMltsJV2QTMqPnwUhjH4If': 'file_storage/call_rJvMltsJV2QTMqPnwUhjH4If.json'}

exec(code, env_args)

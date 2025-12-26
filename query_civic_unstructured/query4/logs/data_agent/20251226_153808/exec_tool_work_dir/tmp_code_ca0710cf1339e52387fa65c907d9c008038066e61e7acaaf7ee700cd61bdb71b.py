code = """import json, re, os
from collections import defaultdict

# Load civic docs result
path_docs = var_call_OuhJp8PlS61ugPvNvSrrvtdi
if isinstance(path_docs, str) and os.path.isfile(path_docs):
    with open(path_docs, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = path_docs

# Load funding table
path_funding = var_call_XVmrKOW3CdB3WGC1867OBsyJ
if isinstance(path_funding, str) and os.path.isfile(path_funding):
    with open(path_funding, 'r', encoding='utf-8') as f:
        funding_rows = json.load(f)
else:
    funding_rows = path_funding

# Helper normalization for base project names
def normalize_base(name: str) -> str:
    if not name:
        return ''
    s = name.lower().strip()
    # replace ampersand with 'and'
    s = s.replace('&', ' and ')
    # remove parenthetical content
    s = re.sub(r'\s*\(.*?\)\s*', ' ', s)
    # remove common trailing word 'project'
    s = re.sub(r'\s+project\s*$', ' ', s)
    # remove extra punctuation
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    # collapse whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Build funding dict aggregated by normalized base name
funding_amounts_base = defaultdict(int)
for row in funding_rows:
    name = (row.get('Project_Name') or '').strip()
    amt = row.get('Amount')
    try:
        amt_int = int(amt)
    except Exception:
        try:
            amt_int = int(float(amt))
        except Exception:
            amt_int = 0
    base = normalize_base(name)
    if base:
        funding_amounts_base[base] += amt_int

# Patterns for Spring 2022 start
spring_2022_terms = [
    'spring 2022', '2022 spring',
]
spring_months = ['march', 'mar', 'april', 'apr', 'may']

# Start indicators
start_indic_re = re.compile(r'(begin\s+construction|construction\s+start|project\s+start|start\s*date|notice\s+to\s+proceed|\bst\s*:)', re.IGNORECASE)

# Determine if a line indicates Spring 2022

def is_spring_2022_line(line: str) -> bool:
    l = line.strip()
    if '2022' not in l:
        return False
    ll = l.lower()
    if any(term in ll for term in spring_2022_terms):
        return True
    # Check for 2022 plus a spring month
    for m in spring_months:
        if re.search(r'\b'+re.escape(m)+r'\b', ll):
            return True
    return False

# Heuristic to extract nearest project name above the line index
stop_markers = [
    re.compile(r'^\s*capital improvement projects', re.IGNORECASE),
    re.compile(r'^\s*disaster recovery projects', re.IGNORECASE),
    re.compile(r'^\s*agenda', re.IGNORECASE),
    re.compile(r'^\s*project\s+schedule', re.IGNORECASE),
    re.compile(r'^\s*estimated\s+schedule', re.IGNORECASE),
    re.compile(r'^\s*updates?:', re.IGNORECASE),
    re.compile(r'^\s*item', re.IGNORECASE),
    re.compile(r'^\s*subject', re.IGNORECASE),
    re.compile(r'^\s*prepared by', re.IGNORECASE),
    re.compile(r'^\s*approved by', re.IGNORECASE),
    re.compile(r'^\s*meeting date', re.IGNORECASE),
    re.compile(r'^\s*date prepared', re.IGNORECASE),
    re.compile(r'^\s*project description', re.IGNORECASE),
]

def extract_project_name(lines, idx):
    for j in range(idx-1, max(-1, idx-20), -1):
        cand = lines[j].strip()
        if not cand:
            continue
        if any(p.search(cand) for p in stop_markers):
            continue
        if cand.endswith(':'):
            continue
        if cand.startswith(('(', '•', '-', '–', '—')):
            continue
        if cand.isupper() and len(cand.split()) <= 4:
            continue
        # avoid schedule lines themselves
        if re.search(r'\b(schedule|updates?)\b', cand, re.IGNORECASE):
            continue
        return cand
    return None

projects_started = {}
# Iterate through documents
for doc in civic_docs:
    text = doc.get('text') or ''
    if not text:
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if start_indic_re.search(line) and is_spring_2022_line(line):
            name = extract_project_name(lines, i)
            if name:
                base = normalize_base(name)
                projects_started.setdefault(base, {'original_names': set(), 'evidence': []})
                projects_started[base]['original_names'].add(name)
                if len(projects_started[base]['evidence']) < 3:
                    projects_started[base]['evidence'].append(line.strip())

# Compute counts and funding sums
count_projects = len(projects_started)

# Sum funding for these base names
funding_sum = 0
matched_details = []
for base, info in sorted(projects_started.items()):
    amt = funding_amounts_base.get(base, 0)
    funding_sum += amt
    matched_details.append({
        'base_project_name': base,
        'example_original_names': sorted(list(info['original_names']))[:2],
        'evidence_lines': info['evidence'],
        'funding_amount_sum_for_base_name': amt
    })

result = {
    'count_projects_started_in_spring_2022': count_projects,
    'total_funding_for_these_projects': funding_sum,
    'details_sample': matched_details[:15]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uvXPpZayHc9xvopowuZEgPWg': ['civic_docs'], 'var_call_Zk4SE6cwwjot1ZhijJ7vHsSe': ['Funding'], 'var_call_OuhJp8PlS61ugPvNvSrrvtdi': 'file_storage/call_OuhJp8PlS61ugPvNvSrrvtdi.json', 'var_call_XVmrKOW3CdB3WGC1867OBsyJ': 'file_storage/call_XVmrKOW3CdB3WGC1867OBsyJ.json'}

exec(code, env_args)

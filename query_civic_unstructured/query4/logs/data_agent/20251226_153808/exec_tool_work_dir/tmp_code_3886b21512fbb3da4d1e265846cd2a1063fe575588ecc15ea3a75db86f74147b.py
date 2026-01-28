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

# Normalize function for base project names

def normalize_base(name: str) -> str:
    if not name:
        return ''
    s = name.strip()
    # remove leading bullets or numbering
    s = re.sub(r'^[\s\-•\(\)\d\.]+', '', s)
    # replace ampersand with 'and'
    s = s.replace('&', ' and ')
    # remove parenthetical content
    s = re.sub(r'\s*\(.*?\)\s*', ' ', s)
    # remove common trailing word 'project'
    s = re.sub(r'\s+Project\s*$', '', s, flags=re.IGNORECASE)
    # collapse whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    return s.lower()

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

# Define Spring 2022 detector
spring_terms = ['spring 2022', '2022 spring']
spring_months = ['march', 'mar', 'april', 'apr', 'may']
start_indic_re = re.compile(r'(begin\s+construction|construction\s+start|project\s+start|start\s*date|notice\s+to\s+proceed|\bst\s*:)', re.IGNORECASE)


def is_spring_2022_line(line: str) -> bool:
    l = line.strip()
    if '2022' not in l:
        return False
    ll = l.lower()
    if any(term in ll for term in spring_terms):
        return True
    for m in spring_months:
        if re.search(r'\b'+re.escape(m)+r'\b', ll):
            return True
    return False

# Title candidate detection
keywords = ['project', 'improvements', 'repairs', 'repair', 'park', 'road', 'bridge', 'canyon', 'storm drain', 'biofilter', 'water', 'traffic', 'walkway', 'median', 'guardrail', 'playground', 'skate', 'facility', 'slope', 'retaining wall', 'culvert']

def is_title_candidate(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    # reject lines that clearly are schedule or narrative
    if ':' in s and not s.endswith('Project') and not s.endswith('Improvements') and not s.endswith('Repairs'):
        # lines with colon are usually headers or narratives
        return False
    if s.endswith('.'):
        return False
    # title case word count
    words = s.split()
    cap_initials = sum(1 for w in words if w[:1].isupper())
    if cap_initials < max(2, int(0.5*len(words))):
        # need sufficient capitalized words
        pass  # don't strictly enforce; some titles have lowercase connectors
    # keyword presence
    low = s.lower()
    if any(k in low for k in keywords):
        return True
    # otherwise, if it's short and mostly capitalized
    if len(words) <= 6 and cap_initials >= len(words)-1:
        return True
    return False

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

def find_project_title_above(lines, idx):
    for j in range(idx-1, max(-1, idx-15), -1):
        cand = lines[j].strip()
        if not cand:
            continue
        if any(p.search(cand) for p in stop_markers):
            continue
        if is_title_candidate(cand):
            return cand
    return None

projects_started = {}
for doc in civic_docs:
    text = doc.get('text') or ''
    if not text:
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if start_indic_re.search(line) and is_spring_2022_line(line):
            title = find_project_title_above(lines, i)
            if title:
                base = normalize_base(title)
                if not base:
                    continue
                info = projects_started.setdefault(base, {'titles': set(), 'evidence': []})
                info['titles'].add(title)
                if len(info['evidence']) < 3:
                    info['evidence'].append(line.strip())

# Compute results
count_projects = len(projects_started)
funding_sum = 0
details = []
for base, info in sorted(projects_started.items()):
    amt = funding_amounts_base.get(base, 0)
    funding_sum += amt
    details.append({
        'base_project_name': base,
        'example_titles': sorted(list(info['titles']))[:2],
        'evidence_lines': info['evidence'],
        'funding_sum_for_base': amt
    })

result = {
    'count_projects_started_in_spring_2022': count_projects,
    'total_funding_for_these_projects': funding_sum,
    'details_sample': details[:15]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uvXPpZayHc9xvopowuZEgPWg': ['civic_docs'], 'var_call_Zk4SE6cwwjot1ZhijJ7vHsSe': ['Funding'], 'var_call_OuhJp8PlS61ugPvNvSrrvtdi': 'file_storage/call_OuhJp8PlS61ugPvNvSrrvtdi.json', 'var_call_XVmrKOW3CdB3WGC1867OBsyJ': 'file_storage/call_XVmrKOW3CdB3WGC1867OBsyJ.json', 'var_call_5WMba0RocrmG5abEotdWZ8zu': {'count_projects_started_in_spring_2022': 14, 'total_funding_for_these_projects': 357000, 'details_sample': [{'base_project_name': 'advertised for construction bids shortly after this date', 'example_original_names': ['advertised for construction bids shortly after this date.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'beginning in spring 2022', 'example_original_names': ['beginning in Spring 2022.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'damaged by the woolsey fire', 'example_original_names': ['damaged by the Woolsey Fire.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'facilities and roadway embankments that were damaged by the woolsey fire', 'example_original_names': ['facilities and roadway embankments that were damaged by the Woolsey Fire.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'fire', 'example_original_names': ['Fire.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'is finalizing the bid documents', 'example_original_names': ['is finalizing the bid documents.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'is working on the project plans to prepare for public bidding', 'example_original_names': ['is working on the project plans to prepare for public bidding.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'scheduled for the april 11 2022 council meeting', 'example_original_names': ['scheduled for the April 11, 2022 Council meeting.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'sending this project out to bid during the spring of 2022', 'example_original_names': ['sending this project out to bid during the Spring of 2022.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'shade structures at malibu bluffs park', 'example_original_names': ['shade structures at Malibu Bluffs Park.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'that was damaged by the woolsey fire', 'example_original_names': ['that was damaged by the Woolsey Fire.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'timber with non combustible materials', 'example_original_names': ['timber with non-combustible materials.'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 0}, {'base_project_name': 'trancas canyon park planting and irrigation repairs', 'example_original_names': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 214000}, {'base_project_name': 'trancas canyon park slope stabilization', 'example_original_names': ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'evidence_lines': ['(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022'], 'funding_amount_sum_for_base_name': 143000}]}}

exec(code, env_args)

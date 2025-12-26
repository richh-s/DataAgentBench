code = """import json, re, os
from collections import defaultdict

# Load civic docs result
path_docs = var_call_OuhJp8PlS61ugPvNvSrrvtdi
if os.path.isfile(path_docs):
    with open(path_docs, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_call_OuhJp8PlS61ugPvNvSrrvtdi  # in case it's already a list

# Load funding table
path_funding = var_call_XVmrKOW3CdB3WGC1867OBsyJ
if os.path.isfile(path_funding):
    with open(path_funding, 'r', encoding='utf-8') as f:
        funding_rows = json.load(f)
else:
    funding_rows = var_call_XVmrKOW3CdB3WGC1867OBsyJ

# Build funding dict by exact Project_Name
funding_amounts = defaultdict(int)
for row in funding_rows:
    name = row.get('Project_Name')
    amt = row.get('Amount')
    try:
        amt_int = int(amt)
    except Exception:
        # try float then int cast
        try:
            amt_int = int(float(amt))
        except Exception:
            amt_int = 0
    if name:
        funding_amounts[name.strip()] += amt_int

# Patterns for Spring 2022 start
spring_2022_patterns = [
    re.compile(r'\bSpring\s*2022\b', re.IGNORECASE),
    re.compile(r'\b2022\s*Spring\b', re.IGNORECASE),
]
# month patterns
months = ['March', 'Mar', 'April', 'Apr', 'May']
month_patterns = [re.compile(r'\b'+m+\n, re.IGNORECASE) for m in []]  # placeholder not used

# Build generic start indicators
start_keywords = [
    'Begin Construction', 'Construction Start', 'Start of Construction', 'Start:', 'Start Date', 'Start', 'st:', 'Project Start', 'Notice to Proceed'
]
# We'll search for lines that have 2022 and either Spring or a spring month

spring_months = ['March', 'Mar', 'April', 'Apr', 'May']

def is_spring_2022_line(line):
    l = line.strip()
    if '2022' not in l:
        return False
    # Check Spring
    for pat in spring_2022_patterns:
        if pat.search(l):
            return True
    # Check specific months
    for m in spring_months:
        if re.search(r'\b'+re.escape(m)+r'\b', l, re.IGNORECASE):
            return True
    return False

# Additionally ensure it's some kind of start-related line
start_indic_re = re.compile(r'(Begin\s+Construction|Construction\s+Start|Start\s*:?|st\s*:?|Notice\s+to\s+Proceed)', re.IGNORECASE)

# Heuristic to extract nearest project name above the line index

def extract_project_name(lines, idx):
    # search upwards up to 10 lines to find a plausible project title
    stop_markers = [
        re.compile(r'^\s*Capital Improvement Projects', re.IGNORECASE),
        re.compile(r'^\s*Disaster Recovery Projects', re.IGNORECASE),
        re.compile(r'^\s*Agenda', re.IGNORECASE),
        re.compile(r'^\s*Project\s+Schedule', re.IGNORECASE),
        re.compile(r'^\s*Estimated\s+Schedule', re.IGNORECASE),
        re.compile(r'^\s*Updates?:', re.IGNORECASE),
        re.compile(r'^\s*Item', re.IGNORECASE),
        re.compile(r'^\s*Subject', re.IGNORECASE),
        re.compile(r'^\s*Prepared by', re.IGNORECASE),
        re.compile(r'^\s*Approved by', re.IGNORECASE),
        re.compile(r'^\s*Meeting date', re.IGNORECASE),
        re.compile(r'^\s*Date prepared', re.IGNORECASE),
        re.compile(r'^\s*Project Description', re.IGNORECASE),
    ]
    for j in range(idx-1, max(-1, idx-15), -1):
        cand = lines[j].strip()
        if not cand:
            continue
        # skip lines that are clearly not names
        if any(p.search(cand) for p in stop_markers):
            # keep going further up
            continue
        if cand.endswith(':'):
            # likely a header, skip
            continue
        # skip bullet-like entries
        if cand.startswith(('(', '•', '-', '–', '—')):
            continue
        # skip all-caps lines that are likely section headers but if they are short like 'DISCUSSION'
        if cand.isupper() and len(cand.split()) <= 3:
            continue
        # else accept this as project name
        return cand
    return None

projects_started_spring_2022 = set()
source_evidence = defaultdict(list)

for doc in civic_docs:
    text = doc.get('text') or ''
    if not text:
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if is_spring_2022_line(line) and start_indic_re.search(line):
            name = extract_project_name(lines, i)
            if name:
                projects_started_spring_2022.add(name)
                # store evidence line
                source_evidence[name].append(line.strip())
        # Also capture explicit "st:" patterns even if without start_indic but with Spring/Mar/Apr/May 2022
        if 'st' in line.lower() and is_spring_2022_line(line):
            name = extract_project_name(lines, i)
            if name:
                projects_started_spring_2022.add(name)
                source_evidence[name].append(line.strip())

# Now compute total funding sum
count_projects = len(projects_started_spring_2022)

# Attempt to map project names to funding exact match; also handle some normalization like removing trailing 'Project'

def normalize(name):
    return name.strip()

names_mapped = []
funding_sum = 0
unmatched = []
for pname in sorted(projects_started_spring_2022):
    n = normalize(pname)
    amt = funding_amounts.get(n)
    if amt is None or amt == 0:
        # try some variants: remove trailing 'Project', 'Improvements Project' vs 'Improvements'
        variants = set()
        if n.endswith(' Project'):
            variants.add(n[:-8])
        if n.endswith(' Projects'):
            variants.add(n[:-9])
        if ' Improvements Project' in n:
            variants.add(n.replace(' Improvements Project', ' Improvements'))
        if ' Repair Project' in n:
            variants.add(n.replace(' Repair Project', ' Repair'))
        if ' Repairs Project' in n:
            variants.add(n.replace(' Repairs Project', ' Repairs'))
        if ' Road ' in n and ' Roadway/Retaining Wall Improvements' in funding_amounts:
            pass
        found = False
        for v in variants:
            amt_v = funding_amounts.get(v)
            if amt_v:
                amt = amt_v
                found = True
                n = v
                break
        if not found:
            unmatched.append(pname)
            continue
    funding_sum += amt
    names_mapped.append({'Project_Name': pname, 'Funding_Match_Name': n, 'Amount': amt, 'Evidence': source_evidence.get(pname, [])[:2]})

result = {
    'count_projects_started_spring_2022': count_projects,
    'total_funding_for_these_projects': funding_sum,
    'matched_projects_detail_sample': names_mapped[:10],
    'unmatched_projects_sample': unmatched[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uvXPpZayHc9xvopowuZEgPWg': ['civic_docs'], 'var_call_Zk4SE6cwwjot1ZhijJ7vHsSe': ['Funding'], 'var_call_OuhJp8PlS61ugPvNvSrrvtdi': 'file_storage/call_OuhJp8PlS61ugPvNvSrrvtdi.json', 'var_call_XVmrKOW3CdB3WGC1867OBsyJ': 'file_storage/call_XVmrKOW3CdB3WGC1867OBsyJ.json'}

exec(code, env_args)

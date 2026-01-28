code = """import json
import re

# Load the large query results from storage-provided file paths
with open(var_call_bL3GaMT9aRuk5IYztuJtmf6B, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_x7aqU6vz0ZsKaLH4mtwjbPXb, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Build funding lookup: list of dicts with Project_Name and Total_Amount
# Normalize funding entries
funding_list = []
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Total_Amount')
    try:
        amt_int = int(amt)
    except Exception:
        try:
            amt_int = int(float(amt))
        except Exception:
            amt_int = 0
    funding_list.append({'name': name, 'amount': amt_int})

# Helper: find candidate project name given text lines and index
ignore_patterns = [
    re.compile(pat, re.I) for pat in [
        r'project schedule', r'updates', r'project description', r'agenda', r'page', r'complete design',
        r'capital improvement projects', r'disaster projects', r'project', r'cid:\d+', r'begin (design|construction)',
        r'advertise', r'award contract', r'complete design', r'estimated schedule', r'estimated schedule:',
        r'begin construction', r'begin design', r'begin', r'updates:', r'updates\b'
    ]
]

def is_valid_candidate(line):
    if not line:
        return False
    line_stripped = line.strip()
    if len(line_stripped) < 3 or len(line_stripped) > 120:
        return False
    # exclude lines that look like labels or contain many non-letters
    if re.search(r'\b(project schedule|updates|project description|agenda|page|begin construction|begin design)\b', line_stripped, re.I):
        return False
    if re.search(r'^\(cid:|^cid:\d+', line_stripped, re.I):
        return False
    # exclude lines that end with ':' as they are likely headings like 'Project Schedule:'
    if line_stripped.endswith(':'):
        return False
    # exclude lines that are all caps and short like 'DISCUSSION' or 'RECOMMENDED ACTION'
    if line_stripped.isupper() and len(line_stripped.split()) < 4:
        return False
    return True

matches = {}

# Regex patterns to identify a start in Spring 2022
start_patterns = [
    re.compile(r'Begin\s+Construction[^\n]*Spring[^\n]*2022', re.I),
    re.compile(r'Begin\s+Construction[^\n]*Spring/\w+[^\n]*2022', re.I),
    re.compile(r'Begin\s+Design[^\n]*Spring[^\n]*2022', re.I),
    re.compile(r'Begin\s+Construction[^\n]*2022.*Spring', re.I),
    re.compile(r'Begin\s+Construction[^\n]*Spring', re.I)  # fallback, ensure year in nearby context
]

# Also consider lines like 'Begin Construction: Spring/Summer 2022' captured by above

for doc in civic_docs:
    text = doc.get('text', '')
    # Normalize line endings
    lines = text.splitlines()
    for i, line in enumerate(lines):
        for pat in start_patterns:
            if pat.search(line):
                # quick check: ensure 2022 is somewhere within +/-3 lines
                window = "\n".join(lines[max(0,i-3):min(len(lines), i+4)])
                if '2022' not in window:
                    continue
                # search backwards for candidate project name
                project_name = None
                for j in range(i-1, max(-1, i-12), -1):
                    cand = lines[j].strip()
                    if is_valid_candidate(cand):
                        project_name = cand
                        break
                if not project_name:
                    # as fallback, try finding an uppercase-title-like line further back
                    for j in range(i-1, max(-1, i-20), -1):
                        cand = lines[j].strip()
                        if cand and len(cand.split()) <= 6 and any(c.isalpha() for c in cand):
                            project_name = cand
                            break
                if project_name:
                    # normalize whitespace
                    proj_norm = re.sub(r'\s+', ' ', project_name).strip()
                    matches[proj_norm] = matches.get(proj_norm, 0) + 1

# Convert matches to a unique list
extracted_projects = sorted(matches.keys())

# For each extracted project, find funding by matching funding_list entries
project_funding = []
for proj in extracted_projects:
    total = 0
    matched_entries = []
    # exact match first
    for fr in funding_list:
        if fr['name'] and fr['name'].strip().lower() == proj.strip().lower():
            total += fr['amount']
            matched_entries.append(fr['name'])
    if total == 0:
        # try substring matches (either way)
        for fr in funding_list:
            if fr['name'] and (proj.lower() in fr['name'].lower() or fr['name'].lower() in proj.lower()):
                total += fr['amount']
                matched_entries.append(fr['name'])
    project_funding.append({'name': proj, 'funding': total, 'matched_funding_entries': matched_entries})

# Remove projects with zero funding matches? The question likely expects sum across matched funding records.
# We'll include projects even if funding is 0

total_projects = len(project_funding)
total_funding = sum(p['funding'] for p in project_funding)

result = {
    'project_count': total_projects,
    'total_funding': total_funding,
    'projects': project_funding
}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_MujWVKL2rzsnCnBkRhI5jdNc': ['civic_docs'], 'var_call_CkJufZ8OKzfyEKZaSzfjxgyj': ['Funding'], 'var_call_bL3GaMT9aRuk5IYztuJtmf6B': 'file_storage/call_bL3GaMT9aRuk5IYztuJtmf6B.json', 'var_call_x7aqU6vz0ZsKaLH4mtwjbPXb': 'file_storage/call_x7aqU6vz0ZsKaLH4mtwjbPXb.json'}

exec(code, env_args)

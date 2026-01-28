code = """import json
import re

# Load data from previous tool results (file paths provided)
with open(var_call_JXvtPsrHoxLgjVcNtxofWA6V, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_l8nTWRGX6PlLJUPCTejRkg1M, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Normalize funding records
funding_map = {}  # normalized name -> list of (original_name, amount)
for rec in funding:
    name = rec.get('Project_Name', '').strip()
    amt = int(rec.get('Amount', 0)) if rec.get('Amount') not in (None, '') else 0
    norm = re.sub(r"\s+", " ", name).strip().lower()
    funding_map.setdefault(norm, []).append({'original_name': name, 'amount': amt})

# Also build a list of funding names for substring matches
funding_names = list(funding_map.keys())

# Helper to find design section in a document
section_start_pattern = re.compile(r'capital improvement projects\s*\(design\)', re.IGNORECASE)
section_end_candidates = [
    r'capital improvement projects\s*\(construction\)',
    r'capital improvement projects\s*\(not started\)',
    r'capital improvement projects\s*\(completed\)',
    r'capital improvement projects\s*\(construction\)',
    r'capital improvement projects\s*\(not started\)'
]
section_end_pattern = re.compile('|'.join(section_end_candidates), re.IGNORECASE)

extracted_projects = set()

for doc in docs:
    text = doc.get('text', '')
    # find design section
    m = section_start_pattern.search(text)
    if not m:
        continue
    start = m.end()
    # find next section boundary after start
    m2 = section_end_pattern.search(text, start)
    end = m2.start() if m2 else len(text)
    section = text[start:end]
    # Split into lines and extract project names
    lines = section.splitlines()
    # find next non-empty line helper
    def next_non_empty(i):
        j = i+1
        while j < len(lines) and lines[j].strip() == '':
            j += 1
        return j if j < len(lines) else None

    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        # Skip obvious non-title lines
        low = s.lower()
        if low.startswith('updates') or low.startswith('page') or 'agenda' in low or low.endswith(':'):
            continue
        if s.startswith('('):
            continue
        # Look ahead to see if next non-empty line starts with patterns indicating this is a project title
        j = next_non_empty(i)
        next_line = lines[j].strip() if j is not None else ''
        if next_line.startswith('(cid') or next_line.lower().startswith('updates') or 'project schedule' in next_line.lower() or 'project description' in next_line.lower() or next_line.lower().startswith('(cid:'):
            # consider s a project title
            # Clean s: remove leading bullets or numbers
            title = re.sub(r'^[\-\u2022\*\d\.\)\s]+', '', s).strip()
            # Normalize whitespace
            title = re.sub(r"\s+", " ", title)
            if title:
                extracted_projects.add(title)

# Now match extracted projects to funding records with amount > 50000
matched_projects = []
for proj in sorted(extracted_projects):
    pname_norm = proj.lower()
    matched_fundings = []
    # Exact or normalized match
    if pname_norm in funding_map:
        for fr in funding_map[pname_norm]:
            if fr['amount'] > 50000:
                matched_fundings.append(fr)
    # substring matches
    if not matched_fundings:
        for fn in funding_names:
            if pname_norm in fn or fn in pname_norm:
                for fr in funding_map[fn]:
                    if fr['amount'] > 50000:
                        matched_fundings.append(fr)
    if matched_fundings:
        matched_projects.append({'project_name': proj, 'fundings': matched_fundings})

count = len(matched_projects)

# Prepare printable result
result = {'count': count, 'matched_projects': matched_projects}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JXvtPsrHoxLgjVcNtxofWA6V': 'file_storage/call_JXvtPsrHoxLgjVcNtxofWA6V.json', 'var_call_l8nTWRGX6PlLJUPCTejRkg1M': 'file_storage/call_l8nTWRGX6PlLJUPCTejRkg1M.json'}

exec(code, env_args)

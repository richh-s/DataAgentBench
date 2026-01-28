code = """import json
import re
from pathlib import Path

# Load the stored query results from files
civic_path = Path(var_call_2Fp1bAHB7PBvCeTmjbFiiz04)
funding_path = Path(var_call_Z7OVvUBbhExXMcwpCPQkBe4N)
with civic_path.open('r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with funding_path.open('r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Normalize funding rows: list of dicts with Project_Name and Amount as int
funding = []
for r in funding_rows:
    name = r.get('Project_Name')
    amount = r.get('Amount')
    try:
        amt = int(amount)
    except:
        try:
            amt = int(float(amount))
        except:
            amt = 0
    funding.append({'Project_Name': name, 'Amount': amt})

# Helper to find funding total for a project name
def match_funding(project_name):
    pn = project_name.strip().lower()
    total = 0
    matched = False
    for fr in funding:
        fn = (fr['Project_Name'] or '').strip().lower()
        # exact match
        if fn == pn:
            total += fr['Amount']
            matched = True
            continue
        # substring match either way
        if pn in fn or fn in pn:
            total += fr['Amount']
            matched = True
            continue
        # remove parenthetical suffixes in fn
        fn_nop = re.sub(r"\s*\([^)]*\)", "", fn).strip()
        if fn_nop == pn or pn in fn_nop or fn_nop in pn:
            total += fr['Amount']
            matched = True
            continue
    return total, matched

# Extract projects that have a Begin (start) in Spring 2022
spring_2022_projects = []
pattern = re.compile(r'begin\b[^\n]{0,100}spring\s*,?\s*2022', re.IGNORECASE)
# Also catch 'begin construction' with Spring 2022
pattern2 = re.compile(r'begin\s+construction[^\n]{0,100}spring\s*,?\s*2022', re.IGNORECASE)
# Generic also consider 'start' variants
pattern3 = re.compile(r'begin\b[^\n]{0,100}2022.*spring|spring.*2022', re.IGNORECASE)

for doc in civic_docs:
    text = doc.get('text') or ''
    # Normalize line endings and split
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if pattern.search(line) or pattern2.search(line) or ("begin" in line.lower() and 'spring' in line.lower() and '2022' in line):
            # search backward for project title
            proj = None
            for j in range(i-1, max(-1, i-12), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                # skip lines that look like labels or metadata
                low = cand.lower()
                if low.startswith('(cid') or low.startswith('page ') or 'updates' in low or 'project schedule' in low or 'agenda' in low or 'item' in low:
                    continue
                # skip lines that are short or are dates
                if len(cand) < 5:
                    continue
                # if cand contains many digits like dates, skip
                if sum(ch.isdigit() for ch in cand) > len(cand)/2:
                    continue
                proj = cand
                break
            if proj:
                spring_2022_projects.append(proj)

# Deduplicate preserving order
seen = set()
unique_projects = []
for p in spring_2022_projects:
    key = p.strip()
    if key.lower() not in seen:
        seen.add(key.lower())
        unique_projects.append(key)

# For each project, find funding amount
projects_with_funding = []
total_funding = 0
for p in unique_projects:
    amt, matched = match_funding(p)
    projects_with_funding.append({'name': p, 'funding': amt, 'matched_funding_record': matched})
    total_funding += amt

result = {
    'count': len(unique_projects),
    'total_funding': total_funding,
    'projects': projects_with_funding
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2Fp1bAHB7PBvCeTmjbFiiz04': 'file_storage/call_2Fp1bAHB7PBvCeTmjbFiiz04.json', 'var_call_Z7OVvUBbhExXMcwpCPQkBe4N': 'file_storage/call_Z7OVvUBbhExXMcwpCPQkBe4N.json'}

exec(code, env_args)

code = """import json, re

# Load the civic documents query result and the funding aggregation result
with open(var_call_BluEeKeRlnhnPiwlKGMEmLEa, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_jPItYFKSpJ9uZinUyW91jl6C, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Build funding map: normalized project name -> amount (int)
fund_map = {}
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Total_Amount')
    try:
        amt_int = int(amt)
    except:
        amt_int = 0
        if amt:
            digits = re.sub(r'[^0-9]', '', str(amt))
            if digits:
                amt_int = int(digits)
    fund_map[name] = amt_int

# Patterns indicating Spring 2022
patterns = ['spring 2022', 'spring/summer 2022', 'march 2022', 'april 2022', 'may 2022', '2022-03', '2022-04', '2022-05']

# Helper to decide if a line is a plausible project title
def is_title_line(line):
    if not line:
        return False
    s = line.strip()
    if len(s) < 3 or len(s) > 200:
        return False
    low = s.lower()
    exclude_starts = ['to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject:', 'updates:', 'project schedule:', 'project description:', 'page ', 'agenda item']
    for es in exclude_starts:
        if low.startswith(es):
            return False
    if low.startswith('(cid') or low.startswith('cid:'):
        return False
    # avoid lines that are clearly schedule bullets
    if re.search(r'begin\b', low) or re.search(r'complete design', low) or re.search(r'advertise', low) or re.search(r'estimated schedule', low):
        return False
    return True

found_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # split into paragraphs
    blocks = [b.strip() for b in re.split(r'\n\s*\n', text) if b.strip()]
    for block in blocks:
        low = block.lower()
        if any(p in low for p in patterns):
            lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
            title = None
            for ln in lines:
                if is_title_line(ln):
                    title = ln
                    break
            if not title:
                # fallback: find line before a pattern-containing line
                for i, ln in enumerate(lines):
                    if any(p in ln.lower() for p in patterns):
                        for j in range(i-1, -1, -1):
                            if is_title_line(lines[j]):
                                title = lines[j]
                                break
                        if title:
                            break
            if title:
                # clean title
                title = re.sub(r'\s+\(cid:.*\)$', '', title).strip()
                found_projects.append(title)

# Deduplicate preserving order
seen = set()
projects = []
for p in found_projects:
    key = p.strip()
    low = key.lower()
    if low not in seen:
        seen.add(low)
        projects.append(key)

# Match to funding
matched_keys = set()
unmatched = []
for proj in projects:
    plow = proj.lower()
    matched = False
    # exact match
    for fk in fund_map:
        if fk and fk.lower() == plow:
            matched_keys.add(fk)
            matched = True
            break
    if matched:
        continue
    # containment
    for fk in fund_map:
        if not fk:
            continue
        fk_low = fk.lower()
        if plow in fk_low or fk_low in plow:
            matched_keys.add(fk)
            matched = True
            break
    if not matched:
        unmatched.append(proj)

total = sum(fund_map[k] for k in matched_keys)

result = {
    'count_projects_started_spring_2022': len(projects),
    'total_matched_funding': total,
    'extracted_projects': projects,
    'matched_funding_projects': sorted(list(matched_keys)),
    'unmatched_projects': unmatched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cJibmufZIbpLLOJoY7hsw2Qi': ['civic_docs'], 'var_call_BluEeKeRlnhnPiwlKGMEmLEa': 'file_storage/call_BluEeKeRlnhnPiwlKGMEmLEa.json', 'var_call_jPItYFKSpJ9uZinUyW91jl6C': 'file_storage/call_jPItYFKSpJ9uZinUyW91jl6C.json'}

exec(code, env_args)

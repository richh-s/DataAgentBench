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
        # fallback if stored as string with commas
        amt_int = int(re.sub(r"[^0-9]", "", str(amt))) if amt and re.search(r"\d", str(amt)) else 0
    fund_map[name] = amt_int

# Patterns indicating Spring 2022 (and March-May 2022 indicators)
patterns = ["spring 2022", "spring/summer 2022", "spring/summer 2022", "march 2022", "april 2022", "may 2022", "2022-03", "2022-04", "2022-05"]

# Helper to decide if a line is a plausible project title
def is_title_line(line):
    if not line or len(line) < 3 or len(line) > 200:
        return False
    low = line.strip().lower()
    # exclude metadata-like lines
    exclude_starts = ["to:", "prepared by", "approved by", "date prepared", "meeting date", "subject:", "updates:", "project schedule:", "project description:", "page ", "agenda item"]
    for es in exclude_starts:
        if low.startswith(es):
            return False
    if low.startswith('(cid') or low.startswith('cid:'):
        return False
    # exclude lines that look like sentence fragments with many punctuation
    if ':' in line and len(line.split(':')[0].split())>4:
        # often key: value lines; keep some like "Project Schedule:" though excluded above
        return False
    return True

found_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    # Normalize newlines
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    for block in blocks:
        low = block.lower()
        if any(p in low for p in patterns):
            # try to extract a plausible title from the block
            lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
            title = None
            # Prefer the first reasonable line that looks like a project name
            for ln in lines:
                if is_title_line(ln):
                    # avoid picking lines that are clearly schedule bullets like "Begin Construction: Spring 2022"
                    if re.search(r"begin\b", ln, re.I) or re.search(r"complete design", ln, re.I) or re.search(r"advertise", ln, re.I) or re.search(r"estimated schedule", ln, re.I):
                        continue
                    title = ln
                    break
            if not title:
                # fallback: look upward from the line containing a pattern to find the nearest title-looking line
                for i, ln in enumerate(lines):
                    if any(p in ln.lower() for p in patterns):
                        # scan backwards
                        for j in range(i-1, -1, -1):
                            if is_title_line(lines[j]):
                                title = lines[j]
                                break
                        if title:
                            break
            if title:
                # Clean title: remove trailing words like "Project" duplicated or page markers
                title = re.sub(r"\s+\(cid:.*\)$", "", title).strip()
                found_projects.append(title)

# Deduplicate preserving order
seen = set()
projects = []
for p in found_projects:
    key = p.strip()
    if key.lower() not in seen:
        seen.add(key.lower())
        projects.append(key)

# Now match extracted projects to funding entries
matched_funding_keys = set()
unmatched_projects = []
for proj in projects:
    plow = proj.lower()
    matched = False
    # exact match
    for fk in fund_map:
        if fk.lower() == plow:
            matched_funding_keys.add(fk)
            matched = True
            break
    if matched:
        continue
    # containment match: proj in fk or fk in proj
    for fk in fund_map:
        fk_low = fk.lower()
        if plow in fk_low or fk_low in plow:
            matched_funding_keys.add(fk)
            matched = True
            break
    if not matched:
        unmatched_projects.append(proj)

# Sum funding amounts for matched funding keys
total_funding = sum(fund_map[k] for k in matched_funding_keys)

result = {
    'count_projects_started_spring_2022': len(projects),
    'total_matched_funding': total_funding,
    'extracted_projects': projects,
    'matched_funding_projects': sorted(list(matched_funding_keys)),
    'unmatched_projects': unmatched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cJibmufZIbpLLOJoY7hsw2Qi': ['civic_docs'], 'var_call_BluEeKeRlnhnPiwlKGMEmLEa': 'file_storage/call_BluEeKeRlnhnPiwlKGMEmLEa.json', 'var_call_jPItYFKSpJ9uZinUyW91jl6C': 'file_storage/call_jPItYFKSpJ9uZinUyW91jl6C.json'}

exec(code, env_args)

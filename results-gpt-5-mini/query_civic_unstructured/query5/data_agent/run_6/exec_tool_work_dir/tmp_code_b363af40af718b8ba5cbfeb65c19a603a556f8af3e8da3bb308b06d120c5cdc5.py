code = """import json
import re

# Load previously stored tool results
with open(var_call_90dmcYwBxTb7vQatqrbc7U4G, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_7E8sUjkgBqwcx0vACQAqhl9z, 'r') as f:
    funding = json.load(f)

# Helper functions
def normalize(s):
    return re.sub(r"[^a-z0-9 ]+", " ", s.lower()).strip()

# Disaster keywords
disaster_keywords = ["fema", "caloes", "caloja", "caljpia", "fema/caloes", "fema/caloes", "disaster", "fire", "woolsey", "recovery", "cal o es", "cal o es", "caljpia"]

# Collect candidate project titles from civic docs
project_candidates = {}

title_pattern = re.compile(r"^([A-Z][A-Za-z0-9 &'()\-,:]+?(Project|Improvements|Improvements Project|Repairs|Repair|Restoration|Resurfacing|Renovation|Study|Facility|Playground|Phase|Road|Roadway|Bridge|Culvert|Drainage|Traffic Study|Facility|Park|Walkway|Project).*)$")

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # record indices of titles
    titles = {}
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        m = title_pattern.match(line_stripped)
        if m:
            title = line_stripped
            titles[i] = title
            # initialize entry
            project_candidates[title] = project_candidates.get(title, {'doc_id': doc.get('_id'), 'blocks': [], 'lines': lines})
    # find lines with '2022'
    for i, line in enumerate(lines):
        if '2022' in line:
            # find nearest previous title index
            prev_titles = [idx for idx in titles.keys() if idx <= i]
            if prev_titles:
                nearest = max(prev_titles)
                title = titles[nearest]
                # capture a block: from title index to next title or +10 lines
                # find next title index
                next_titles = [idx for idx in titles.keys() if idx > nearest]
                end = (min(next_titles) if next_titles else min(len(lines), nearest+20))
                block = '\n'.join(lines[nearest:end])
                project_candidates[title]['blocks'].append(block)

# Now determine which projects are disaster-related and started in 2022
# Heuristic: project has at least one block containing '2022' (we already captured) and block or title contains disaster keywords
selected_projects = set()
for title, info in project_candidates.items():
    blocks = info['blocks']
    if not blocks:
        continue
    combined = title + '\n' + '\n'.join(blocks)
    low = combined.lower()
    # check disaster keywords
    if any(k in low for k in disaster_keywords):
        # check if any line in blocks indicates begin or start in 2022
        started = False
        for b in blocks:
            for line in b.splitlines():
                if '2022' in line:
                    # if line mentions begin or start or advertise or construction or complete design
                    if any(k in line.lower() for k in ['begin construction', 'begin construction:', 'begin construction', 'start', 'advertise', 'advertise:', 'complete design', 'complete design:', 'begin construction', 'begin construction:']):
                        started = True
                        break
                    # also consider 'construction was completed, november 2022' not a start
                    # but if line says 'begin construction: winter 2022' etc
                    if 'begin' in line.lower() or 'start' in line.lower() or 'advertise' in line.lower():
                        started = True
                        break
            if started:
                break
        # As fallback if not found started by keywords, but block has 2022 associated, accept it
        if not started:
            # if any 2022 found in block, take it as started in 2022 per loose hint
            if any('2022' in b for b in blocks):
                started = True
        if started:
            selected_projects.add(title)

# Also consider projects where title itself mentions FEMA/CalOES etc even if we didn't capture blocks
# Scan entire document text for lines that look like project names with parentheses including FEMA/CalOES and a nearby 2022
for doc in civic_docs:
    text = doc.get('text','')
    for m in re.finditer(r"([A-Za-z0-9 &'()\-,:]+\(.*?(FEMA|CalOES|CalJPIA).*?\).{0,200})", text, re.IGNORECASE):
        snippet = m.group(0)
        # find project name up to newline
        candidate = snippet.split('\n')[0].strip()
        if '2022' in text[max(0, m.start()-200):m.end()+200]:
            selected_projects.add(candidate)

# Normalize selected_projects
selected_projects = list(selected_projects)

# Now match with funding records
matched_records = []
fund_total = 0

for rec in funding:
    fname = rec.get('Project_Name','')
    fname_norm = normalize(fname)
    for p in selected_projects:
        p_norm = normalize(p)
        if not p_norm:
            continue
        # match if one contains the other
        if p_norm in fname_norm or fname_norm in p_norm:
            amt = rec.get('Amount')
            try:
                amt_int = int(str(amt))
            except:
                try:
                    amt_int = int(float(str(amt)))
                except:
                    amt_int = 0
            fund_total += amt_int
            matched_records.append({'Project_Name': rec.get('Project_Name'), 'Amount': amt_int})
            break

# Deduplicate matched_records by Project_Name
unique = {}
for r in matched_records:
    unique[r['Project_Name']] = r
matched_list = list(unique.values())

import json
result = {'total_funding': fund_total, 'matched_projects': matched_list, 'selected_projects': selected_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FbCAMFAZTL2Ih3VWgvwFzEcF': ['civic_docs'], 'var_call_90dmcYwBxTb7vQatqrbc7U4G': 'file_storage/call_90dmcYwBxTb7vQatqrbc7U4G.json', 'var_call_aId1Wornd25qzPfcbmiNPMM9': ['Funding'], 'var_call_7E8sUjkgBqwcx0vACQAqhl9z': 'file_storage/call_7E8sUjkgBqwcx0vACQAqhl9z.json'}

exec(code, env_args)

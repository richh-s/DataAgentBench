code = """import json
from pathlib import Path

# Load results from previous query tool calls
civic_path = var_call_pLE2WbY9t57zr1o1htKTHb5u
funding_path = var_call_Fz70htaJ8zqS1o9DpRQ6GX2s

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Build funding lookup dict (Project_Name -> total_amount int)
funding_dict = {}
for r in funding_rows:
    name = r.get('Project_Name')
    try:
        amt = int(r.get('total_amount'))
    except:
        try:
            amt = int(r.get('Amount', 0))
        except:
            amt = 0
    funding_dict[name] = amt

# Patterns to search for Spring 2022 occurrences
patterns = ["Spring 2022", "2022-Spring", "2022 Spring", "Spring, 2022",
            "March 2022", "Mar 2022", "April 2022", "Apr 2022", "May 2022", "May, 2022",
            "2022-March", "2022-April", "2022-May"]

found_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Normalize newlines
    lines = text.splitlines()
    lowered = text.lower()
    for pat in patterns:
        start = 0
        while True:
            idx = lowered.find(pat.lower(), start)
            if idx == -1:
                break
            # find line index containing this idx
            # compute char pos to line index
            char_count = 0
            line_idx = 0
            for i, line in enumerate(lines):
                char_count += len(line) + 1
                if char_count > idx:
                    line_idx = i
                    break
            # search upwards for a candidate project title
            candidate = None
            for j in range(line_idx-1, max(-1, line_idx-30), -1):
                if j < 0:
                    break
                l = lines[j].strip()
                if not l:
                    continue
                # skip obvious headers or labels
                low = l.lower()
                if low.startswith('(') or low.startswith('cid') or low.startswith('to:') or low.startswith('prepared by') or low.startswith('approved by'):
                    continue
                if any(k in low for k in ['project schedule', 'updates', 'project description', 'discussion', 'recommended action', 'agenda', 'page']):
                    continue
                # likely a title if contains words and not colon-only lines
                if ':' in l and len(l) < 40:
                    # could be like 'Project Schedule:' skip
                    continue
                # avoid lines that look like section headers e.g., 'Capital Improvement Projects (Design)'
                # but these sometimes are followed by project names; still accept if contains keywords
                candidate = l
                # if candidate looks like a good project name by containing keywords, stop
                keywords = ['Project', 'Road', 'Park', 'Repairs', 'Improvements', 'Resurfacing', 'Drain', 'Playground', 'Water', 'Traffic', 'Signal', 'Slope', 'Bridge', 'Canyon', 'Bluffs', 'Skate', 'Median', 'Walkway']
                if any(k.lower() in low for k in [kw.lower() for kw in keywords]):
                    break
                # otherwise continue searching up to find a better one
            if candidate:
                found_projects.append(candidate)
            start = idx + len(pat)

# Deduplicate and clean project names
unique_projects = []
seen = set()
for p in found_projects:
    pp = ' '.join(p.split())
    if pp.lower() not in seen:
        seen.add(pp.lower())
        unique_projects.append(pp)

# Attempt to match funding for each project
matched = []
for proj in unique_projects:
    amt = None
    # exact match
    if proj in funding_dict:
        amt = funding_dict[proj]
    else:
        # try normalized: remove common suffixes in funding table or proj
        def normalize(s):
            s = s.replace('(FEMA Project)', '').replace('(CalOES Project)', '').replace('(CalJPIA Project)', '')
            s = s.replace('(FEMA/CalOES Project)', '').replace('(CalJPIA/FEMA Project)', '')
            return s.strip().lower()
        nproj = normalize(proj)
        # try find funding entries where normalized names equal
        found_amt = 0
        found_any = False
        for fname, famt in funding_dict.items():
            if normalize(fname) == nproj:
                found_amt = famt
                found_any = True
                break
        if found_any:
            amt = found_amt
        else:
            # try substring matches
            for fname, famt in funding_dict.items():
                if nproj in fname.lower() or fname.lower() in nproj:
                    amt = famt
                    found_any = True
                    break
    if amt is None:
        amt = 0
    matched.append({'Project_Name': proj, 'Funding': amt})

# Filter out projects with zero funding? The question likely expects count of projects started in Spring 2022 and their total funding.
# Keep all projects found; sum funding
count = len(matched)
total = sum(m['Funding'] for m in matched)

result = {'count': count, 'total_funding': total, 'projects': matched}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pLE2WbY9t57zr1o1htKTHb5u': 'file_storage/call_pLE2WbY9t57zr1o1htKTHb5u.json', 'var_call_Fz70htaJ8zqS1o9DpRQ6GX2s': 'file_storage/call_Fz70htaJ8zqS1o9DpRQ6GX2s.json'}

exec(code, env_args)

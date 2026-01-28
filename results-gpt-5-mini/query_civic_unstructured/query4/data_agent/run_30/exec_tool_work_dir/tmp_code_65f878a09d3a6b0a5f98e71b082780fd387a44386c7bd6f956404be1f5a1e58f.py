code = """import json, re

# Load data from storage paths
with open(var_call_VRJfQzwEvGj1nReSJtvXQEzi, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_RVk0cVgnA6ObHRufRtLeY0mk, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Build funding map: Project_Name -> total amount (int)
funding_map = {}
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Total_Amount')
    try:
        amt_int = int(amt)
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = 0
    funding_map[name.strip()] = amt_int

# Helper to decide if a line is likely a project title
exclude_phrases = ['updates', 'project schedule', 'project description', 'agenda', 'item', 'page', 'meeting', 'subject', 'recommended action', 'discussion', 'estimated schedule']

def is_likely_title(line):
    if not line:
        return False
    s = line.strip()
    if len(s) < 3:
        return False
    low = s.lower()
    if any(p in low for p in exclude_phrases):
        return False
    if ':' in s:
        return False
    if s.startswith('(') or s.startswith('cid'):
        return False
    # avoid lines that are clearly dates
    if re.search(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', s):
        return False
    # must contain a letter
    if not re.search(r'[A-Za-z]', s):
        return False
    return True

found_projects = []

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        low = line.lower()
        if 'spring' in low and '2022' in low:
            # search backwards up to 12 lines for a likely title
            title = None
            for j in range(max(0, idx-12), idx+1):
                cand = lines[j].strip()
                if is_likely_title(cand):
                    title = cand
                    # prefer the last plausible title before the schedule, continue searching to get the closest
            if title:
                # Clean title: remove trailing words like 'Project' if it's alone? Keep as-is
                found_projects.append(title)

# Deduplicate preserving order
seen = set()
uniq_projects = []
for p in found_projects:
    if p not in seen:
        seen.add(p)
        uniq_projects.append(p)

# Match to funding_map keys using exact match first, then fuzzy contains
matched = []
unmatched = []
for p in uniq_projects:
    # exact match
    if p in funding_map:
        matched.append({'Project_Name': p, 'Amount': funding_map[p]})
    else:
        # try to find a funding key that contains p or p contains key
        found_key = None
        for k in funding_map.keys():
            if p.lower() == k.lower():
                found_key = k
                break
        if not found_key:
            for k in funding_map.keys():
                if p.lower() in k.lower() or k.lower() in p.lower():
                    found_key = k
                    break
        if found_key:
            matched.append({'Project_Name': found_key, 'Amount': funding_map[found_key], 'Matched_By': found_key})
        else:
            unmatched.append({'Project_Name': p, 'Amount': 0})

# Compute totals
num_projects = len(uniq_projects)
# For funding total, sum matched amounts; include unmatched as 0
total_funding = sum(m['Amount'] for m in matched) + sum(u['Amount'] for u in unmatched)

result = {
    'num_projects_found_in_docs': num_projects,
    'total_funding_for_those_projects': total_funding,
    'projects': {
        'matched': matched,
        'unmatched': unmatched
    }
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SWdYhnNcnfGhyqygrmZo9Hum': ['civic_docs'], 'var_call_jMjslhGHl4uH9yM8CMklZCNe': ['Funding'], 'var_call_VRJfQzwEvGj1nReSJtvXQEzi': 'file_storage/call_VRJfQzwEvGj1nReSJtvXQEzi.json', 'var_call_RVk0cVgnA6ObHRufRtLeY0mk': 'file_storage/call_RVk0cVgnA6ObHRufRtLeY0mk.json'}

exec(code, env_args)

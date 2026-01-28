code = """import json, re

# Load the large query results from storage files
with open(var_call_ifKTd9m49wjLskHsH8IDbSh4, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_ZK1aX28h8MGo0W1v6MBLI9wZ, 'r') as f:
    funding_rows = json.load(f)

# Helper to normalize project names for matching
import string

def normalize_name(s):
    s = s.lower()
    # remove punctuation
    s = re.sub(r"[\(\)\.,'\"\-/&]", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

proj_set = set()

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if 'begin construction' in low:
            block = ' '.join(lines[i:i+4]).lower()
            # check if spring and 2022 appear in the same line/block
            if 'spring' in block and '2022' in block:
                # find project name above
                name = None
                for j in range(i-1, max(i-12, -1), -1):
                    candidate = lines[j].strip()
                    cl = candidate.lower()
                    if not candidate:
                        continue
                    if cl.startswith('(cid:'):
                        continue
                    if 'updates' in cl or 'project schedule' in cl or 'agenda' in cl or 'page' in cl:
                        continue
                    # Heuristic: project name line often contains letters and digits and is shorter than 200
                    if re.search('[a-zA-Z]', candidate) and len(candidate) < 200:
                        name = candidate
                        break
                if name:
                    proj_set.add(name.strip())

# As an additional heuristic, look for lines that explicitly mention "Begin Construction: Spring 2022" (exact phrase anywhere)
pattern_exact = re.compile(r"begin\s+construction\s*[:\-]?\s*spring\s*,?\s*2022", re.IGNORECASE)
for doc in civic_docs:
    text = doc.get('text','')
    for m in pattern_exact.finditer(text):
        # find position and then previous lines
        pos = m.start()
        # get substring up to pos and take last 300 chars, then split lines
        prior = text[:pos][-500:]
        prior_lines = prior.splitlines()
        # choose last non-empty line that looks like a title
        name = None
        for candidate in reversed(prior_lines):
            candidate = candidate.strip()
            if not candidate:
                continue
            if candidate.lower().startswith('(cid:'):
                continue
            if 'updates' in candidate.lower():
                continue
            if re.search('[a-zA-Z]', candidate) and len(candidate) < 200:
                name = candidate
                break
        if name:
            proj_set.add(name.strip())

# Prepare funding lookup
funding_list = funding_rows
# Normalize funding names
for r in funding_list:
    r['norm_name'] = normalize_name(r.get('Project_Name',''))

# Match projects to funding entries
matched_projects = []
project_funding_map = {}

for proj in sorted(proj_set):
    norm_proj = normalize_name(proj)
    total_for_proj = 0
    matched = False
    for r in funding_list:
        fn = r['norm_name']
        if norm_proj == fn or norm_proj in fn or fn in norm_proj:
            # parse amount
            amt_raw = str(r.get('Amount','0'))
            amt_digits = re.sub(r"[^0-9-]","", amt_raw)
            try:
                amt = int(amt_digits) if amt_digits not in ('','-') else 0
            except:
                amt = 0
            total_for_proj += amt
            matched = True
    if matched:
        project_funding_map[proj] = total_for_proj
        matched_projects.append(proj)

# Final counts
count_projects = len(project_funding_map)
total_funding = sum(project_funding_map.values())

# Prepare output
out = {"count": count_projects, "total_funding": total_funding, "projects": project_funding_map}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ifKTd9m49wjLskHsH8IDbSh4': 'file_storage/call_ifKTd9m49wjLskHsH8IDbSh4.json', 'var_call_ZK1aX28h8MGo0W1v6MBLI9wZ': 'file_storage/call_ZK1aX28h8MGo0W1v6MBLI9wZ.json'}

exec(code, env_args)

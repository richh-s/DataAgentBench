code = """import json, re

# Load data from storage files
with open(var_call_oM9fF0ceT8cpCIpTFp0douXc, 'r') as f:
    docs = json.load(f)
with open(var_call_8fzGQWMf0n1awFW2g5xDFjUd, 'r') as f:
    funding = json.load(f)

# Helper to find project title near a line index
stop_keywords = ['updates', 'project schedule', 'project description', 'recommended action',
                 'agenda', 'page', 'meeting date', 'date prepared', 'subject', 'discussion', 'approved by',
                 'prepared by']

candidates = []

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'spring\s*2022', line, re.I):
            # search backwards up to 15 lines for a likely project title
            title = None
            for j in range(i-1, max(i-16, -1), -1):
                l = lines[j].strip()
                if not l:
                    continue
                low = l.lower()
                if ':' in l:
                    continue
                if any(k in low for k in stop_keywords):
                    continue
                # Heuristic: require at least 2 words and contains letters
                words = re.findall(r"\w+", l)
                if len(words) < 2:
                    continue
                # Exclude lines that are all-caps headings like 'ITEM 4.B.' or 'PAGE 1 OF 6'
                if re.match(r'^[A-Z0-9\s\W]{3,}$', l) and l.upper()==l and len(l.split())<10:
                    continue
                title = l
                break
            if title:
                candidates.append(title)
            else:
                # try a broader regex: look back up to 200 chars to capture a preceding project-like phrase
                idx = text.lower().find('spring 2022')
                # find last uppercase-starting phrase before this occurrence within 300 chars
                pos = max(0, idx-300)
                window = text[pos:idx]
                m = re.findall(r"([A-Z][A-Za-z0-9\&\'\-\,\s]{5,120}(?:Project|Repairs|Improvements|Study|Park|Road|Facility|Project))", window)
                if m:
                    candidates.extend(m)

# Normalize candidates
norm_candidates = []
for c in candidates:
    c2 = ' '.join(c.split())
    # remove leading bullets or numbering
    c2 = re.sub(r'^[\d\)\.-]+\s*', '', c2)
    if c2 not in norm_candidates:
        norm_candidates.append(c2)

# Prepare funding matching
fund_rows = funding  # list of dicts

matched_funding_ids = set()
project_matches = {}

import math

def tokenize(s):
    return [t.lower() for t in re.findall(r"[A-Za-z0-9]+", s)]

for proj in norm_candidates:
    p_low = proj.lower()
    p_tokens = set(tokenize(proj))
    project_matches[proj] = []
    for row in fund_rows:
        fname = row.get('Project_Name','')
        f_low = fname.lower()
        # direct substring matches
        if p_low in f_low or f_low in p_low:
            project_matches[proj].append(row)
            matched_funding_ids.add(row.get('Funding_ID'))
            continue
        # token overlap heuristic
        f_tokens = set(tokenize(fname))
        if not p_tokens or not f_tokens:
            continue
        inter = p_tokens & f_tokens
        # require at least 2 tokens in common or >=50% of smaller set
        if len(inter) >= 2 or len(inter) >= 0.5 * min(len(p_tokens), len(f_tokens)):
            project_matches[proj].append(row)
            matched_funding_ids.add(row.get('Funding_ID'))

# Count projects (unique candidates found)
project_count = len(norm_candidates)

# Sum funding amounts for matched funding rows
total_funding = 0
matched_rows = []
for row in fund_rows:
    if row.get('Funding_ID') in matched_funding_ids:
        try:
            amt = int(row.get('Amount') if row.get('Amount') is not None else 0)
        except:
            try:
                amt = int(float(row.get('Amount')))
            except:
                amt = 0
        total_funding += amt
        matched_rows.append({'Funding_ID': row.get('Funding_ID'), 'Project_Name': row.get('Project_Name'), 'Amount': amt})

# Build result
result = {
    'project_count_identified': project_count,
    'total_funding_matched': total_funding,
    'identified_projects': norm_candidates,
    'matched_funding_records': matched_rows
}

# Print as required
print("----BEGIN PRINT FORMAT----")
print('print("__RESULT__:")')
print('print(\'' + json.dumps(result).replace("'", "\\'") + '\')')
print("----END PRINT FORMAT----")"""

env_args = {'var_call_90KW5gb5l0aKm4fGIQLSCn1V': ['civic_docs'], 'var_call_GNu0SDGXscZavzXu7agaWGPl': ['Funding'], 'var_call_oM9fF0ceT8cpCIpTFp0douXc': 'file_storage/call_oM9fF0ceT8cpCIpTFp0douXc.json', 'var_call_8fzGQWMf0n1awFW2g5xDFjUd': 'file_storage/call_8fzGQWMf0n1awFW2g5xDFjUd.json'}

exec(code, env_args)

code = """import json, re, pandas as pd

# Load data from stored files
with open(var_call_zQf7dbf5RqUPorcHIEOZ9aVd, 'r') as f:
    docs = json.load(f)
with open(var_call_nd22TlbmasvB6JYauGF7xowc, 'r') as f:
    funding_list = json.load(f)

funding_df = pd.DataFrame(funding_list)
# Ensure numeric
funding_df['TotalAmount'] = funding_df['TotalAmount'].astype(int)

# Pattern for spring 2022 mentions
pattern = re.compile(r"(Spring\s*2022|2022[-/]?\s*03|2022[-/]?\s*04|2022[-/]?\s*05|2022\s*March|2022\s*April|2022\s*May|2022\-03|2022\-04|2022\-05|2022\s*Mar|2022\s*Apr|2022\s*May)", re.IGNORECASE)

found_projects = []

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if pattern.search(line):
            # look back up to 10 lines to find a candidate project title
            candidate = None
            for j in range(max(0, i-10), i)[::-1]:
                l = lines[j].strip()
                if not l:
                    continue
                # skip lines that are obviously not titles
                low = l.lower()
                if low.startswith('page') or low.startswith('agenda') or low.startswith('item') or low.startswith('to:') or low.startswith('prepared') or low.startswith('approved') or low.startswith('subject'):
                    continue
                if low.startswith('(cid') or low.startswith('(') or low.startswith('updates') or low.startswith('project schedule') or low.startswith('project description') or low.startswith('project updates'):
                    continue
                # often titles are in Title Case and not too long
                if len(l) > 250:
                    continue
                # also skip lines that look like sentences (contain period)
                if '.' in l and len(l.split())>6:
                    continue
                candidate = l
                break
            if candidate:
                # clean candidate
                cand = candidate.strip(' :\t')
                # remove leading numbering if any
                cand = re.sub(r'^\d+\.\s*', '', cand)
                found_projects.append(cand)

# Deduplicate while preserving order
seen = set()
projects = []
for p in found_projects:
    np = re.sub(r'\s+', ' ', p).strip()
    if np.lower() not in seen:
        seen.add(np.lower())
        projects.append(np)

# Now match to funding table using normalized comparison
import string

def normalize(s):
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(r'\s+', ' ', s).strip()
    return s

funding_df['norm_name'] = funding_df['Project_Name'].apply(normalize)

project_funding_list = []
total_funding = 0
for p in projects:
    np = normalize(p)
    # exact norm match
    matches = funding_df[funding_df['norm_name'] == np]
    if matches.empty:
        # try substring match either way
        matches = funding_df[funding_df['norm_name'].str.contains(np, na=False)]
    if matches.empty:
        matches = funding_df[funding_df['norm_name'].apply(lambda x: np in x)]
    if matches.empty:
        amount = 0
        matched_names = []
    else:
        amount = int(matches['TotalAmount'].sum())
        matched_names = matches['Project_Name'].tolist()
    total_funding += amount
    project_funding_list.append({'project_name': p, 'matched_funding_amount': amount, 'matched_funding_records': matched_names})

result = {'num_projects_started_spring_2022': len(projects), 'total_funding': total_funding, 'projects': project_funding_list}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zQf7dbf5RqUPorcHIEOZ9aVd': 'file_storage/call_zQf7dbf5RqUPorcHIEOZ9aVd.json', 'var_call_fwLay9g5Xo1a02o1iz27bCwD': ['Funding'], 'var_call_nd22TlbmasvB6JYauGF7xowc': 'file_storage/call_nd22TlbmasvB6JYauGF7xowc.json'}

exec(code, env_args)

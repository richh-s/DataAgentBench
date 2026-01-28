code = """import json, re
from pathlib import Path

# Load previous tool results from storage file paths
with open(var_call_UHWAxyqZSqdjZJtNin5k3W9T, 'r') as f:
    funding_records = json.load(f)
with open(var_call_ld8UyhXz2PIqqwR7qTrjvLJX, 'r') as f:
    civic_docs = json.load(f)

# Process funding records: build set of project names with Amount > 50000
funding_df = funding_records
# Normalize funding project names by removing parenthetical suffixes and lowercasing
def normalize_name(n):
    if n is None:
        return None
    s = n.strip()
    # remove parenthetical content e.g., (FEMA Project)
    s = re.sub(r"\s*\([^)]*\)", "", s).strip()
    s = re.sub(r"\s+", " ", s)
    return s.lower()

funded_projects = set()
for r in funding_df:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_val = int(str(amt))
    except:
        try:
            amt_val = int(float(str(amt)))
        except:
            amt_val = 0
    if amt_val > 50000:
        nn = normalize_name(name)
        if nn:
            funded_projects.add(nn)

# Extract 'Design' capital projects from civic docs
# Heuristic: find sections labelled 'Capital Improvement Projects (Design)'
keywords = [
    'Project','Improvements','Repairs','Park','Road','Walkway','Study','Median',
    'Skate','Signs','Replacement','Biofilter','Traffic','Curb','Storm','Drain',
    'Walkway','Culvert','Bridge','HVAC','Roof','Playground','Slope','Resurfacing',
    'Drainage','Stormwater','Treatment'
]

design_projects = set()
for doc in civic_docs:
    text = doc.get('text','')
    # Normalize line endings
    lines = text.splitlines()
    # find indices of lines containing the design header
    for i,l in enumerate(lines):
        if 'capital improvement projects' in l.lower() and 'design' in l.lower():
            # iterate subsequent lines
            j = i+1
            while j < len(lines):
                line = lines[j].strip()
                low = line.lower()
                # stop conditions: next major section
                if 'capital improvement projects' in low and 'construction' in low:
                    break
                if 'capital improvement projects' in low and 'not started' in low:
                    break
                if re.match(r'^capital improvement projects', low):
                    break
                # skip empty and meta lines
                if not line:
                    j += 1
                    continue
                if line.endswith(':'):
                    j += 1
                    continue
                if line.startswith('(cid:') or line.startswith('('):
                    j += 1
                    continue
                if line.startswith('page') or line.lower().startswith('agenda'):
                    j += 1
                    continue
                # if the line looks like a project title based on keywords
                if any(k.lower() in low for k in keywords):
                    # stop if this line seems to be a paragraph (long and contains periods) but still could be title
                    # Take the line as project name
                    clean = re.sub(r"\s*\([^)]*\)", "", line).strip()
                    clean = re.sub(r"\s+", " ", clean)
                    # Exclude lines that are obviously not project names
                    if len(clean) > 3 and not re.search(r'updates|project schedule|meeting date|prepared by|approved by|recommended action|discussion|agenda item', clean, re.I):
                        design_projects.add(clean.lower())
                j += 1

# Normalize design project names (remove parentheticals already done)
norm_design = set()
for n in design_projects:
    nn = re.sub(r"\s*\([^)]*\)", "", n).strip()
    nn = re.sub(r"\s+", " ", nn)
    if nn:
        norm_design.add(nn)

# Now find intersection with funded_projects
matches = sorted(list(norm_design.intersection(funded_projects)))
count = len(matches)

# Prepare JSON-serializable result
result = {'count': count, 'projects': matches}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PtZuWRxH87Tgyayz9wtB5oJf': ['civic_docs'], 'var_call_CNKmF94n78t9OwXbUItUGYZA': ['Funding'], 'var_call_UHWAxyqZSqdjZJtNin5k3W9T': 'file_storage/call_UHWAxyqZSqdjZJtNin5k3W9T.json', 'var_call_ld8UyhXz2PIqqwR7qTrjvLJX': 'file_storage/call_ld8UyhXz2PIqqwR7qTrjvLJX.json'}

exec(code, env_args)

code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_4HdUiHnSFJBjIwK87YHCGUTC, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_wwbgDMXQ67DvK4hs4ybAOibf, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Prepare funding dict list with normalized names
import string

def normalize_name(s):
    if s is None:
        return ''
    s = s.lower()
    # remove content in parentheses
    s = re.sub(r"\([^)]*\)", "", s)
    # remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    # collapse whitespace
    s = re.sub(r"\s+", " ", s)
    s = s.strip()
    return s

funding = []
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_val = int(amt)
    except:
        try:
            amt_val = int(float(amt))
        except:
            amt_val = 0
    funding.append({'orig_name': name, 'name': normalize_name(name), 'amount': amt_val})

# Compile patterns for Spring 2022 detection
patterns = [r"spring\s*,?\s*2022", r"2022\s*-?\s*spring", r"2022-03", r"2022-04", r"2022-05",
            r"march\s*2022", r"april\s*2022", r"may\s*2022", r"03/2022", r"03-2022", r"2022/03"]
pat = re.compile("(" + ")|(".join(patterns) + ")", re.IGNORECASE)

extracted_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    # split into segments by two or more newlines
    segments = re.split(r"\n\s*\n+", text)
    for seg in segments:
        if pat.search(seg):
            # find first non-empty line as project name candidate
            lines = [ln.strip() for ln in seg.splitlines() if ln.strip()]
            if not lines:
                continue
            # Heuristic: project name is the first line unless it's generic like 'Updates:' or 'Discussion:'
            candidate = None
            for ln in lines[:5]:
                low = ln.lower()
                if any(x in low for x in ['updates', 'agenda', 'page', 'item', 'discussion', 'recommended action', 'subject', 'meeting date']):
                    continue
                candidate = ln
                break
            if not candidate:
                candidate = lines[0]
            # Clean candidate
            candidate_clean = re.sub(r"\s+", " ", candidate).strip()
            # Avoid lines that are too short or clearly not project names
            if len(candidate_clean) < 3:
                continue
            extracted_projects.append(candidate_clean)

# Deduplicate preserving order
seen = set()
projects = []
for p in extracted_projects:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        projects.append(p)

# Now match projects to funding entries
matches = {}
for p in projects:
    np = normalize_name(p)
    total_amt = 0
    matched_entries = []
    for f in funding:
        if np and (np in f['name'] or f['name'] in np):
            total_amt += f['amount']
            matched_entries.append(f['orig_name'])
    matches[p] = {'matched_funding_sum': total_amt, 'matched_funding_projects': matched_entries}

# Count projects and sum funding
project_count = len(projects)
total_funding = sum(v['matched_funding_sum'] for v in matches.values())

# Prepare result
result = {'projects_count': project_count, 'total_funding': total_funding, 'projects_detail': matches}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_S3MK3XxRWpjcrpcZo6SEYkoA': ['civic_docs'], 'var_call_124Wlw9LcWtohjHmorwIF8ck': ['Funding'], 'var_call_4HdUiHnSFJBjIwK87YHCGUTC': 'file_storage/call_4HdUiHnSFJBjIwK87YHCGUTC.json', 'var_call_wwbgDMXQ67DvK4hs4ybAOibf': 'file_storage/call_wwbgDMXQ67DvK4hs4ybAOibf.json'}

exec(code, env_args)

code = """import json, re

# Load data from storage-provided file paths
with open(var_call_q7R3xqp8WG9IOZBRlFr8pyIy, 'r') as f:
    funding = json.load(f)
with open(var_call_QzBZclHwTrrUNkhyo5VjgzV8, 'r') as f:
    civic_docs = json.load(f)

# Combine all civic text into one big string for searching
all_text = "\n".join([d.get('text','') for d in civic_docs])
all_text_lower = all_text.lower()

# Disaster keywords to identify disaster-related funding records
disaster_kw = re.compile(r"\b(fema|caloes|caljpia|disaster|fire|fema/|fema)\b", re.I)

# Helper to get base name before any parenthesis
def base_name(name):
    return re.split(r"\(|-", name)[0].strip()

candidates = []
for rec in funding:
    name = rec.get('Project_Name','')
    # If funding entry name itself mentions disaster keywords, consider it candidate
    if disaster_kw.search(name):
        candidates.append(rec)
    else:
        # also consider names that contain common disaster topics
        if re.search(r"\b(guardrail|culvert|storm drain|drainage|road repairs|slope repairs|retaining wall|bridge|water quality)\b", name, re.I):
            # we'll include these only if civic docs show disaster context; mark for further checking
            candidates.append(rec)

# For each candidate, check civic docs for occurrence of project name or base name with '2022' nearby
results = []
for rec in candidates:
    name = rec.get('Project_Name','')
    name_lower = name.lower()
    bname = base_name(name).lower()
    found = False
    found_year = False
    # search for exact project name or base name in civic text
    idx = all_text_lower.find(name_lower)
    if idx == -1 and bname:
        idx = all_text_lower.find(bname)
    if idx != -1:
        found = True
        # context window
        start = max(0, idx-300)
        end = min(len(all_text_lower), idx+300)
        context = all_text_lower[start:end]
        if '2022' in context:
            found_year = True
    else:
        # not found by exact names; try token presence of important words from name
        tokens = re.findall(r"[A-Za-z]{4,}", bname)
        # try to find any two-token sequence
        for i in range(len(tokens)-1):
            seq = tokens[i] + ' ' + tokens[i+1]
            if seq in all_text_lower:
                idx = all_text_lower.find(seq)
                found = True
                start = max(0, idx-300)
                end = min(len(all_text_lower), idx+300)
                context = all_text_lower[start:end]
                if '2022' in context:
                    found_year = True
                break
    results.append({'record': rec, 'mentioned_in_docs': found, 'year2022_nearby': found_year})

# Sum amounts for those that are disaster-related (based on name keywords) AND have year2022_nearby True
total = 0
included_projects = []
for r in results:
    rec = r['record']
    if r['year2022_nearby']:
        try:
            amt = int(rec.get('Amount') or 0)
        except:
            # remove commas
            amt = int(re.sub(r'[^0-9]','', str(rec.get('Amount') or '0')) or 0)
        total += amt
        included_projects.append({'Project_Name': rec.get('Project_Name'), 'Amount': amt})

# As a fallback: if none matched by this method but there are clear disaster mentions in civic docs listing projects under Disaster Recovery Projects for 2022,
# we could try to look for project names listed in sections under 'Disaster Recovery' and then match funding. But use current total.

output = {'total_funding_disaster_projects_started_2022': total, 'included_funding_records': included_projects}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_xHNly7z1Fzv5N8jwdK3mtrAL': ['civic_docs'], 'var_call_jRI4KvDQihFoo9gBTqySXjRT': ['Funding'], 'var_call_q7R3xqp8WG9IOZBRlFr8pyIy': 'file_storage/call_q7R3xqp8WG9IOZBRlFr8pyIy.json', 'var_call_QzBZclHwTrrUNkhyo5VjgzV8': 'file_storage/call_QzBZclHwTrrUNkhyo5VjgzV8.json'}

exec(code, env_args)

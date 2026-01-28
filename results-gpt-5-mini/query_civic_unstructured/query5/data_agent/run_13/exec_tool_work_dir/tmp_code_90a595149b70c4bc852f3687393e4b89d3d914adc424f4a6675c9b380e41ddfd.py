code = """import json, re

# Load previous tool results from storage variables
funding_path = var_call_5bTpei777tnyEwOoHrzoqjsN
civic_docs_path = var_call_v3QtXqLSAoVAAsdW3jdtOTEz

with open(funding_path, 'r') as f:
    funding = json.load(f)
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts to int
for r in funding:
    try:
        r['TotalAmount'] = int(r['TotalAmount'])
    except:
        # fallback if string contains commas
        r['TotalAmount'] = int(re.sub(r"[^0-9]", "", str(r.get('TotalAmount', '0'))))

# Candidate disaster keywords
keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'woolsey', 'fire', 'emergency']

# Prepare civic docs text concatenation for searching
# We'll search each doc individually
civic_texts = [d.get('text','') for d in civic_docs]

matched = []

for rec in funding:
    name = rec.get('Project_Name','')
    name_l = name.lower()
    # Check if funding project name indicates disaster via keywords
    if any(k in name_l for k in keywords):
        # Create base name by removing parenthetical suffixes
        base = re.sub(r"\s*\([^)]*\)", "", name).strip()
        base_l = base.lower()
        found_2022 = False
        # search in civic docs for name or base name
        for text in civic_texts:
            t_l = text.lower()
            # search for full name first, then base
            for pattern in [name_l, base_l]:
                if not pattern:
                    continue
                idx = t_l.find(pattern)
                if idx != -1:
                    # get surrounding snippet
                    start = max(0, idx-300)
                    end = min(len(t_l), idx+len(pattern)+300)
                    snippet = t_l[start:end]
                    if '2022' in snippet:
                        found_2022 = True
                        break
                    # as fallback, look for 'begin'/'start' within snippet plus '2022'
                    if re.search(r"(begin|start|project schedule|project will|project schedule:)", snippet) and '2022' in t_l[max(0, idx-1000):min(len(t_l), idx+1000)]:
                        found_2022 = True
                        break
            if found_2022:
                break
        if found_2022:
            matched.append({'Project_Name': name, 'Base_Name': base, 'Amount': rec['TotalAmount']})

# Additionally, there may be disaster projects without explicit keywords in funding names
# We'll also scan civic docs for mentions of 'Disaster Recovery' and extract nearby project names
# Simple heuristic: find lines under 'Disaster Recovery Projects' section and extract capitalized project lines ending with 'Project' or similar
additional_matches = []
for doc in civic_docs:
    text = doc.get('text','')
    t_l = text.lower()
    if 'disaster recovery' in t_l or 'disaster recovery projects' in t_l:
        # split into lines and find candidate project lines
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if re.search(r"project", line, re.IGNORECASE) and any(k in line.lower() for k in ['fema','caloes','caljpia','disaster','fire']):
                # extract project name heuristically
                candidate = re.sub(r"[^\w\s\(\)\-/,&.]", '', line).strip()
                # try match to funding table entries by substring
                for rec in funding:
                    if candidate and candidate.lower() in rec['Project_Name'].lower():
                        # check 2022 in nearby lines
                        context = '\n'.join(lines[max(0,i-3):i+4]).lower()
                        if '2022' in context:
                            if not any(m['Project_Name']==rec['Project_Name'] for m in matched):
                                additional_matches.append({'Project_Name': rec['Project_Name'], 'Base_Name': rec['Project_Name'], 'Amount': rec['TotalAmount']})

# Combine matched and additional_matches
all_matches = {m['Project_Name']: m for m in matched}
for m in additional_matches:
    all_matches[m['Project_Name']] = m

matched_list = list(all_matches.values())

total = sum(m['Amount'] for m in matched_list)

# Prepare result
result = {'total_disaster_funding_started_2022': total, 'matched_projects': matched_list}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HlLq4TH1LZBMTIGorZ4YldDZ': ['Funding'], 'var_call_rD258WLarCW4yILJiRDBIw8J': ['civic_docs'], 'var_call_v3QtXqLSAoVAAsdW3jdtOTEz': 'file_storage/call_v3QtXqLSAoVAAsdW3jdtOTEz.json', 'var_call_5bTpei777tnyEwOoHrzoqjsN': 'file_storage/call_5bTpei777tnyEwOoHrzoqjsN.json'}

exec(code, env_args)

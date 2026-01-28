code = """import json, re
# Load data from storage-provided file paths
with open(var_call_iSPtBLAw7MkeNDClZKq7ZGgp, 'r') as f:
    funding_data = json.load(f)
with open(var_call_jKcieENqqTuB2STtGsegOtdh, 'r') as f:
    civic_docs = json.load(f)

# Prepare funding records: Project_Name and Total_Amount as int
funding_records = []
for r in funding_data:
    name = r.get('Project_Name')
    amt = r.get('Total_Amount')
    try:
        amt_i = int(amt)
    except:
        try:
            amt_i = int(float(amt))
        except:
            amt_i = 0
    funding_records.append({'Project_Name': name, 'Amount': amt_i})

# Prepare civic texts
texts = [d.get('text','') for d in civic_docs]
all_text = "\n\n".join(texts).lower()

# Helper functions
def normalize(name):
    if not name:
        return ''
    s = name
    # remove parenthetical suffixes
    s = re.sub(r"\(.*?\)", "", s)
    # remove the word 'project' and excess whitespace
    s = re.sub(r"\bproject\b", "", s, flags=re.I)
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s.lower()

# Keywords for disaster identification
disaster_keywords = ['fema', 'caloes', 'cal o es', 'caljpia', 'disaster', 'fire', 'woolsey', 'federal assistance', 'emergency', 'recovery']

# Identify projects that are disaster-related and started in 2022
included_projects = []
for rec in funding_records:
    name = rec['Project_Name']
    name_low = (name or '').lower()
    norm = normalize(name)
    started_2022 = False
    is_disaster = False

    # If project name explicitly contains 2022, mark started_2022
    if '2022' in name_low:
        started_2022 = True

    # If project name contains disaster keywords, mark disaster
    for kw in disaster_keywords:
        if kw in name_low:
            is_disaster = True
            break

    # Search for occurrences in civic docs
    for txt in texts:
        t = txt.lower()
        # look for exact or normalized name in text
        found = False
        if norm and norm in t:
            found = True
            idx = t.find(norm)
            start = max(0, idx-400)
            end = min(len(t), idx+400)
            window = t[start:end]
        else:
            # try matching significant tokens from name
            tokens = [tok for tok in norm.split() if len(tok)>3]
            if tokens:
                # check if majority of tokens appear nearby
                # rough approach: check if first token in text
                for tok in tokens:
                    if tok in t:
                        idx = t.find(tok)
                        start = max(0, idx-400)
                        end = min(len(t), idx+400)
                        window = t[start:end]
                        # ensure other tokens present in window
                        if all(tok2 in window for tok2 in tokens[:3]):
                            found = True
                            break
        if found:
            # check for 2022 in window
            if '2022' in window:
                started_2022 = True
            # check disaster keywords in window
            for kw in disaster_keywords:
                if kw in window:
                    is_disaster = True
                    break
        # if both flags true we can stop
        if started_2022 and is_disaster:
            break

    # Additional heuristic: if not found in civic docs but project name has parenthetical like '(FEMA' etc, we treated earlier
    if started_2022 and is_disaster:
        included_projects.append(rec)

# Sum amounts
total = sum(r['Amount'] for r in included_projects)

# Prepare output
out = {'total_disaster_projects_started_2022': total, 'matched_projects_count': len(included_projects), 'matched_projects': [r['Project_Name'] for r in included_projects]}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_jllSd3KeQpuvBLNBHoOhYQUV': ['civic_docs'], 'var_call_Hi40kBUCCDIT6YasqyyCJqXH': ['Funding'], 'var_call_jKcieENqqTuB2STtGsegOtdh': 'file_storage/call_jKcieENqqTuB2STtGsegOtdh.json', 'var_call_iSPtBLAw7MkeNDClZKq7ZGgp': 'file_storage/call_iSPtBLAw7MkeNDClZKq7ZGgp.json'}

exec(code, env_args)

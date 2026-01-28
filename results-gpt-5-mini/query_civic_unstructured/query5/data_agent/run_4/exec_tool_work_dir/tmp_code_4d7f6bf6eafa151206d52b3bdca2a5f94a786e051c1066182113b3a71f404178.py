code = """import json, re
# Read stored query results from file paths provided by previous tool calls
fd_path = var_call_iSPtBLAw7MkeNDClZKq7ZGgp
cd_path = var_call_jKcieENqqTuB2STtGsegOtdh
with open(fd_path, 'r') as f:
    funding_data = json.load(f)
with open(cd_path, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts
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

# Combine civic texts
texts = [d.get('text','') for d in civic_docs]

# Normalization helper
def normalize(name):
    if not name:
        return ''
    s = name
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\bproject\b", "", s, flags=re.I)
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s.lower()

# Keywords indicating disaster
disaster_keywords = ['fema', 'caloes', 'cal o es', 'caljpia', 'disaster', 'fire', 'woolsey', 'federal assistance', 'emergency', 'recovery']

included_projects = []
for rec in funding_records:
    name = rec['Project_Name'] or ''
    name_low = name.lower()
    norm = normalize(name)
    started_2022 = False
    is_disaster = False

    if '2022' in name_low:
        started_2022 = True
    for kw in disaster_keywords:
        if kw in name_low:
            is_disaster = True
            break

    # search in civic documents
    for txt in texts:
        t = txt.lower()
        if not t:
            continue
        found = False
        if norm and norm in t:
            found = True
            idx = t.find(norm)
            start = max(0, idx-400)
            end = min(len(t), idx+400)
            window = t[start:end]
        else:
            tokens = [tok for tok in norm.split() if len(tok)>3]
            if tokens:
                for tok in tokens:
                    if tok in t:
                        idx = t.find(tok)
                        start = max(0, idx-400)
                        end = min(len(t), idx+400)
                        window = t[start:end]
                        if all(tok2 in window for tok2 in tokens[:3]):
                            found = True
                            break
        if found:
            if '2022' in window:
                started_2022 = True
            for kw in disaster_keywords:
                if kw in window:
                    is_disaster = True
                    break
        if started_2022 and is_disaster:
            break

    if started_2022 and is_disaster:
        included_projects.append(rec)

total = sum(r['Amount'] for r in included_projects)

out = {'total_disaster_projects_started_2022': total, 'matched_projects_count': len(included_projects), 'matched_projects': [r['Project_Name'] for r in included_projects]}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_jllSd3KeQpuvBLNBHoOhYQUV': ['civic_docs'], 'var_call_Hi40kBUCCDIT6YasqyyCJqXH': ['Funding'], 'var_call_jKcieENqqTuB2STtGsegOtdh': 'file_storage/call_jKcieENqqTuB2STtGsegOtdh.json', 'var_call_iSPtBLAw7MkeNDClZKq7ZGgp': 'file_storage/call_iSPtBLAw7MkeNDClZKq7ZGgp.json'}

exec(code, env_args)

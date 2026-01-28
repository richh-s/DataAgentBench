code = """import json, re, pandas as pd
# Load data
with open(var_call_7wrRvou0OCXa9djFG0KR3940, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_UyOFX4B0XwW3mB89jITEtNdZ, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# DataFrame for funding
df_f = pd.DataFrame(funding)
# Ensure Amount is int
df_f['Amount'] = df_f['Amount'].astype(int)

# Helper to strip parentheses suffix
def base_name(name):
    return re.sub(r"\s*\([^)]*\)", "", name).strip()

# Disaster keywords
disaster_kw = ["fema", "caloes", "caljpia", "disaster", "fire", "emergency", "woolsey"]

# For each funding project, search civic docs
proj_info = {}
for idx, row in df_f.iterrows():
    pname = row['Project_Name']
    bn = base_name(pname)
    proj_info[pname] = {'found': False, 'is_disaster': False, 'started_2022': False, 'contexts': []}
    pattern = re.compile(re.escape(bn), re.IGNORECASE)
    for doc in civic_docs:
        text = doc.get('text','')
        for m in pattern.finditer(text):
            proj_info[pname]['found'] = True
            start = max(0, m.start()-300)
            end = min(len(text), m.end()+300)
            context = text[start:end]
            proj_info[pname]['contexts'].append(context)
            lc = context.lower()
            # disaster detection
            if any(kw in lc for kw in disaster_kw):
                proj_info[pname]['is_disaster'] = True
            # started in 2022 detection: look for 'begin construction' near 2022
            if '2022' in lc:
                if 'begin construction' in lc or re.search(r"begin\s*:\s*.*2022", lc) or re.search(r"begin construction:\s*.*(spring|summer|fall|winter)\s*2022", lc) or re.search(r"advertise:\s*.*2022", lc):
                    proj_info[pname]['started_2022'] = True

# Also check for 'Disaster Recovery Projects' sections
for doc in civic_docs:
    text = doc.get('text','')
    m = re.search(r"Disaster Recovery Projects", text, re.IGNORECASE)
    if m:
        section = text[m.end(): m.end()+2000].lower()
        for pname in proj_info.keys():
            bn = base_name(pname)
            if re.search(re.escape(bn), section, re.IGNORECASE):
                proj_info[pname]['is_disaster'] = True

# Now match funding rows where project marked disaster and started_2022
matched_records = []
for idx, row in df_f.iterrows():
    pname = row['Project_Name']
    amount = int(row['Amount'])
    info = proj_info.get(pname)
    if info and info['is_disaster'] and info['started_2022']:
        matched_records.append({'Funding_ID': row['Funding_ID'], 'Project_Name': pname, 'Amount': amount})
    else:
        # try base name matching across projects
        bn = base_name(pname)
        for other in proj_info.keys():
            if base_name(other).lower() == bn.lower():
                info2 = proj_info[other]
                if info2['is_disaster'] and info2['started_2022']:
                    matched_records.append({'Funding_ID': row['Funding_ID'], 'Project_Name': pname, 'Amount': amount, 'matched_to': other})
                    break

# Sum
total = sum(r['Amount'] for r in matched_records)

out = {'total_funding': total, 'matched_count': len(matched_records), 'matched_records': matched_records}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_UyOFX4B0XwW3mB89jITEtNdZ': 'file_storage/call_UyOFX4B0XwW3mB89jITEtNdZ.json', 'var_call_7wrRvou0OCXa9djFG0KR3940': 'file_storage/call_7wrRvou0OCXa9djFG0KR3940.json'}

exec(code, env_args)

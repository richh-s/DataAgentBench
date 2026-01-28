code = """import json, re, pandas as pd
# Load data from storage paths
with open(var_call_7wrRvou0OCXa9djFG0KR3940, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_UyOFX4B0XwW3mB89jITEtNdZ, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# DataFrames
df_f = pd.DataFrame(funding)
# Convert Amount to int
df_f['Amount'] = df_f['Amount'].astype(int)

# Prepare project name set from funding
proj_names = df_f['Project_Name'].unique().tolist()

# Normalize function
def base_name(name):
    m = re.match(r"^(.*?)\s*\(", name)
    return m.group(1).strip() if m else name.strip()

# Prepare mapping for discovered project info
proj_info = {name: {'found': False, 'is_disaster': False, 'started_2022': False, 'contexts': []} for name in proj_names}

# disaster keywords
disaster_kw = ["fema", "caloes", "caljpia", "disaster", "fire", "emergency", "woolsey", "fema/", "fema)"]

# Patterns to detect begin/start in 2022
begin_patterns = [r"Begin Construction:.*2022", r"Begin Construction:.*2022", r"Begin Construction:.*(Spring|Summer|Fall|Winter) 2022",
                  r"Begin Construction:.*[A-Za-z]+ 2022", r"Begin:.*2022", r"Begin Construction:\s*(Spring|Summer|Fall|Winter) 2022",
                  r"Advertise:.*2022", r"Begin Construction:.*2022", r"Construction was started.*2022", r"Start:.*2022"]
# compile
begin_regex = re.compile("(" + "|".join([p.replace("\", "\\") for p in [r"Begin Construction:.*2022", r"Begin Construction:.*(Spring|Summer|Fall|Winter) 2022", r"Begin Construction:.*[A-Za-z]+ 2022", r"Begin:.*2022", r"Start:.*2022", r"Begin Construction:.*2022", r"Advertise:.*2022"])]) + ")", re.IGNORECASE)
# Simpler: we'll check for 'Begin Construction' and '2022' in same context, or 'Begin' and '2022'

for doc in civic_docs:
    text = doc.get('text','')
    lower_text = text.lower()
    for pname in proj_names:
        found = False
        # try full name
        if re.search(re.escape(pname), text, flags=re.IGNORECASE):
            found = True
            m = re.search(re.escape(pname), text, flags=re.IGNORECASE)
        else:
            # try base name
            bn = base_name(pname)
            if bn and re.search(re.escape(bn), text, flags=re.IGNORECASE):
                found = True
                m = re.search(re.escape(bn), text, flags=re.IGNORECASE)
            else:
                m = None
        if found and m:
            context = text[max(0, m.start()-300): m.end()+300]
            info = proj_info[pname]
            info['found'] = True
            info['contexts'].append(context)
            lc = context.lower()
            # disaster check
            if any(kw in lc for kw in disaster_kw):
                info['is_disaster'] = True
            # check for Begin Construction + 2022 within context
            if 'begin construction' in lc and '2022' in lc:
                info['started_2022'] = True
            # also check for patterns like 'begin construction: fall 2022' or 'advertise: fall 2022'
            if re.search(r"begin construction:.*2022", lc) or re.search(r"begin construction:.*(spring|summer|fall|winter) 2022", lc) or re.search(r"advertise:.*2022", lc):
                info['started_2022'] = True
            # check for lines like 'begin construction: fall 2022' with various spacing
            if re.search(r"begin\s+construction\s*:.*2022", lc):
                info['started_2022'] = True
            # check for 'begin:' with 2022
            if re.search(r"begin\s*:\s*.*2022", lc):
                info['started_2022'] = True

# Also, sometimes project is labeled under 'Disaster Recovery Projects' heading; mark all projects appearing under that heading
for doc in civic_docs:
    text = doc.get('text','')
    # find position of 'Disaster Recovery Projects' or similar
    m = re.search(r"Disaster Recovery Projects", text, flags=re.IGNORECASE)
    if m:
        # take following 2000 chars
        section = text[m.end(): m.end()+2000].lower()
        for pname in proj_names:
            bn = base_name(pname)
            if re.search(re.escape(bn), section, flags=re.IGNORECASE):
                proj_info[pname]['is_disaster'] = True

# Now, determine which funding records correspond to projects that are disaster and started_2022
matched_records = []
for idx, row in df_f.iterrows():
    pname = row['Project_Name']
    amount = int(row['Amount'])
    # check direct
    info = proj_info.get(pname)
    matched = False
    if info and info['is_disaster'] and info['started_2022']:
        matched = True
        matched_records.append({'Funding_ID': row['Funding_ID'], 'Project_Name': pname, 'Amount': amount, 'matched_name': pname})
    else:
        # try base name
        bn = base_name(pname)
        # find any proj_info entry whose base matches bn
        for other in proj_names:
            if base_name(other).lower() == bn.lower():
                info2 = proj_info.get(other)
                if info2 and info2['is_disaster'] and info2['started_2022']:
                    matched = True
                    matched_records.append({'Funding_ID': row['Funding_ID'], 'Project_Name': pname, 'Amount': amount, 'matched_name': other})
                    break
        # also try matching bn in any proj_info contexts
        if not matched:
            for other in proj_names:
                if re.search(re.escape(bn), ' '.join(proj_info[other]['contexts']), flags=re.IGNORECASE):
                    info2 = proj_info.get(other)
                    if info2 and info2['is_disaster'] and info2['started_2022']:
                        matched = True
                        matched_records.append({'Funding_ID': row['Funding_ID'], 'Project_Name': pname, 'Amount': amount, 'matched_name': other})
                        break

# Sum amounts
total = sum(r['Amount'] for r in matched_records)

# Prepare output
out = {'total_funding': total, 'matched_count': len(matched_records), 'matched_records': matched_records}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_UyOFX4B0XwW3mB89jITEtNdZ': 'file_storage/call_UyOFX4B0XwW3mB89jITEtNdZ.json', 'var_call_7wrRvou0OCXa9djFG0KR3940': 'file_storage/call_7wrRvou0OCXa9djFG0KR3940.json'}

exec(code, env_args)

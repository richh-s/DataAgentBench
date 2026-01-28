code = """import json, re, pandas as pd

# Load data files from storage paths
with open(var_call_kYr0scjoSRkupx1549fyWvIy, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_jh3XKI5dJrA4acAmQLIT3BwR, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding dataframe
df = pd.DataFrame(funding)
# Ensure Amount is int
df['Amount'] = df['Amount'].astype(int)

# Identify candidate disaster-related funding rows by name or funding source
disaster_pattern = re.compile(r'FEMA|CalOES|CalJPIA|FEMA/CalOES', re.IGNORECASE)
funding_source_pattern = re.compile(r'Federal Assistance|Federal', re.IGNORECASE)

candidate_mask = df['Project_Name'].str.contains(disaster_pattern) | df['Funding_Source'].str.contains(funding_source_pattern, na=False)
candidates = df[candidate_mask].copy()

matched_rows = []

# Helper to get base project name (strip parenthetical suffixes)
def base_name(name):
    return re.sub(r"\s*\(.*?\)", "", name).strip()

# Pre-concatenate all civic docs texts for searching convenience
all_text = '\n'.join([doc.get('text','') for doc in civic_docs])
all_text_lower = all_text.lower()

for idx, row in candidates.iterrows():
    pname = row['Project_Name']
    bname = base_name(pname)
    if not bname:
        continue
    # search for base name in all_text
    idx_found = all_text_lower.find(bname.lower())
    found_2022 = False
    context = None
    if idx_found != -1:
        start = max(0, idx_found-200)
        end = min(len(all_text), idx_found + len(bname) + 200)
        context = all_text[start:end]
        if '2022' in context:
            found_2022 = True
    # Also check filename fields in civic docs for 2022
    if not found_2022:
        for doc in civic_docs:
            if bname.lower() in doc.get('text','').lower():
                # check nearby for 2022
                t = doc.get('text','')
                i = t.lower().find(bname.lower())
                if i != -1:
                    s = max(0, i-200)
                    e = min(len(t), i+len(bname)+200)
                    if '2022' in t[s:e]:
                        found_2022 = True
                        context = t[s:e]
                        break
            # check filename
            if '2022' in doc.get('filename','') and bname.lower() in doc.get('text','').lower():
                found_2022 = True
                context = '(found in file: '+doc.get('filename','')+')'
                break
    if found_2022:
        matched_rows.append({
            'Funding_ID': int(row['Funding_ID']),
            'Project_Name': row['Project_Name'],
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']),
            'Matched_Context_Snippet': context if context is not None else ''
        })

# Additionally, there may be disaster projects without explicit FEMA/CalOES in funding table but whose names appear in civic docs under a Disaster Recovery Projects section with 2022 dates.
# To catch more, scan civic docs for occurrences of 'Disaster' or 'Disaster Recovery' and extract nearby capitalized project-like phrases, then match funding rows by base name.

# Find indices of 'Disaster Recovery' occurrences
disaster_matches = []
for doc in civic_docs:
    txt = doc.get('text','')
    for m in re.finditer(r'Disaster Recovery Projects|Disaster Recovery|Disaster', txt, re.IGNORECASE):
        s = max(0, m.start()-500)
        e = min(len(txt), m.end()+500)
        snippet = txt[s:e]
        # look for project-like lines in snippet: lines with title case and may contain words and numbers
        lines = [ln.strip() for ln in re.split(r'\n+', snippet) if ln.strip()]
        for ln in lines:
            # Heuristic: line contains words and at least one digit or a known project keyword
            if len(ln) > 5 and re.search(r'\b(project|repair|repairs|improvements|road|drain|culvert|bridge|beach|walkway|slope|roadway)\b', ln, re.IGNORECASE):
                disaster_matches.append(ln)

# Try to match these disaster_matches to funding table entries (by base name substring)
for dm in disaster_matches:
    for idx, row in df.iterrows():
        bname = base_name(row['Project_Name'])
        if bname and bname.lower() in dm.lower():
            # check if 2022 is in dm
            if '2022' in dm or '2022' in all_text:
                # include if not already present
                if not any(m['Funding_ID'] == int(row['Funding_ID']) for m in matched_rows):
                    matched_rows.append({
                        'Funding_ID': int(row['Funding_ID']),
                        'Project_Name': row['Project_Name'],
                        'Funding_Source': row['Funding_Source'],
                        'Amount': int(row['Amount']),
                        'Matched_Context_Snippet': dm
                    })

# Sum amounts
total = sum(m['Amount'] for m in matched_rows)

# Prepare result
result = {
    'total_disaster_funding_started_in_2022': total,
    'matched_funding_rows_count': len(matched_rows),
    'matched_rows': matched_rows
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LNP4ZyjRTM1X5aZ3RtzWo5HY': ['civic_docs'], 'var_call_kYr0scjoSRkupx1549fyWvIy': 'file_storage/call_kYr0scjoSRkupx1549fyWvIy.json', 'var_call_jh3XKI5dJrA4acAmQLIT3BwR': 'file_storage/call_jh3XKI5dJrA4acAmQLIT3BwR.json'}

exec(code, env_args)

code = """import json
import re
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_Kh4pJSIR5TK5dytVJwi04v4T, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_mYCVhIDE3PQLGrX2Q8yp2mkS, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
df = pd.DataFrame(funding)
# Ensure correct types
if 'Amount' in df.columns:
    df['Amount'] = df['Amount'].astype(int)
else:
    df['Amount'] = 0

# Prepare civic docs text
docs = []
for d in civic_docs:
    text = d.get('text','')
    filename = d.get('filename','')
    docs.append({'filename': filename, 'text': text.lower()})

# Define disaster triggers
triggers = ['fema','caloes','cal-oes','cal o es','caljpia','disaster','fire','woolsey','emergency','recovery']

matched_rows = []

for idx, row in df.iterrows():
    pname = str(row.get('Project_Name',''))
    pname_l = pname.lower()
    is_disaster = any(t in pname_l for t in triggers)
    start_in_2022 = '2022' in pname_l

    # search in docs
    for doc in docs:
        txt = doc['text']
        if pname_l.strip() == '':
            continue
        if pname_l in txt:
            # mark disaster if triggers in nearby context or doc-level indicators
            occ = txt.find(pname_l)
            # context window
            start = max(0, occ-500)
            end = min(len(txt), occ+500)
            context = txt[start:end]
            if any(t in context for t in triggers):
                is_disaster = True
            # check for 'disaster recovery projects' heading in doc
            if 'disaster recovery' in txt or 'disaster recovery projects' in txt:
                # if project mentioned in doc and doc relates to disaster, mark disaster
                is_disaster = True
            # check for 2022 in context
            if '2022' in context:
                start_in_2022 = True
            # Also check for common date phrases near project
            date_patterns = [r'begin construction[:\s]*[^\n]{0,60}2022', r'complete construction[:\s]*[^\n]{0,60}2022', r'project schedule[:\s\S]{0,200}2022', r'advertise[:\s]*[^\n]{0,60}2022']
            for pat in date_patterns:
                if re.search(pat, context, flags=re.IGNORECASE):
                    start_in_2022 = True
            # if we've found mention, no need to check other docs
            # but continue to collect additional evidence across docs

    if is_disaster and start_in_2022:
        matched_rows.append({'Funding_ID': row.get('Funding_ID'), 'Project_Name': pname, 'Amount': int(row.get('Amount',0))})

total = sum(r['Amount'] for r in matched_rows)

# Prepare result
result = {'total_funding_for_disaster_projects_started_in_2022': total, 'matched_projects': matched_rows}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Ss7VhtPklvfFHAvQC6pL7yFl': ['civic_docs'], 'var_call_QZ53J9sniSJpXSfsqqo4CkT9': ['Funding'], 'var_call_Kh4pJSIR5TK5dytVJwi04v4T': 'file_storage/call_Kh4pJSIR5TK5dytVJwi04v4T.json', 'var_call_mYCVhIDE3PQLGrX2Q8yp2mkS': 'file_storage/call_mYCVhIDE3PQLGrX2Q8yp2mkS.json'}

exec(code, env_args)

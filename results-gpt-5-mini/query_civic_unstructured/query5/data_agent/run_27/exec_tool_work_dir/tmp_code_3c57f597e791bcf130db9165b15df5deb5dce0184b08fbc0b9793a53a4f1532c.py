code = """import json
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
triggers = ['fema', 'caloes', 'cal-oes', 'cal o es', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency', 'recovery']

matched_rows = []

for idx, row in df.iterrows():
    pname = str(row.get('Project_Name',''))
    pname_l = pname.lower()
    is_disaster = any(t in pname_l for t in triggers)
    start_in_2022 = ('2022' in pname_l) or ('2022' in str(row.get('Funding_ID','')))

    # search in docs for mentions
    if pname_l.strip() != '':
        for doc in docs:
            txt = doc['text']
            if pname_l in txt:
                occ = txt.find(pname_l)
                start = max(0, occ-200)
                end = min(len(txt), occ+200)
                context = txt[start:end]
                # check triggers in context or doc
                if any(t in context for t in triggers):
                    is_disaster = True
                if any(t in txt for t in triggers):
                    # if doc contains disaster words, mark disaster
                    is_disaster = True
                # check for 2022 near occurrence or in filename
                if '2022' in context or '2022' in doc['filename']:
                    start_in_2022 = True

    if is_disaster and start_in_2022:
        matched_rows.append({'Funding_ID': row.get('Funding_ID'), 'Project_Name': pname, 'Amount': int(row.get('Amount',0))})

total = sum(r['Amount'] for r in matched_rows)

result = {'total_funding_for_disaster_projects_started_in_2022': total, 'matched_projects': matched_rows}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Ss7VhtPklvfFHAvQC6pL7yFl': ['civic_docs'], 'var_call_QZ53J9sniSJpXSfsqqo4CkT9': ['Funding'], 'var_call_Kh4pJSIR5TK5dytVJwi04v4T': 'file_storage/call_Kh4pJSIR5TK5dytVJwi04v4T.json', 'var_call_mYCVhIDE3PQLGrX2Q8yp2mkS': 'file_storage/call_mYCVhIDE3PQLGrX2Q8yp2mkS.json'}

exec(code, env_args)

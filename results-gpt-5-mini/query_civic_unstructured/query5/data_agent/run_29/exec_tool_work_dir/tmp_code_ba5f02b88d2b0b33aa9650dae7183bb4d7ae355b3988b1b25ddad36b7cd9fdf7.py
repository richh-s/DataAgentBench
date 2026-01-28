code = """import json
import pandas as pd

# Load query results from storage file paths
path_funding = var_call_RF5KUQDKAHcatKco1yXwKyuW
path_civic = var_call_kzPaCpRaTreguFOvBPuotfG7

with open(path_funding, 'r') as f:
    funding_records = json.load(f)

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Prepare civic docs texts
docs_texts = [d.get('text', '') for d in civic_docs]

# Helper to find contexts
def find_contexts(name):
    name_l = name.lower()
    contexts = []
    for text in docs_texts:
        t_l = text.lower()
        idx = t_l.find(name_l)
        if idx != -1:
            start = max(0, idx-300)
            end = min(len(t_l), idx+len(name_l)+300)
            contexts.append(t_l[start:end])
    return contexts

# Disaster keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency', 'federal assistance']

matched = []
for _, row in fund_df.iterrows():
    pname = row['Project_Name']
    pname_clean = pname
    if '(' in pname:
        pname_clean = pname.split('(')[0].strip()
    contexts = find_contexts(pname_clean)
    if not contexts:
        contexts = find_contexts(pname)
    if not contexts:
        tokens = pname_clean.split()
        if len(tokens) > 4:
            short = ' '.join(tokens[:4])
            contexts = find_contexts(short)
    if not contexts:
        continue
    ctx = '\n'.join(contexts)
    is_disaster = any(k in pname.lower() for k in disaster_keywords) or any(k in ctx for k in disaster_keywords)
    started_2022 = '2022' in ctx
    if is_disaster and started_2022:
        matched.append({'Funding_ID': int(row['Funding_ID']), 'Project_Name': row['Project_Name'], 'Amount': int(row['Amount'])})

total = sum(m['Amount'] for m in matched)

result = {'total_funding_2022_disaster_projects': total, 'matched_records': matched}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Mmh90s31ZiG1mcuIAkQlcjXF': ['civic_docs'], 'var_call_3GU6IwnaLiLmQBgB80238sHz': ['Funding'], 'var_call_kzPaCpRaTreguFOvBPuotfG7': 'file_storage/call_kzPaCpRaTreguFOvBPuotfG7.json', 'var_call_RF5KUQDKAHcatKco1yXwKyuW': 'file_storage/call_RF5KUQDKAHcatKco1yXwKyuW.json'}

exec(code, env_args)

code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
with open(var_call_gowyjKcRaFpHAaawcpGL6RuM, 'r') as f:
    civic_docs = json.load(f)

funding_records = var_call_7YdK1VDRxucUmql3YBWLNT73

# Heuristic: extract project blocks and classify topics & completion dates
park_keywords = ['park', 'playground']

projects = []
for doc in civic_docs:
    text = doc.get('text','')
    # split on double newlines with title-like lines
    chunks = re.split(r"\n\n+", text)
    for ch in chunks:
        # project name: first line if it looks like a title (few words, capitalized words)
        lines = [l.strip() for l in ch.split('\n') if l.strip()]
        if not lines:
            continue
        name = lines[0]
        if len(name.split()) < 2:
            continue
        block = ch.lower()
        topic_terms = []
        if any(k in block for k in park_keywords):
            topic_terms.append('park')
        # status
        status = None
        if 'construction was completed' in block or 'construction was completed,' in block or 'construction was completed ' in block:
            status = 'completed'
        elif 'construction was completed' in block:
            status = 'completed'
        elif 'construction is complete' in block:
            status = 'completed'
        elif 'construction was completed' in block:
            status = 'completed'
        elif 'project is currently under construction' in block or 'begin construction' in block:
            status = status or 'design'
        # end date heuristics: look for 'completed' sentences with year
        et = None
        m = re.search(r'completed[^0-9]*(20[0-9]{2})', block)
        if m:
            et = m.group(1)
        projects.append({'Project_Name': name.strip(), 'topic': ','.join(sorted(set(topic_terms))), 'status': status, 'et': et})

# Filter to park-related, completed in 2022
proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])
mask = (proj_df['topic'].str.contains('park', na=False)) & (proj_df['status']=='completed') & (proj_df['et'].str.contains('2022', na=False))
park_completed_2022 = proj_df[mask]

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)

merged = fund_df.merge(park_completed_2022[['Project_Name']], on='Project_Name', how='inner')

total_funding = int(merged['Amount'].sum())

result = {'total_funding_park_completed_2022': total_funding, 'projects': merged[['Project_Name','Amount']].to_dict(orient='records')}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gowyjKcRaFpHAaawcpGL6RuM': 'file_storage/call_gowyjKcRaFpHAaawcpGL6RuM.json', 'var_call_7YdK1VDRxucUmql3YBWLNT73': 'file_storage/call_7YdK1VDRxucUmql3YBWLNT73.json'}

exec(code, env_args)

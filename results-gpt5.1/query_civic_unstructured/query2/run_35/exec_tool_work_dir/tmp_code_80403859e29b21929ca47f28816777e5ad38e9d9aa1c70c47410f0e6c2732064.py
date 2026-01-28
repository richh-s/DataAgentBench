code = """import re, json, pandas as pd

path_docs = var_call_2sCnV5Xilf9drWfeUXJ12Z4C
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc.get('text','')
    for line in text.split('\n'):
        line_clean = line.strip('\u202f ').strip()
        if not line_clean:
            continue
        if any(k in line_clean for k in ['Park', 'Playground']):
            status = None
            et = None
            m = re.search(r"(?:Construction was completed|construction was completed|Construction completed|was completed)[^\n]*?(\d{4})", text, re.IGNORECASE)
            if m:
                status = 'completed'
                et = m.group(1)
            topic = 'park'
            projects.append({'Project_Name': line_clean, 'topic': topic, 'status': status, 'et': et})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

funding = var_call_7UKR5eT5rM7eOKgTQjfC3pBL
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

merged = pd.merge(fund_df, proj_df, on='Project_Name', how='inner')

mask = (merged['topic']=='park') & (merged['status']=='completed') & (merged['et'].astype(str).str.contains('2022'))
filtered = merged[mask]

total_funding = int(filtered['Amount'].sum()) if not filtered.empty else 0

result = {'total_funding_park_projects_completed_2022': total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2sCnV5Xilf9drWfeUXJ12Z4C': 'file_storage/call_2sCnV5Xilf9drWfeUXJ12Z4C.json', 'var_call_7UKR5eT5rM7eOKgTQjfC3pBL': 'file_storage/call_7UKR5eT5rM7eOKgTQjfC3pBL.json'}

exec(code, env_args)

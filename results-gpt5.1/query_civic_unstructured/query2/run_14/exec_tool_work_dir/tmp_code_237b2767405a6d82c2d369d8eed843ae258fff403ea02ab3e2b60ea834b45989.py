code = """import json, re, pandas as pd

path_docs = var_call_d13AjFzIoR37eT7lbNWqXGul
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_tOTBnlHHR6bc19BQN6YYxXnJ)
funding['Amount'] = funding['Amount'].astype(int)

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if ('Park' in line or 'Playground' in line) and not line.startswith('Page '):
            name = line
            window_lines = lines[i:i+6]
            window = '\n'.join(window_lines)
            status = None
            et = None
            m = re.search(r'Construction was completed[, ]+([A-Za-z]+ 20\d{2})', window)
            if not m:
                m = re.search(r'Construction was completed[, ]*(20\d{2})', window)
            if not m:
                m = re.search(r'completed[, ]+([A-Za-z]+ 20\d{2})', window)
            if m:
                status = 'completed'
                et = m.group(1)
            topics = []
            if 'Park' in name:
                topics.append('park')
            if 'Playground' in name:
                topics.append('playground')
            if topics:
                projects.append({'Project_Name': name, 'topic': ','.join(topics), 'status': status, 'et': et})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name', 'et']).reset_index(drop=True)

if proj_df.empty:
    result = {'identified_projects': [], 'total_funding_park_completed_2022': 0}
else:
    mask_park = proj_df['topic'].str.contains('park')
    mask_completed = proj_df['status'] == 'completed'
    mask_2022 = proj_df['et'].astype(str).str.contains('2022', na=False)
    completed_2022_parks = proj_df[mask_park & mask_completed & mask_2022]

    merged = completed_2022_parks.merge(funding, on='Project_Name', how='left')

    if merged['Amount'].isna().any():
        for idx, row in merged[merged['Amount'].isna()].iterrows():
            name = row['Project_Name']
            cand = funding[funding['Project_Name'].str.contains(re.escape(name), case=False, na=False)]
            if not cand.empty:
                merged.loc[idx, 'Amount'] = cand['Amount'].iloc[0]

    merged_nonnull = merged.dropna(subset=['Amount'])
    total_funding = int(merged_nonnull['Amount'].sum()) if not merged_nonnull.empty else 0
    result = {
        'identified_projects': merged_nonnull[['Project_Name', 'topic', 'status', 'et', 'Amount']].to_dict(orient='records'),
        'total_funding_park_completed_2022': total_funding
    }

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_d13AjFzIoR37eT7lbNWqXGul': 'file_storage/call_d13AjFzIoR37eT7lbNWqXGul.json', 'var_call_tOTBnlHHR6bc19BQN6YYxXnJ': 'file_storage/call_tOTBnlHHR6bc19BQN6YYxXnJ.json'}

exec(code, env_args)

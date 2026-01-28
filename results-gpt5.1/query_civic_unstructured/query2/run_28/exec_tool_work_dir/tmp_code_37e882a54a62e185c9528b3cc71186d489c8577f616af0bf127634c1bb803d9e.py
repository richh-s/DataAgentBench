code = """import re, json, pandas as pd

# Load civic docs full result
path_docs = var_call_GPQnJn9mNEuzbJnsIM8mS8LK
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

funding_records = var_call_2UY5fDVZuoqQkHNoWQDtB3BI

texts = [d.get('text','') for d in civic_docs]
full_text = '\n'.join(texts)

lines = [l.strip() for l in full_text.split('\n') if l.strip()]

projects = []
current_project = None

for line in lines:
    if re.match(r'^[A-Z0-9].*Project', line) or re.match(r'^[A-Z0-9].*Park', line):
        if len(line.split()) <= 2:
            continue
        if current_project:
            projects.append(current_project)
        current_project = {'Project_Name': line, 'status': None, 'st': None, 'et': None, 'topic': None}
    elif current_project:
        low = line.lower()
        if 'updates:' in low or 'project description' in low:
            continue
        if 'construction was completed' in low or 'construction: completed' in low or 'was completed' in low or 'construction was completed' in low:
            m = re.search(r'(\w+\s+\d{4}|\d{4})', line)
            if m:
                current_project['status'] = 'completed'
                current_project['et'] = m.group(0)
        if 'complete construction:' in low or 'complete construction' in low:
            m = re.search(r'(spring|summer|fall|winter)?\s*\d{4}', low)
            if m:
                current_project['et'] = m.group(0)
        if 'park' in low:
            current_project['topic'] = (current_project.get('topic') or '') + ',park'

if current_project:
    projects.append(current_project)

proj_df = pd.DataFrame(projects)

park_completed_2022 = proj_df[
    proj_df['topic'].fillna('').str.contains('park') &
    (proj_df['status'] == 'completed') &
    proj_df['et'].fillna('').str.contains('2022')
]

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)


def normalize(name):
    return re.sub(r'[^a-z0-9]+',' ', name.lower()).strip()

park_completed_2022['norm_name'] = park_completed_2022['Project_Name'].apply(normalize)
fund_df['norm_name'] = fund_df['Project_Name'].apply(normalize)

merged = pd.merge(park_completed_2022, fund_df, on='norm_name', how='inner')

total_funding = int(merged['Amount'].sum()) if not merged.empty else 0

result = {'total_funding_park_completed_2022': total_funding,
          'matched_projects': merged[['Project_Name_y','Amount']].to_dict(orient='records') if not merged.empty else []}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_GPQnJn9mNEuzbJnsIM8mS8LK': 'file_storage/call_GPQnJn9mNEuzbJnsIM8mS8LK.json', 'var_call_2UY5fDVZuoqQkHNoWQDtB3BI': 'file_storage/call_2UY5fDVZuoqQkHNoWQDtB3BI.json'}

exec(code, env_args)

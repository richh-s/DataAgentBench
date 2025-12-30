code = """import re, json, pandas as pd
import pathlib, json as jsonlib

# Load full civic docs
path = pathlib.Path(var_call_aov1Zh3Mr02KU3T4a9S3830g)
with open(path, 'r') as f:
    civic_docs = jsonlib.load(f)

projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if re.search(r'park', line, re.I):
            name = line
            status = None
            et = None
            for j in range(i+1, min(i+6, len(lines))):
                l2 = lines[j]
                if 'Construction was completed' in l2 or 'construction was completed' in l2:
                    status = 'completed'
                m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}', l2)
                if m:
                    et = m.group(0)
            topic = 'park'
            projects.append({'Project_Name': name, 'topic': topic, 'status': status, 'et': et})

# Load funding table
path2 = pathlib.Path(var_call_yslhMF58NiMpbgNYQKz6ueg5)
with open(path2,'r') as f:
    funding = jsonlib.load(f)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])
mask_2022 = proj_df['et'].fillna('').str.contains('2022')
mask_completed = proj_df['status'].eq('completed')
mask_park = proj_df['topic'].str.contains('park', case=False)
proj_2022 = proj_df[mask_2022 & mask_completed & mask_park]

merged = proj_2022.merge(fund_df, on='Project_Name', how='left')

if merged.empty:
    total_funding = 0
else:
    total_funding = int(merged['Amount'].sum())

result = json.dumps({"total_funding_park_projects_completed_2022": total_funding})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_aov1Zh3Mr02KU3T4a9S3830g': 'file_storage/call_aov1Zh3Mr02KU3T4a9S3830g.json', 'var_call_yslhMF58NiMpbgNYQKz6ueg5': 'file_storage/call_yslhMF58NiMpbgNYQKz6ueg5.json'}

exec(code, env_args)

code = """import re, json, pandas as pd
from pathlib import Path

path_docs = Path(var_call_wdKx1T0jpUpmPr4beCkwECeE)
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_aKuJLGLVcmzc8hcXrQpq3kCQ)

text = " \n".join(doc['text'] for doc in civic_docs)

blocks = re.split(r"\n\s*\n", text)
projects = []
for blk in blocks:
    first_line = blk.strip().split("\n")[0].strip()
    if not first_line:
        continue
    if (('Park' in first_line or 'park' in first_line) and 'Project' in blk) or 'Park Playground' in first_line:
        proj = {'Project_Name': first_line}
        m = re.search(r"Construction was completed,? ([A-Za-z]+ \d{4})", blk)
        if m:
            proj['status'] = 'completed'
            proj['et'] = m.group(1)
        topics = []
        if 'Park' in first_line or 'park' in first_line:
            topics.append('park')
        proj['topic'] = ','.join(topics)
        projects.append(proj)

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])
mask_park = proj_df['topic'].str.contains('park', case=False, na=False)
mask_completed = proj_df['status'].eq('completed')
mask_2022 = proj_df['et'].fillna('').str.contains('2022')
proj_2022 = proj_df[mask_park & mask_completed & mask_2022]

merged = funding.merge(proj_2022[['Project_Name']], on='Project_Name', how='inner')
merged['Amount'] = merged['Amount'].astype(int)

total_funding = int(merged['Amount'].sum()) if not merged.empty else 0

result = json.dumps(total_funding)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_wdKx1T0jpUpmPr4beCkwECeE': 'file_storage/call_wdKx1T0jpUpmPr4beCkwECeE.json', 'var_call_aKuJLGLVcmzc8hcXrQpq3kCQ': 'file_storage/call_aKuJLGLVcmzc8hcXrQpq3kCQ.json'}

exec(code, env_args)

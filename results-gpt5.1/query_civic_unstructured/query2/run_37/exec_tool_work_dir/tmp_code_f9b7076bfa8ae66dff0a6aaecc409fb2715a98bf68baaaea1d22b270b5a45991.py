code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
path_docs = Path(var_call_wdKx1T0jpUpmPr4beCkwECeE)
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

# Funding records
funding = pd.DataFrame(var_call_aKuJLGLVcmzc8hcXrQpq3kCQ)

text = " \n".join(doc['text'] for doc in civic_docs)

# crude project parsing: split on double newlines, treat lines that look like project titles
blocks = re.split(r"\n\s*\n", text)
projects = []
current = None
for blk in blocks:
    line = blk.strip().split("\n")[0].strip()
    if not line:
        continue
    if re.match(r"[A-Z0-9].+", line) and 'Project' in line or 'Park' in line:
        current = {'Project_Name': line}
        # find status
        m_status = re.search(r"Construction was completed,? (\w+ \d{4})", blk)
        if m_status:
            current['status'] = 'completed'
            current['et'] = m_status.group(1)
        m_status2 = re.search(r"Construction was completed (\w+ \d{4})", blk)
        if m_status2:
            current['status'] = 'completed'
            current['et'] = m_status2.group(1)
        # topic heuristic
        topics = []
        if 'Park' in line:
            topics.append('park')
        current['topic'] = ','.join(topics)
        projects.append(current)

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

# Filter for park-related, completed in 2022
mask_park = proj_df['topic'].str.contains('park', case=False, na=False)
mask_completed = proj_df['status'].eq('completed')
mask_2022 = proj_df['et'].fillna('').str.contains('2022')
proj_2022 = proj_df[mask_park & mask_completed & mask_2022]

# Join with funding on Project_Name
merged = funding.merge(proj_2022[['Project_Name']], on='Project_Name', how='inner')
merged['Amount'] = merged['Amount'].astype(int)

total_funding = int(merged['Amount'].sum()) if not merged.empty else 0

result = json.dumps({"total_funding_2022_park_completed": total_funding})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_wdKx1T0jpUpmPr4beCkwECeE': 'file_storage/call_wdKx1T0jpUpmPr4beCkwECeE.json', 'var_call_aKuJLGLVcmzc8hcXrQpq3kCQ': 'file_storage/call_aKuJLGLVcmzc8hcXrQpq3kCQ.json'}

exec(code, env_args)

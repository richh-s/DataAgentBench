code = """import json, re, pandas as pd
from pathlib import Path

# Load full civic docs
with open(var_call_OLxlsF7TvTAF3pbFRp718q5r, 'r') as f:
    civic_docs = json.load(f)
funding = pd.DataFrame(var_call_FVDVoj5cVp70POh1ERKFUzcE)
funding['Amount'] = funding['Amount'].astype(int)

text = '\n'.join(doc['text'] for doc in civic_docs)

# Heuristic: find project lines that look like project titles, then nearby status/completion info
lines = text.splitlines()
projects = []
current_project = None
buffer = []
for line in lines:
    stripped = line.strip()
    if not stripped:
        continue
    # New project when line is title-like (no colon, not too long) and contains Park/park
    if (('Park' in stripped or 'park' in stripped) and ':' not in stripped and len(stripped) < 80):
        # save previous
        if current_project is not None:
            projects.append({'Project_Name': current_project, 'context': '\n'.join(buffer)})
        current_project = stripped
        buffer = []
    else:
        if current_project is not None:
            buffer.append(stripped)

if current_project is not None:
    projects.append({'Project_Name': current_project, 'context': '\n'.join(buffer)})

proj_df = pd.DataFrame(projects)

# Identify completed in 2022: context contains 'Construction was completed' or 'construction was completed' and '2022'
mask_completed_2022 = proj_df['context'].str.contains('completed', case=False, na=False) & proj_df['context'].str.contains('2022', na=False)
completed_2022 = proj_df[mask_completed_2022]

# Join with funding by project name (exact match first, then fuzzy via substring matching to funding project names)
funding_projects = funding['Project_Name'].tolist()

matched_names = set()
amount_total = 0
for _, row in completed_2022.iterrows():
    name = row['Project_Name']
    # exact
    fmatch = funding[funding['Project_Name'] == name]
    if fmatch.empty:
        # try contains either way
        fmatch = funding[funding['Project_Name'].str.contains(re.escape(name), case=False, na=False) | funding['Project_Name'].apply(lambda x: name.lower() in x.lower())]
    if not fmatch.empty:
        # assume all rows for that project count
        amount_total += fmatch['Amount'].sum()
        matched_names.update(fmatch['Project_Name'].unique())

result = {
    'completed_2022_park_projects': completed_2022.to_dict(orient='records'),
    'matched_funding_projects': list(matched_names),
    'total_funding': int(amount_total)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OLxlsF7TvTAF3pbFRp718q5r': 'file_storage/call_OLxlsF7TvTAF3pbFRp718q5r.json', 'var_call_FVDVoj5cVp70POh1ERKFUzcE': 'file_storage/call_FVDVoj5cVp70POh1ERKFUzcE.json'}

exec(code, env_args)

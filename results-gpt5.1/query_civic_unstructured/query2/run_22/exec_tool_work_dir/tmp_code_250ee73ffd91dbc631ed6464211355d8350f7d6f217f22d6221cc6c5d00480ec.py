code = """import json, re, pandas as pd

with open(var_call_OLxlsF7TvTAF3pbFRp718q5r, 'r') as f:
    civic_docs = json.load(f)
funding = pd.DataFrame(var_call_FVDVoj5cVp70POh1ERKFUzcE)
funding['Amount'] = funding['Amount'].astype(int)

text = '\n'.join(doc['text'] for doc in civic_docs)
lines = text.split('\n')

projects = []
current_project = None
buffer = []
for line in lines:
    stripped = line.strip()
    if not stripped:
        continue
    if (('Park' in stripped or 'park' in stripped) and ':' not in stripped and len(stripped) < 80):
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
mask_completed_2022 = proj_df['context'].str.contains('completed', case=False, na=False) & proj_df['context'].str.contains('2022', na=False)
completed_2022 = proj_df[mask_completed_2022]

matched_names = set()
amount_total = 0
for _, row in completed_2022.iterrows():
    name = row['Project_Name']
    fmatch = funding[funding['Project_Name'] == name]
    if fmatch.empty:
        fmatch = funding[funding['Project_Name'].str.contains(re.escape(name), case=False, na=False) | funding['Project_Name'].apply(lambda x: name.lower() in x.lower())]
    if not fmatch.empty:
        amount_total += int(fmatch['Amount'].sum())
        matched_names.update(list(fmatch['Project_Name'].unique()))

result = {
    'total_funding': int(amount_total)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OLxlsF7TvTAF3pbFRp718q5r': 'file_storage/call_OLxlsF7TvTAF3pbFRp718q5r.json', 'var_call_FVDVoj5cVp70POh1ERKFUzcE': 'file_storage/call_FVDVoj5cVp70POh1ERKFUzcE.json'}

exec(code, env_args)

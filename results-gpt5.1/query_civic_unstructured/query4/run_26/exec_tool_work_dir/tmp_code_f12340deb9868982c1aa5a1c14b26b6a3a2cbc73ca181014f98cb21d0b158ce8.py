code = """import re, json, pandas as pd
path_civic = var_call_ldmJUIvsZJAzw1wXe35zrsaX
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)
texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)
lines = [l.strip() for l in full_text.split('\n') if l.strip()]
projects = {}
for i,l in enumerate(lines):
    name = None
    if re.search(r'Project', l) or re.search(r'Repairs|Improvements|Study|Facility|Park', l):
        name = l
    if not name:
        continue
    context = '\n'.join(lines[max(0,i-5):i+10])
    if re.search(r'Begin (Construction|Design):?\s*(Spring 2022|March 2022|April 2022|May 2022|2022-Spring|2022-March|2022-04|2022-05)', context, re.IGNORECASE):
        projects[name] = context
path_fund = var_call_9H3atxEvNCgxQLPlrfBmlSeE
with open(path_fund, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)
matched_projects = {}
for pname in projects:
    mask = fund_df['Project_Name'].apply(lambda x: x in pname or pname in x)
    rows = fund_df[mask]
    if not rows.empty:
        matched_projects[pname] = rows
if matched_projects:
    all_rows = pd.concat(matched_projects.values(), ignore_index=True).drop_duplicates(subset=['Funding_ID'])
    num_projects = all_rows['Project_Name'].nunique()
    total_funding = int(all_rows['Amount'].sum())
else:
    num_projects = 0
    total_funding = 0
result = {"num_projects_spring_2022": num_projects, "total_funding_spring_2022": total_funding}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ldmJUIvsZJAzw1wXe35zrsaX': 'file_storage/call_ldmJUIvsZJAzw1wXe35zrsaX.json', 'var_call_9H3atxEvNCgxQLPlrfBmlSeE': 'file_storage/call_9H3atxEvNCgxQLPlrfBmlSeE.json', 'var_call_Y7GrS5dj0LOP1MoyCmtJslOF': ['civic_docs'], 'var_call_j6hHI4yDdi7GsyyxFqRfkQVt': ['Funding']}

exec(code, env_args)

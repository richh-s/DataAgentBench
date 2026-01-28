code = """import re, json, pandas as pd

with open(var_call_FRjYq885wjf7bPRjPPh0gKKu, 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line_strip = line.strip()
        if not line_strip:
            continue
        if re.search(r'park|Playground', line_strip, re.IGNORECASE):
            projects.append({'Project_Name': line_strip})

proj_df = pd.DataFrame(projects).drop_duplicates().reset_index(drop=True)

proj_info = {}
for doc in civic_docs:
    lines = doc.get('text', '').split('\n')
    for i, line in enumerate(lines):
        for pname in proj_df['Project_Name']:
            if pname and pname in line:
                context = '\n'.join(lines[i:i+5])
                status = None
                et = None
                if re.search(r'Construction was completed,?\s*November 2022', context):
                    status = 'completed'
                    et = '2022-11'
                if re.search(r'Construction was completed,?\s*January 2022', context):
                    status = 'completed'
                    et = '2022-01'
                if re.search(r'Construction was completed,?\s*December 2022', context):
                    status = 'completed'
                    et = '2022-12'
                if status:
                    proj_info[pname] = {'status': status, 'et': et}

proj_info_list = []
for pname, info in proj_info.items():
    proj_info_list.append({'Project_Name': pname, 'status': info['status'], 'et': info['et']})

proj_info_df = pd.DataFrame(proj_info_list)

with open(var_call_tWF7f96V2hcpeDu2iyw7CAKD, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

merged = pd.merge(proj_info_df, fund_df, on='Project_Name', how='inner')

mask_2022 = merged['et'].astype(str).str.contains('2022', na=False)
mask_park = merged['Project_Name'].str.contains('park|Playground', case=False, na=False)
filtered = merged[mask_2022 & mask_park]

total_funding = int(filtered['Amount'].sum()) if not filtered.empty else 0

result = json.dumps(total_funding)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_FRjYq885wjf7bPRjPPh0gKKu': 'file_storage/call_FRjYq885wjf7bPRjPPh0gKKu.json', 'var_call_tWF7f96V2hcpeDu2iyw7CAKD': 'file_storage/call_tWF7f96V2hcpeDu2iyw7CAKD.json'}

exec(code, env_args)

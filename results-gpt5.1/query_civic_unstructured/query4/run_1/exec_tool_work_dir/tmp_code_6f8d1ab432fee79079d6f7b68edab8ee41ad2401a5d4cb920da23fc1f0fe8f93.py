code = """import re, json, pandas as pd

path_docs = var_call_tcwwlyeJzBSz4Nu4hWVWoxlz
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]

keywords = ['Project', 'Improvements', 'Repairs', 'Park', 'Road', 'Street', 'Drain', 'Canyon', 'Bridge', 'Playground', 'Water', 'Signals', 'Biofilter', 'Shade', 'Walkway', 'Median', 'Crosswalk', 'HVAC', 'Roof', 'Solar', 'Traffic Study', 'Warning']

project_records = []
for text in texts:
    lines = [l.strip() for l in text.split('\n')]
    for i, line in enumerate(lines):
        if not line or ':' in line:
            continue
        if any(k in line for k in keywords):
            window = '\n'.join(lines[i:i+15])
            m = re.search(r'(Begin Construction|Start|Project Schedule)[^\n]*?(Spring\s+2022|2022[- ]Spring)', window, re.IGNORECASE)
            if m:
                st = '2022-Spring'
                project_records.append({'Project_Name': line, 'st': st})

import pandas as pd
proj_df = pd.DataFrame(project_records).drop_duplicates(subset=['Project_Name'])

path_fund = var_call_Ok4O10RYmCgD1UHY1FmZiFHG
with open(path_fund, 'r') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Amount'] = fund_df['Amount'].astype(int)

merged = proj_df.merge(fund_df, on='Project_Name', how='inner')

result = {
    'projects_started_spring_2022_count': int(len(merged)),
    'total_funding_spring_2022': int(merged['Amount'].sum()),
    'project_names': merged['Project_Name'].tolist()
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_tcwwlyeJzBSz4Nu4hWVWoxlz': 'file_storage/call_tcwwlyeJzBSz4Nu4hWVWoxlz.json', 'var_call_Ok4O10RYmCgD1UHY1FmZiFHG': 'file_storage/call_Ok4O10RYmCgD1UHY1FmZiFHG.json'}

exec(code, env_args)

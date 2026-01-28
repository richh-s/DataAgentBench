code = """import json, pandas as pd

funding_records = var_call_RXv889JDY6ZF2TdZ0JrS8Dai
funding_df = pd.DataFrame(funding_records)

path = var_call_6JTWoCyV1lYT6526R0ru96NS
with open(path, 'r') as f:
    civic_records = json.load(f)

texts = [r.get('text','') for r in civic_records]

projects = []
for text in texts:
    blocks = text.split('\n\n')
    for block in blocks:
        lower = block.lower()
        if 'capital improvement projects (design)' in lower:
            status = 'design'
            ptype = 'capital'
        elif 'capital improvement projects (not started)' in lower:
            status = 'not started'
            ptype = 'capital'
        else:
            continue
        for pname in funding_df['Project_Name'].unique():
            if isinstance(pname, str) and pname.lower() in lower:
                projects.append({'Project_Name': pname, 'status': status, 'type': ptype})

proj_df = pd.DataFrame(projects).drop_duplicates()
merged = pd.merge(funding_df, proj_df, on='Project_Name', how='inner')
count = int(((merged['type'] == 'capital') & (merged['status'] == 'design')).sum())

out = json.dumps(count)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RXv889JDY6ZF2TdZ0JrS8Dai': 'file_storage/call_RXv889JDY6ZF2TdZ0JrS8Dai.json', 'var_call_6JTWoCyV1lYT6526R0ru96NS': 'file_storage/call_6JTWoCyV1lYT6526R0ru96NS.json'}

exec(code, env_args)

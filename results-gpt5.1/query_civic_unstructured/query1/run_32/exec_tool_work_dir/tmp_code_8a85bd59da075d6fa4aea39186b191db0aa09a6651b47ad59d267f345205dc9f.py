code = """import json, pandas as pd

# Load funding projects over 50k
funding_records = var_call_RXv889JDY6ZF2TdZ0JrS8Dai
funding_df = pd.DataFrame(funding_records)

# Load civic docs full result from file path
import os, pathlib
path = var_call_6JTWoCyV1lYT6526R0ru96NS
with open(path, 'r') as f:
    civic_records = json.load(f)

texts = [r.get('text','') for r in civic_records]

projects = []
for text in texts:
    # simple heuristic: split on double newlines and keep lines near keywords
    blocks = text.split('\n\n')
    for block in blocks:
        lower = block.lower()
        if 'capital improvement projects' in lower or 'projects (design)' in lower or 'capital improvement projects (design)' in lower or 'capital improvement projects (not started)' in lower or 'disaster recovery projects' in lower:
            # within this block, look for known project names from funding
            for pname in funding_df['Project_Name'].unique():
                if isinstance(pname,str) and pname.lower() in lower:
                    status = None
                    ptype = None
                    if 'capital improvement projects (design)' in lower:
                        status = 'design'
                        ptype = 'capital'
                    elif 'capital improvement projects (not started)' in lower:
                        status = 'not started'
                        ptype = 'capital'
                    projects.append({'Project_Name': pname, 'status': status, 'type': ptype})

proj_df = pd.DataFrame(projects).drop_duplicates()

# join with funding over 50k
merged = pd.merge(funding_df, proj_df, on='Project_Name', how='inner')
result_count = int(((merged['type']=='capital') & (merged['status']=='design')).sum())

out = json.dumps({'count_capital_design_over_50k': result_count})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RXv889JDY6ZF2TdZ0JrS8Dai': 'file_storage/call_RXv889JDY6ZF2TdZ0JrS8Dai.json', 'var_call_6JTWoCyV1lYT6526R0ru96NS': 'file_storage/call_6JTWoCyV1lYT6526R0ru96NS.json'}

exec(code, env_args)

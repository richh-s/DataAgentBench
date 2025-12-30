code = """import json, re, pandas as pd

path = var_call_i1t62alcZi7FqO92q62frU2z
with open(path, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_h3SMRD85wbsb0T0Bp1p6UtKY)

projects = {}
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        if ('(FEMA' in line_stripped) or ('(CalOES' in line_stripped) or ('(CalJPIA' in line_stripped) or ('Disaster' in line_stripped) or ('disaster' in line_stripped):
            name = line_stripped
            st = None
            m = re.search(r"20[0-9]{2}", line_stripped)
            if m:
                st = m.group(0)
            projects[name] = {'Project_Name': name, 'type': 'disaster', 'st': st}

proj_df = pd.DataFrame(list(projects.values()))

proj_2022 = proj_df[proj_df['st'].astype(str).str.contains('2022', na=False)]

merged = pd.merge(funding, proj_2022, on='Project_Name', how='inner')

if not merged.empty:
    merged['Amount'] = merged['Amount'].astype(int)
    total = int(merged['Amount'].sum())
else:
    total = 0

result = json.dumps({'total_funding_disaster_2022': total})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_i1t62alcZi7FqO92q62frU2z': 'file_storage/call_i1t62alcZi7FqO92q62frU2z.json', 'var_call_h3SMRD85wbsb0T0Bp1p6UtKY': 'file_storage/call_h3SMRD85wbsb0T0Bp1p6UtKY.json'}

exec(code, env_args)

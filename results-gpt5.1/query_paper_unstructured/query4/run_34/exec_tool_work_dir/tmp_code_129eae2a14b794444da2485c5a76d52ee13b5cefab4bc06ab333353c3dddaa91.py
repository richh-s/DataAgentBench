code = """import re, json
import pandas as pd

# load full citations
path_cit = var_call_24sgiO77VEzCiF7BdOTkkqCy
with open(path_cit, 'r') as f:
    cit = json.load(f)

# filter paper docs for domain physical activity and year 2016 via regex heuristics
path_docs = var_call_pwSTL4PH6C8r5RQDjiuaZRem
with open(path_docs, 'r') as f:
    docs = json.load(f)

records = []
for d in docs:
    text = d.get('text','')
    # year heuristic: look for 2016 in header; skip if obviously other year like 2015 venue line
    if '2016' not in text:
        continue
    if re.search(r'physical activity', text, re.I):
        title = d.get('filename','').replace('.txt','').strip()
        records.append({'title': title})

# unique titles
titles_pa_2016 = sorted({r['title'] for r in records})

# build dataframe for citations
cit_df = pd.DataFrame(cit)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

result = []
for t in titles_pa_2016:
    # exact match on title
    row = cit_df[cit_df['title'] == t]
    if not row.empty:
        total = int(row['total_citations'].iloc[0])
    else:
        total = 0
    result.append({'title': t, 'total_citations': total})

result_json = json.dumps(result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_pwSTL4PH6C8r5RQDjiuaZRem': 'file_storage/call_pwSTL4PH6C8r5RQDjiuaZRem.json', 'var_call_24sgiO77VEzCiF7BdOTkkqCy': 'file_storage/call_24sgiO77VEzCiF7BdOTkkqCy.json'}

exec(code, env_args)

code = """import json, pandas as pd

# Read data
f_path = locals()['var_functions.query_db:4']
c_path = locals()['var_functions.query_db:5']

f_fh = open(f_path, 'r')
 funding_raw = json.load(f_fh)
f_fh.close()

c_fh = open(c_path, 'r')
 civic_docs = json.load(c_fh)
c_fh.close()

# Set up funding dataframe
df_f = pd.DataFrame(funding_raw)
df_f['Amount'] = pd.to_numeric(df_f['Amount'])

# Find projects in civic docs
park_2022 = []
for d in civic_docs:
    txt = d.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        cur = lines[i].strip()
        if '2022' in cur and ('completed' in cur.lower() or 'completion' in cur.lower()):
            # Look backwards
            for j in range(i-1, -1, -1):
                prev = lines[j].strip()
                if prev and len(prev) > 10 and not prev.startswith('('):
                    low = prev.lower()
                    skip_words = ['project schedule', 'project des', 'updates:', 'to:', 'from:', 'subject:', 'prepared', 'approved']
                    if not any(w in low for w in skip_words):
                        if 'park' in low or 'playground' in low or 'bluff' in low:
                            park_2022.append(prev)
                            break
                    
# Deduplicate
park_2022 = list(set(park_2022))

# Match funding
total = 0
for p in park_2022:
    p_low = p.lower()
    for _, r in df_f.iterrows():
        name_low = r['Project_Name'].lower()
        if p_low in name_low or name_low in p_low:
            total += r['Amount']

result = {'total_funding': int(total)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_documents': 5, 'park_projects_found': 21, 'total_park_funding': 1123000, 'completed_2022_projects_raw': 2}}

exec(code, env_args)

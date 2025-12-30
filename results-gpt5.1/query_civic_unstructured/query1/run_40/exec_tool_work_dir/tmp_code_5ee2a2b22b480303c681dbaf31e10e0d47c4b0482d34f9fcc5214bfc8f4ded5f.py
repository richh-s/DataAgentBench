code = """import re, json, pandas as pd

with open(var_call_3wntBK6NTfB3jdApZE7rruJ5, 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

texts = [d['text'] for d in var_call_yNy3q6EAzcH0UoYaPw8djOE4]

projects = []
for text in texts:
    lines = text.split('\n')
    in_design = False
    for line in lines:
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
            continue
        if in_design and 'Capital Improvement Projects (Construction)' in line:
            in_design = False
        if in_design:
            s = line.strip()
            if s and not s.startswith('(cid:') and 'Updates' not in s and 'Project Schedule' not in s and 'Estimated Schedule' not in s and not s.startswith('Page '):
                if len(s.split()) < 12:
                    projects.append({'Project_Name': s, 'status': 'design', 'type': 'capital'})

projects_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

merged = pd.merge(funding_df, projects_df, on='Project_Name', how='inner')

result_df = merged[(merged['type']=='capital') & (merged['status']=='design') & (merged['Amount'] > 50000)]
count = int(result_df.shape[0])

out = json.dumps(count)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_3wntBK6NTfB3jdApZE7rruJ5': 'file_storage/call_3wntBK6NTfB3jdApZE7rruJ5.json', 'var_call_yNy3q6EAzcH0UoYaPw8djOE4': 'file_storage/call_yNy3q6EAzcH0UoYaPw8djOE4.json'}

exec(code, env_args)

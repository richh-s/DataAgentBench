code = """import re, json, pandas as pd

# Load full funding results
with open(var_call_3wntBK6NTfB3jdApZE7rruJ5, 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract project names and statuses from civic docs text (simple heuristic)
texts = [d['text'] for d in var_call_yNy3q6EAzcH0UoYaPw8djOE4]

projects = []
for text in texts:
    # Identify sections for capital improvement projects design
    # We'll consider any line under a heading containing 'Capital Improvement Projects (Design)'
    lines = text.split('\n')
    in_design = False
    for line in lines:
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
            continue
        if in_design and line.strip().endswith('Projects (Construction)'):
            in_design = False
        if in_design:
            # project name lines are non-empty and not bullet/update lines
            if line.strip() and not line.strip().startswith('(cid:') and 'Updates' not in line and 'Project Schedule' not in line and 'Estimated Schedule' not in line:
                # Heuristic: single-line title with few words and capital letters
                if len(line.split()) < 12:
                    projects.append({'Project_Name': line.strip(), 'status': 'design', 'type': 'capital'})

projects_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

# Join with funding on Project_Name
merged = pd.merge(funding_df, projects_df, on='Project_Name', how='inner')

# Filter for capital, design, amount > 50000
result_df = merged[(merged['type']=='capital') & (merged['status']=='design') & (merged['Amount'] > 50000)]
count = int(result_df.shape[0])

out = json.dumps({'count_capital_design_over_50000': count})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_3wntBK6NTfB3jdApZE7rruJ5': 'file_storage/call_3wntBK6NTfB3jdApZE7rruJ5.json', 'var_call_yNy3q6EAzcH0UoYaPw8djOE4': 'file_storage/call_yNy3q6EAzcH0UoYaPw8djOE4.json'}

exec(code, env_args)

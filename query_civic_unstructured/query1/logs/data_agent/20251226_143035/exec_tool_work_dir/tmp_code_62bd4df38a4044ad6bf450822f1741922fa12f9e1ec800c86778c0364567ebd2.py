code = """import pandas as pd
import json

# Load funding data
funding_data_path = 'var_call_ftaQezTBmv5Al1wjsLpyDp6o'
with open(funding_data_path) as f:
    funding_records = json.load(f)

# Load civic documents data
civic_docs_data_path = 'var_call_Ll8AHgPQgrmHn41PEdkSmmIw'
with open(civic_docs_data_path) as f:
    civic_docs_records = json.load(f)

# Extract project names from civic docs related to 'design'
projects = []
for doc in civic_docs_records:
    if 'Capital Improvement Projects (Design)' in doc['text']:
        relevant_lines = doc['text'].split('\n')
        for line in relevant_lines:
            if 'Improvements' in line:
                projects.append(line.strip())

# Convert to DataFrame and filter funding records
funding_df = pd.DataFrame(funding_records)

# Filter the funding DataFrame according to project names extracted and amount conditions
filtered_projects = funding_df[funding_df['Project_Name'].isin(projects) & (funding_df['Amount'] > 50000)]

# Count the filtered projects
count_design_projects = filtered_projects.shape[0]

# Print the result
print('__RESULT__:')
print(count_design_projects)"""

env_args = {'var_call_ftaQezTBmv5Al1wjsLpyDp6o': 'file_storage/call_ftaQezTBmv5Al1wjsLpyDp6o.json', 'var_call_Ll8AHgPQgrmHn41PEdkSmmIw': 'file_storage/call_Ll8AHgPQgrmHn41PEdkSmmIw.json'}

exec(code, env_args)

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

# Extract project names from civic docs with 'design' status
projects_in_design = []
for doc in civic_docs_records:
    if 'design' in doc['text'].lower():
        projects_in_design += [line.strip() for line in doc['text'].split('\n') if 'Improvements' in line]

# Clean project names
projects_in_design = [project.split(':')[0].strip() for project in projects_in_design]

# Create DataFrame from funding records
funding_df = pd.DataFrame(funding_records)

# Filter the funding DataFrame for projects in design status with funding > $50,000
filtered_funding = funding_df[(funding_df['Project_Name'].isin(projects_in_design)) & (funding_df['Amount'] > 50000)]

# Count the filtered projects
count_of_projects = filtered_funding.shape[0]

# Print the result
print('__RESULT__:')
print(count_of_projects)"""

env_args = {'var_call_ftaQezTBmv5Al1wjsLpyDp6o': 'file_storage/call_ftaQezTBmv5Al1wjsLpyDp6o.json', 'var_call_Ll8AHgPQgrmHn41PEdkSmmIw': 'file_storage/call_Ll8AHgPQgrmHn41PEdkSmmIw.json'}

exec(code, env_args)

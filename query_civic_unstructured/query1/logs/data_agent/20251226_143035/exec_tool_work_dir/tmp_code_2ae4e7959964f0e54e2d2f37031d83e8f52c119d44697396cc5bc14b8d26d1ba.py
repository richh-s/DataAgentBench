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

# Extract project names from civic documents that contain 'design'
projects_in_design = []
for doc in civic_docs_records:
    lines = doc['text'].split('\n')
    if any('design' in line.lower() for line in lines):
        for line in lines:
            if 'Improvements' in line:
                projects_in_design.append(line.strip())

# Clean project names
projects_in_design = [project.split(':')[0].strip() for project in projects_in_design]

# Create a DataFrame from funding records
funding_df = pd.DataFrame(funding_records)

# Filter for projects with funding greater than $50,000
filtered_projects = funding_df[(funding_df['Project_Name'].isin(projects_in_design)) & (funding_df['Amount'] > 50000)]

# Count the number of such projects
count = filtered_projects.shape[0]

# Print the result
print('__RESULT__:')
print(count)"""

env_args = {'var_call_ftaQezTBmv5Al1wjsLpyDp6o': 'file_storage/call_ftaQezTBmv5Al1wjsLpyDp6o.json', 'var_call_Ll8AHgPQgrmHn41PEdkSmmIw': 'file_storage/call_Ll8AHgPQgrmHn41PEdkSmmIw.json'}

exec(code, env_args)

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

# Extract project names from civic docs involving 'design'
projects_in_design = []
for doc in civic_docs_records:
    if 'design' in doc['text'].lower():
        relevant_lines = doc['text'].split('\n')
        for line in relevant_lines:
            if 'design' in line.lower():
                projects_in_design.append(line.strip())

# Extract only project names
projects_in_design = [project.split(':')[0].strip() for project in projects_in_design]

# Convert funding records into a DataFrame for filtering
funding_df = pd.DataFrame(funding_records)

# Filter the records to count how many projects are in design and have funding > $50,000
filtered_funding = funding_df[(funding_df['Project_Name'].isin(projects_in_design)) & (funding_df['Amount'] > 50000)]

# Count the resulting projects
count_of_projects = filtered_funding.shape[0]

# Output the result
print('__RESULT__:')
print(count_of_projects)"""

env_args = {'var_call_ftaQezTBmv5Al1wjsLpyDp6o': 'file_storage/call_ftaQezTBmv5Al1wjsLpyDp6o.json', 'var_call_Ll8AHgPQgrmHn41PEdkSmmIw': 'file_storage/call_Ll8AHgPQgrmHn41PEdkSmmIw.json'}

exec(code, env_args)

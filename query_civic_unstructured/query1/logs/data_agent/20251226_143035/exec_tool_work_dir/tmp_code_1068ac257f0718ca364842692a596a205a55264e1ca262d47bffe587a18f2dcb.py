code = """import pandas as pd
import json

# Load funding data
funding_data_path = 'var_call_FMg9vplBr9GHN1E55wyBrM0i'
with open(funding_data_path) as f:
    funding_records = json.load(f)

# Load civic documents data
civic_docs_data_path = 'var_call_CaySYkEAB18J48jUAfU0QAtf'
with open(civic_docs_data_path) as f:
    civic_docs_records = json.load(f)

# Extract project names related to 'design' from civic docs
projects_in_design = []
for doc in civic_docs_records:
    lines = doc['text'].split('\n')
    if 'design' in doc['text'].lower():
        for line in lines:
            if 'Improvements' in line:
                projects_in_design.append(line.strip())

# Clean up project names
projects_in_design = [project.split(':')[0].strip() for project in projects_in_design]

# Create DataFrame from funding records
funding_df = pd.DataFrame(funding_records)

# Filter the funding DataFrame for projects in design with funding > 50,000
filtered_projects = funding_df[(funding_df['Project_Name'].isin(projects_in_design)) & (funding_df['Amount'].astype(int) > 50000)]

# Count the number of such projects
count_of_projects = filtered_projects.shape[0]

# Print the result
print('__RESULT__:')
print(count_of_projects)"""

env_args = {'var_call_ftaQezTBmv5Al1wjsLpyDp6o': 'file_storage/call_ftaQezTBmv5Al1wjsLpyDp6o.json', 'var_call_Ll8AHgPQgrmHn41PEdkSmmIw': 'file_storage/call_Ll8AHgPQgrmHn41PEdkSmmIw.json', 'var_call_FMg9vplBr9GHN1E55wyBrM0i': 'file_storage/call_FMg9vplBr9GHN1E55wyBrM0i.json', 'var_call_CaySYkEAB18J48jUAfU0QAtf': 'file_storage/call_CaySYkEAB18J48jUAfU0QAtf.json'}

exec(code, env_args)

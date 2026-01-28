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

# Extract project names and status from civic docs
projects = []
for doc in civic_docs_records:
    text = doc.get('text', '')
    # Extract project information here based on known format,
    # This is a simplified example and may require robust parsing logic
    if 'Capital Improvement Projects (Design)' in text:
        projects += [line for line in text.split('\n') if 'Improvements' in line]

# Assume a simple logic that extracts the names and matches funding records
project_names_in_design_status = [project.split(':')[0].strip() for project in projects]

# Convert funding records to DataFrame for easier processing
funding_df = pd.DataFrame(funding_records)

# Filter funding_df for projects in the design status
filtered_funding = funding_df[funding_df['Project_Name'].isin(project_names_in_design_status)]

# Count how many have funding greater than $50,000
count_projects = filtered_funding[filtered_funding['Amount'].astype(int) > 50000].shape[0]

# Print the result
print('__RESULT__:')
print(count_projects)"""

env_args = {'var_call_ftaQezTBmv5Al1wjsLpyDp6o': 'file_storage/call_ftaQezTBmv5Al1wjsLpyDp6o.json', 'var_call_Ll8AHgPQgrmHn41PEdkSmmIw': 'file_storage/call_Ll8AHgPQgrmHn41PEdkSmmIw.json'}

exec(code, env_args)

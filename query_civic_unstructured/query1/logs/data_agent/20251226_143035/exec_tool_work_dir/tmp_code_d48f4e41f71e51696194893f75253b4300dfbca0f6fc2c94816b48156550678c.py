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

# Extract project names related to 'design' from civic docs
projects = []
for doc in civic_docs_records:
    if 'design' in doc['text'].lower():
        lines = doc['text'].split('\n')
        projects += [line for line in lines if 'Improvements' in line]

# Clean up the project names
projects = [project.split(':')[0].strip() for project in projects]

# Create DataFrame from funding records
funding_df = pd.DataFrame(funding_records)

# Filter the funding DataFrame for projects with funding > 50,000
count = (funding_df[funding_df['Project_Name'].isin(projects)]
             [funding_df['Amount'] > 50000].shape[0])

# Print the result in the required format
print('__RESULT__:')
print(count)"""

env_args = {'var_call_ftaQezTBmv5Al1wjsLpyDp6o': 'file_storage/call_ftaQezTBmv5Al1wjsLpyDp6o.json', 'var_call_Ll8AHgPQgrmHn41PEdkSmmIw': 'file_storage/call_Ll8AHgPQgrmHn41PEdkSmmIw.json'}

exec(code, env_args)

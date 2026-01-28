code = """import pandas as pd
import json

# Access the funding data from storage
funding_data = locals()['var_functions.query_db:0']

# Since it's a file path for large results, let's read it
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data

# Convert to DataFrame
df_funding = pd.DataFrame(funding_records)

# Convert Amount to integer
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Filter projects with funding > 50000
df_funding_gt_50k = df_funding[df_funding['Amount'] > 50000]

# Group project names for matching (handle the FEMA/CalOES variants)
project_names_list = df_funding_gt_50k['Project_Name'].tolist()

result = {
    'total_projects_over_50k': len(df_funding_gt_50k),
    'project_names': project_names_list
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

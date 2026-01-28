code = """import json
import pandas as pd

# Load project names that started in Spring 2022
project_names_spring_2022 = locals()['var_function-call-15042023778065350409']

# Load funding data
with open(locals()['var_function-call-1820665131150725703'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Filter funding data for projects that started in Spring 2022
filtered_funding_df = df_funding[df_funding['Project_Name'].isin(project_names_spring_2022)]

# Get the count of projects and convert to standard Python int
project_count = int(len(filtered_funding_df['Project_Name'].unique()))

# Calculate the total funding and convert to standard Python int
total_funding = int(filtered_funding_df['Amount'].astype(int).sum())

result = {
    "project_count": project_count,
    "total_funding": total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-5224027569778701662': 'file_storage/function-call-5224027569778701662.json', 'var_function-call-15042023778065350409': ['Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Malibu Park Drainage Improvements'], 'var_function-call-1820665131150725703': 'file_storage/function-call-1820665131150725703.json'}

exec(code, env_args)

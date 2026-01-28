code = """import json
import pandas as pd

# Load funding data
with open('/tmp/tmpf4d6q2f3.json', 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Filter for disaster projects (contain FEMA, CalOES, or CalJPIA)
is_disaster = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)
disaster_projects = funding_df[is_disaster]

# Filter for projects that started in 2022 (contain 2022 in name)
projects_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]

# Calculate total funding
total_funding = projects_2022['Amount'].sum()
num_projects = len(projects_2022)

# Create result
result = {
    'total_funding': int(total_funding),
    'num_projects': int(num_projects),
    'projects': projects_2022[['Project_Name', 'Amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

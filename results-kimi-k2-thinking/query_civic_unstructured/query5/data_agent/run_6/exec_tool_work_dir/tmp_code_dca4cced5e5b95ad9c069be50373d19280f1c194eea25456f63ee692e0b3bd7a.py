code = """import pandas as pd

# Access the funding data from the previous query
funding_data = var_functions.query_db_36
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Identify disaster projects (those with FEMA, CalOES, or CalJPIA in project name)
pattern = r'(FEMA|CalOES|CalJPIA)'
disaster_projects = funding_df[funding_df['Project_Name'].str.contains(pattern, case=False, na=False)]

# Filter for projects that started in 2022 (contain 2022 in the project name)
disaster_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]

# Calculate total funding
total_funding = disaster_2022['Amount'].sum()
num_projects = len(disaster_2022)

# Create result
result = {
    'total_funding': int(total_funding),
    'num_projects': int(num_projects),
    'projects': disaster_2022[['Project_Name', 'Amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)

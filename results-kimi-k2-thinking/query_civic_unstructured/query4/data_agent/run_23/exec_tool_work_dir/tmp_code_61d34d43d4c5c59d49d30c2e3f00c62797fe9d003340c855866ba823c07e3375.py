code = """import json
import pandas as pd

# Access funding data
funding_file = locals()['var_functions.query_db:17']

with open(funding_file, 'r') as f:
    funding = json.load(f)

# Create DataFrame and convert amount to numeric
df_funding = pd.DataFrame(funding)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Filter for projects with 2022 in the name
projects_2022 = df_funding[df_funding['Project_Name'].str.contains('2022', case=False, na=False)]

# Calculate total funding for 2022 projects
total_funding_2022 = projects_2022['Amount'].sum()

print('__RESULT__:')
print(json.dumps({
    'count_2022_projects': len(projects_2022),
    'total_funding_2022': int(total_funding_2022),
    'projects_2022': projects_2022[['Project_Name', 'Amount']].to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:22': {'civic_docs_count': 5, 'funding_count': 500, 'sample_civic_doc_filename': 'malibucity_agenda_03222023-2060.txt', 'total_funding_available': 28094000}, 'var_functions.execute_python:32': {'docs_with_spring_2022': 0, 'total_funding_records': 500, 'sample_refs': []}}

exec(code, env_args)

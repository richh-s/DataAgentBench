code = """# Get file paths from storage
civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

print('Civic docs file:', civic_path)
print('Funding file:', funding_path)

# Check if files exist
import os
print('Civic file exists:', os.path.exists(civic_path))
print('Funding file exists:', os.path.exists(funding_path))

result = {
    'civic_path': str(civic_path),
    'funding_path': str(funding_path),
    'civic_exists': os.path.exists(civic_path),
    'funding_exists': os.path.exists(funding_path)
}

print('__RESULT__:')
print(__import__('json').dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}}

exec(code, env_args)

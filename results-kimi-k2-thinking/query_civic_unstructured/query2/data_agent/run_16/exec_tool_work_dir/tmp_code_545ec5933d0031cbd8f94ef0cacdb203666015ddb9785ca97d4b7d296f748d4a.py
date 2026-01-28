code = """import json
import os

# Debug: See what variables are available
print('Available variables:')
for key in sorted(dir()):
    if not key.startswith('__'):
        print('  ' + key)

# Try to access the query results directly
try:
    funding_result = var_functions.query_db_8
    print('\nFunding result type: ' + str(type(funding_result)))
    print('Funding result (first 100 chars): ' + str(funding_result)[:100])
except Exception as e:
    print('\nError accessing funding result: ' + str(e))

try:
    civic_result = var_functions.query_db_10
    print('\nCivic result type: ' + str(type(civic_result)))
    print('Civic result (first 100 chars): ' + str(civic_result)[:100])
except Exception as e:
    print('\nError accessing civic result: ' + str(e))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

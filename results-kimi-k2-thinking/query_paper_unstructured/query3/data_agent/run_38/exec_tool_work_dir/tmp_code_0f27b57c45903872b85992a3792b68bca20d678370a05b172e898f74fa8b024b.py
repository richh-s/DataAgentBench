code = """import json
import re

# Get stored data
papers_data = locals()['var_functions.query_db:30']
citations_data = locals()['var_functions.query_db:28']

print('Type of papers_data:', type(papers_data))
print('Type of citations_data:', type(citations_data))
print('First 5 papers_data elements:', papers_data[:5])
print('First 5 citations_data elements:', citations_data[:5])

# Try to process citations - handle if items are strings
if citations_data:
    first_cit = citations_data[0]
    print('First citation type:', type(first_cit))
    print('First citation value:', first_cit)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:40': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App: 266 citations', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection: 265 citations'], 'var_functions.execute_python:48': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App: 266 citations', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection: 265 citations']}

exec(code, env_args)

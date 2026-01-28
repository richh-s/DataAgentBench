code = """import json
import re

# Get the data from storage using locals()
civic_docs_key = 'var_functions.query_db:16'
funding_data_key = 'var_functions.query_db:17'

civic_docs = locals()[civic_docs_key]
funding_data = locals()[funding_data_key]

print('Loaded ' + str(len(civic_docs)) + ' civic documents')
print('Loaded ' + str(len(funding_data)) + ' funding records')

# Check data types
print('Civic docs type: ' + str(type(civic_docs)))
print('Funding data type: ' + str(type(funding_data)))

# Sample data
if civic_docs and len(civic_docs) > 0:
    print('Sample civic doc keys: ' + str(list(civic_docs[0].keys())))
    
if funding_data and len(funding_data) > 0:
    print('Sample funding record: ' + str(funding_data[0]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)

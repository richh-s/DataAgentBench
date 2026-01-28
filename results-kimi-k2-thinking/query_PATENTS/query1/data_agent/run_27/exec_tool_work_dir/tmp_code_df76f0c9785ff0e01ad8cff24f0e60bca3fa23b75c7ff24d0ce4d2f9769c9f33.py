code = """import json
import pandas as pd
import re

# Load the data file for 2022
file_path = locals()['var_functions.query_db:42']
with open(file_path, 'r') as f:
    data_2022 = json.load(f)

print(f"Loaded {len(data_2022)} records from 2022")

# Also need to get data from previous years for EMA calculation
# Let's query for 2020, 2021, and 2022 data

# For now, let's just parse what we have and identify unique CPC codes at level 5
cpc_codes_2022 = set()

for row in data_2022:
    try:
        cpc_json = row['cpc']
        if isinstance(cpc_json, str):
            cpc_list = json.loads(cpc_json)
        else:
            cpc_list = cpc_json
            
        for cpc_entry in cpc_list:
            code = cpc_entry['code']
            # Check if it's a level 5 CPC code (format: XNNN/NN)
            if re.match(r'^[A-Z]\d{2}[A-Z]\d{2,}/\d{2,}$', code):
                cpc_codes_2022.add(code)
    except:
        continue

print(f"Found {len(cpc_codes_2022)} unique level 5 CPC codes in 2022")
print("Sample codes:", list(cpc_codes_2022)[:10])

# Now get historical data for these CPC codes to calculate EMA
# We'll need data from previous years

# For now, let's also load 2021 and 2020 data
# (We'll use a smaller sample to avoid timeout)

# Return the set of CPC codes for now as a starting point
result = json.dumps({'cpc_codes_2022': sorted(list(cpc_codes_2022))})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:32': [], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)

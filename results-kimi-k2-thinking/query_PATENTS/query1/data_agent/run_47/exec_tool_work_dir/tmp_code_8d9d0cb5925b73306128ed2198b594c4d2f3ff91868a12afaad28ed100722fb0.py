code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the data file from storage
data_file = locals()['var_functions.query_db:5']
with open(data_file, 'r') as f:
    raw_data = json.load(f)

# Inspect the raw structure of the first few records
first_cpc = raw_data[0]['cpc']
second_cpc = raw_data[1]['cpc']
third_cpc = raw_data[2]['cpc']

result = {
    "type_first_cpc": str(type(first_cpc)),
    "first_cpc_preview": str(first_cpc)[:300],
    "is_first_list": isinstance(first_cpc, list),
    "type_second_cpc": str(type(second_cpc)),
    "second_cpc_preview": str(second_cpc)[:300],
    "is_second_list": isinstance(second_cpc, list)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.execute_python:16': {'total_raw_records': 277813, 'parsed_records': 0, 'unique_cpc_codes': 0, 'year_range': '0 to 0', 'sample_cpc': [], 'data_check': False}}

exec(code, env_args)

code = """import json
import pandas as pd
import os

# Get file paths from storage
funding_file_path = locals()['var_functions.query_db:5']
civic_file_path = locals()['var_functions.query_db:12']

# Load funding data
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open(civic_file_path, 'r') as f:
    civic_data = json.load(f)

# Convert to DataFrames
funding_df = pd.DataFrame(funding_data)
civic_df = pd.DataFrame(civic_data)

print('__RESULT__:')
print(json.dumps({
    'funding_records': len(funding_df),
    'civic_documents': len(civic_df),
    'funding_columns': list(funding_df.columns),
    'sample_funding': funding_df.head(2).to_dict(orient='records')
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}}

exec(code, env_args)

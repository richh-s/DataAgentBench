code = """import json
import pandas as pd

# Load the full results from file
result_filepath = '/tmp/tmp6sps7xgk.json'
with open(result_filepath, 'r') as f:
    raw_data = json.load(f)

# Preview the first record to understand structure
preview_record = raw_data[0]
print('__RESULT__:')
print("First record keys:", str(list(preview_record.keys())))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

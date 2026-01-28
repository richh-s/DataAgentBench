code = """import json
import pandas as pd
import re

# Access the data from storage
funding_data = locals()['var_functions.query_db:5']
civic_docs_data = locals()['var_functions.query_db:12']

# Convert to DataFrames for easier processing
funding_df = pd.DataFrame(funding_data)
civic_df = pd.DataFrame(civic_docs_data)

# Display basic info to understand the data structure
print('__RESULT__:')
print(json.dumps({
    'funding_rows': len(funding_df),
    'civic_docs': len(civic_df),
    'funding_columns': list(funding_df.columns),
    'funding_sample': funding_df.head(3).to_dict(orient='records')
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

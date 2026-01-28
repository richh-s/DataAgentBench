code = """import json
import pandas as pd

# Get the file paths from storage
articles_path = locals()['var_functions.query_db:4']
metadata_path = locals()['var_functions.query_db:6']

# Load the data
with open(articles_path, 'r') as f:
    articles_data = json.load(f)

with open(metadata_path, 'r') as f:
    metadata_data = json.load(f)

# Create DataFrames
articles_df = pd.DataFrame(articles_data)
metadata_df = pd.DataFrame(metadata_data)

# Show basic info
result = {
    "articles_count": len(articles_df),
    "metadata_count": len(metadata_df),
    "articles_columns": list(articles_df.columns),
    "metadata_columns": list(metadata_df.columns)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

code = """import json

# Load the full results
articles_file = var_functions.query_db:4
metadata_file = var_functions.query_db:6

# Read the articles data
with open(articles_file, 'r') as f:
    articles_data = json.load(f)

# Read the metadata data
with open(metadata_file, 'r') as f:
    metadata_data = json.load(f)

# Convert lists to dataframes for easier processing
import pandas as pd

articles_df = pd.DataFrame(articles_data)
metadata_df = pd.DataFrame(metadata_data)

print('__RESULT__:')
print(f"Articles count: {len(articles_df)}, Metadata count: {len(metadata_df)}")
print(f"Articles columns: {list(articles_df.columns)}")
print(f"Metadata columns: {list(metadata_df.columns)}")
print(f"Sample articles:\n{articles_df.head(3).to_string()}")
print(f"Sample metadata:\n{metadata_df.head(3).to_string()}")"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

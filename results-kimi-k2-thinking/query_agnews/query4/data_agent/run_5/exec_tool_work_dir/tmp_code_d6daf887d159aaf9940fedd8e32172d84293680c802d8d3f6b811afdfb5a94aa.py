code = """import json
import pandas as pd

# Load the metadata from the JSON file
metadata_file = var_functions.query_db:2
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Create a DataFrame for easier processing
df_metadata = pd.DataFrame(metadata_2015)

# Get unique article IDs
article_ids = df_metadata['article_id'].tolist()
print('__RESULT__:')
print(json.dumps({"count": len(article_ids), "sample_ids": article_ids[:10]}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

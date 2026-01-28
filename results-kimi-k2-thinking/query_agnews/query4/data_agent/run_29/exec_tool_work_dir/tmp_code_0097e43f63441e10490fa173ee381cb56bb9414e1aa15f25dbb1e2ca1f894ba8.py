code = """import json
import pandas as pd

# Load metadata results
metadata_path = var_functions.query_db:2
with open(metadata_path, 'r') as f:
    metadata_2015 = json.load(f)

# Create DataFrame for easier processing
metadata_df = pd.DataFrame(metadata_2015)
metadata_df['article_id'] = metadata_df['article_id'].astype(int)

# Get article IDs for 2015
article_ids_2015 = metadata_df['article_id'].tolist()
print('__RESULT__:')
print(json.dumps({
    'metadata_count': len(article_ids_2015),
    'sample_metadata': metadata_df.head().to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

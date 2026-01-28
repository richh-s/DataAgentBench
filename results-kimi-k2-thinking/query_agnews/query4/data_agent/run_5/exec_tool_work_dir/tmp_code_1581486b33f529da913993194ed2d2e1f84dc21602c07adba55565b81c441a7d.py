code = """import json
import pandas as pd

# Load metadata file
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Create DataFrame of 2015 metadata
df_2015 = pd.DataFrame(metadata_2015)
df_2015['article_id'] = df_2015['article_id'].astype(int)

# Group by region to see counts
region_counts = df_2015['region'].value_counts()
print('__RESULT__:')
print(json.dumps({
    'total_articles_2015': len(df_2015),
    'regions': region_counts.to_dict(),
    'sample_article_ids': df_2015['article_id'].head(5).tolist()
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'total_articles_2015': 6696, 'sample_article_ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}, 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)

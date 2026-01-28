code = """import json
import pandas as pd

# Read the JSON data files
with open('var_functions.query_db:2', 'r') as f:
    metadata_data = json.load(f)

with open('var_functions.query_db:5', 'r') as f:
    articles_data = json.load(f)

# Convert to DataFrames
metadata_df = pd.DataFrame(metadata_data)
articles_df = pd.DataFrame(articles_data)

# Convert article_id to integer for proper joining
metadata_df['article_id'] = pd.to_numeric(metadata_df['article_id'], errors='coerce')
articles_df['article_id'] = pd.to_numeric(articles_df['article_id'], errors='coerce')

# Merge the dataframes
merged_df = pd.merge(metadata_df, articles_df, on='article_id', how='inner')

# Sample data to verify merge worked
sample_data = merged_df.head(3).to_dict('records')

result = {
    'articles_2015': len(metadata_df),
    'matched_articles': len(merged_df),
    'columns': list(merged_df.columns),
    'sample': sample_data
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

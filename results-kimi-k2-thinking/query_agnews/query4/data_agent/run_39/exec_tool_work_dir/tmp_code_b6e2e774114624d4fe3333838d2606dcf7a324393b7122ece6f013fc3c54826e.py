code = """import json
import pandas as pd

# Read the metadata results
metadata_file = var_functions.query_db:2
with open(metadata_file, 'r') as f:
    metadata_data = json.load(f)

# Read the articles results
articles_file = var_functions.query_db:5
with open(articles_file, 'r') as f:
    articles_data = json.load(f)

# Convert to DataFrames
metadata_df = pd.DataFrame(metadata_data)
articles_df = pd.DataFrame(articles_data)

# Convert article_id to int for proper joining
metadata_df['article_id'] = metadata_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

print('__RESULT__:')
print(json.dumps({
    'metadata_shape': metadata_df.shape,
    'articles_shape': articles_df.shape,
    'metadata_columns': list(metadata_df.columns),
    'articles_columns': list(articles_df.columns),
    'sample_metadata': metadata_df.head(2).to_dict('records'),
    'sample_articles': articles_df.head(2).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json
import pandas as pd
from collections import Counter

# Get file paths from storage
articles_path = locals()['var_functions.query_db:4']
metadata_2015_path = locals()['var_functions.query_db:22']

# Load all articles
with open(articles_path, 'r') as f:
    articles_data = json.load(f)

# Load 2015 metadata
with open(metadata_2015_path, 'r') as f:
    metadata_2015 = json.load(f)

articles_df = pd.DataFrame(articles_data)
metadata_2015_df = pd.DataFrame(metadata_2015)

# Check data sizes
result = {
    "total_articles": len(articles_df),
    "articles_2015": len(metadata_2015_df),
    "sample_articles": articles_df.head(2).to_dict('records'),
    "sample_metadata": metadata_2015_df.head(2).to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'articles_count': 10000, 'metadata_count': 127600, 'articles_columns': ['article_id', 'title', 'description'], 'metadata_columns': ['article_id', 'author_id', 'region', 'publication_date']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

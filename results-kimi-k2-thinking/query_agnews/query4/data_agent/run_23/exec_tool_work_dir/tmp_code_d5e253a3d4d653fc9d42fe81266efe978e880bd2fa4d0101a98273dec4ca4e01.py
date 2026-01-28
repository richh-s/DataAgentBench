code = """import json
import pandas as pd
from collections import Counter

# Load the data
articles_path = locals()['var_functions.query_db:4']
metadata_2015_path = locals()['var_functions.query_db:22']

with open(articles_path, 'r') as f:
    articles_data = json.load(f)

with open(metadata_2015_path, 'r') as f:
    metadata_2015 = json.load(f)

articles_df = pd.DataFrame(articles_data)
metadata_2015_df = pd.DataFrame(metadata_2015)

# Merge
articles_2015_df = articles_df.merge(metadata_2015_df, on='article_id', how='inner')

result_info = {
    "merged_count": len(articles_2015_df),
    "regions_available": articles_2015_df['region'].value_counts().to_dict()
}

print('__RESULT__:')
print(json.dumps(result_info))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'articles_count': 10000, 'metadata_count': 127600, 'articles_columns': ['article_id', 'title', 'description'], 'metadata_columns': ['article_id', 'author_id', 'region', 'publication_date']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'total_articles': 10000, 'articles_2015': 6696, 'sample_articles': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}], 'sample_metadata': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}]}}

exec(code, env_args)

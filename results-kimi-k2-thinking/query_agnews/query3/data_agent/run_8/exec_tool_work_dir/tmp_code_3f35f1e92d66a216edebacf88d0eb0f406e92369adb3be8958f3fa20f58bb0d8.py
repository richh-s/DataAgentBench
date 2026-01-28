code = """import json
import pandas as pd
from datetime import datetime

# Load the metadata query result
metadata_file_path = var_functions.query_db:5
print(f"Metadata file path: {metadata_file_path}")

with open(metadata_file_path, 'r') as f:
    metadata_records = json.load(f)

# Convert to DataFrame
metadata_df = pd.DataFrame(metadata_records)
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_df['year'] = metadata_df['publication_date'].dt.year

print(f"Total Europe articles 2010-2020: {len(metadata_df)}")
print(f"Year range: {metadata_df['year'].min()} - {metadata_df['year'].max()}")

# Extract unique article IDs
article_ids = [int(x) for x in metadata_df['article_id'].tolist()]
print(f"Sample article IDs: {article_ids[:10]}")

# We need to find which of these are Business articles
# But first we need to get the articles data from MongoDB
# Let's prepare the query for MongoDB

print("__RESULT__:")
print(json.dumps({"metadata_count": len(metadata_df), "article_id_count": len(article_ids), "year_min": int(metadata_df['min']), "year_max": int(metadata_df['year'].max())}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

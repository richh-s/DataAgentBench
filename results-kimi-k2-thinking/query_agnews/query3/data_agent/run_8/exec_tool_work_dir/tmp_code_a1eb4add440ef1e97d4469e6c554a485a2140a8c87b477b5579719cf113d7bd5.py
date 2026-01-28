code = """import json
import pandas as pd

# Load the metadata result
metadata_path = var_functions.query_db:5
with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

print(f"Total European articles (2010-2020): {len(metadata_records)}")

# Create a DataFrame
metadata_df = pd.DataFrame(metadata_records)
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_df['year'] = metadata_df['publication_date'].dt.year

# Check year distribution
year_counts = metadata_df['year'].value_counts().sort_index()
print(f"\nArticles per year:")
print(year_counts)

# Get all unique article IDs
article_ids = sorted(set([int(x) for x in metadata_df['article_id'].tolist()]))
print(f"\nTotal unique article IDs: {len(article_ids)}")
print(f"First 10 article IDs: {article_ids[:10]}")
print(f"Last 10 article IDs: {article_ids[-10:]}")

# Calculate total years
year_range = range(2010, 2021)
total_years = len(year_range)
print(f"\nTotal years (2010-2020 inclusive): {total_years}")

print("__RESULT__:")
print(json.dumps({
    "total_articles": len(metadata_records),
    "unique_articles": len(article_ids),
    "year_counts": year_counts.to_dict(),
    "total_years": total_years
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Read the review data from the file
with open('var_functions.query_db:2', 'r') as f:
    reviews_2018 = json.load(f)

# Convert to DataFrame for easier manipulation
df_reviews = pd.DataFrame(reviews_2018)

# Extract unique businesses that received reviews in 2018
unique_business_refs_2018 = df_reviews['business_ref'].unique().tolist()

# Show some statistics
print(f"Total reviews in 2018: {len(df_reviews)}")
print(f"Unique businesses with reviews in 2018: {len(unique_business_refs_2018)}")
print(f"Sample business refs: {unique_business_refs_2018[:5]}")

# __RESULT__:
print(json.dumps({
    'total_reviews_2018': len(df_reviews),
    'unique_business_count': len(unique_business_refs_2018),
    'business_refs': unique_business_refs_2018
}))"""

env_args = {'var_functions.list_db:0': ['review', 'tip', 'user'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

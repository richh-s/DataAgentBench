code = """import json
# Read the full 2015 article metadata from file
file_path = var_functions.query_db:4
with open(file_path, 'r') as f:
    articles_2015_metadata = json.load(f)

# Convert to DataFrame for easier handling
import pandas as pd
df_metadata = pd.DataFrame(articles_2015_metadata)
print(f"Total articles in 2015: {len(df_metadata)}")
print(df_metadata.head())

# Get the list of article_ids
article_ids_2015 = df_metadata['article_id'].tolist()

# Now query MongoDB for these articles
db_name = "articles_database"
collection = "articles"
# Create a MongoDB query for articles with these article_ids
# Convert to string format for MongoDB query
article_ids_str = json.dumps(article_ids_2015)

# We'll construct the query string for MongoDB
query_str = json.dumps({
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids_2015}},
    "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}
})

# Use execute_python to create a variable we can reference in the next query
print('__RESULT__:')
print(json.dumps({"query": query_str, "count": len(article_ids_2015)}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'author_id': '268', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'author_id': '470', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'author_id': '387', 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'author_id': '684', 'region': 'Africa', 'publication_date': '2015-06-02'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

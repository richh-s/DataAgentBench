code = """import json
import pandas as pd

# Load the result from the previous SQL query
with open('var_function-call-12548450677556957208.json', 'r') as f:
    sql_data = json.load(f)

# Extract article_ids
article_ids = [int(entry['article_id']) for entry in sql_data]
print(f"Total articles in 2015: {len(article_ids)}")

# Prepare the MongoDB query
# We will select articles where article_id is in the list
# We need title and description to classify
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}
}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-12548450677556957208': 'file_storage/function-call-12548450677556957208.json'}

exec(code, env_args)

code = """import json
import pandas as pd

with open(locals()['var_function-call-7345730232889374380'], 'r') as f:
    articles_2015 = json.load(f)

articles_2015_df = pd.DataFrame(articles_2015)
article_ids_2015 = articles_2015_df['article_id'].tolist()

# Split the list into chunks of 100 to avoid exceeding the query limit
chunk_size = 100
article_id_chunks = [article_ids_2015[i:i + chunk_size] for i in range(0, len(article_ids_2015), chunk_size)]

# Create a list of MongoDB queries for each chunk
mongo_queries = []
for chunk in article_id_chunks:
    query = {
        "collection": "articles",
        "filter": {"article_id": {"$in": chunk}},
        "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}
    }
    mongo_queries.append(query)

print('__RESULT__:')
print(json.dumps(mongo_queries))"""

env_args = {'var_function-call-7345730232889374380': 'file_storage/function-call-7345730232889374380.json'}

exec(code, env_args)

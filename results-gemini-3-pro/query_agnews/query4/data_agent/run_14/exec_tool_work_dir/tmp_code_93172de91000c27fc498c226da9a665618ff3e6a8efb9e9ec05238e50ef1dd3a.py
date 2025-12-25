code = """import json

# Load IDs
file_path = locals()['var_function-call-14238142441611435889']
with open(file_path, 'r') as f:
    data = json.load(f)

article_ids = [int(x) for x in data['article_ids']]
total_ids = len(article_ids)

# Split into chunks of 1000
chunk_size = 1000
chunks = [article_ids[i:i + chunk_size] for i in range(0, len(article_ids), chunk_size)]

# Prepare queries for all chunks
queries = []
for chunk in chunks:
    q = {
        "collection": "articles",
        "filter": {
            "article_id": {"$in": chunk}
        },
        "projection": {
            "_id": 0,
            "article_id": 1,
            "title": 1,
            "description": 1
        }
    }
    queries.append(q)

# Save queries to a file for later use
with open('queries.json', 'w') as f:
    json.dump(queries, f)

# Return the first query and the number of chunks
print("__RESULT__:")
print(json.dumps({
    "total_ids": total_ids,
    "num_chunks": len(chunks),
    "first_query": queries[0]
}))"""

env_args = {'var_function-call-17386204446982133767': 'file_storage/function-call-17386204446982133767.json', 'var_function-call-14238142441611435889': 'file_storage/function-call-14238142441611435889.json', 'var_function-call-5963990079878715096': 'file_storage/function-call-5963990079878715096.json'}

exec(code, env_args)

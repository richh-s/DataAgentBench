code = """import json

# Load the SQLite result
with open(locals()['var_function-call-4059042724151098954'], 'r') as f:
    citations_data = json.load(f)

# Extract titles and create filenames
titles = [record['title'] for record in citations_data]
filenames = [t + ".txt" for t in titles]

print(f"Number of papers: {len(filenames)}")

# Prepare the query for MongoDB
# We'll use the filenames to fetch the documents
query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": filenames}},
    "projection": {"filename": 1, "text": 1}
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-4059042724151098954': 'file_storage/function-call-4059042724151098954.json'}

exec(code, env_args)

code = """import json

# Read the full MongoDB query result
mongo_result_path = locals()['var_functions.query_db:2']
print(f"Reading MongoDB results from: {mongo_result_path}")

# Read and parse the JSON file
with open(mongo_result_path, 'r') as f:
    papers = json.load(f)

print(f"Total number of papers in database: {len(papers)}")
print(f"First paper structure keys: {list(papers[0].keys()) if papers else 'No papers'}")

# Let's examine a few papers to understand the structure
if papers:
    sample = papers[0]
    print(f"\nSample paper filename: {sample.get('filename')}")
    print(f"Sample paper text preview (first 500 chars):\n{sample.get('text', '')[:500]}")

# Storage reference
print(f"\nMongoDB results stored in: var_functions.query_db:2")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

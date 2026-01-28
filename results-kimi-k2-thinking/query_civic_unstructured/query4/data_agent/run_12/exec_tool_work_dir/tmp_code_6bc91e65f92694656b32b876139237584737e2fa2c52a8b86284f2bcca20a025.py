code = """import json

# Load the full results from the file
result_file_key = 'functions.query_db:2'
result_file = var_functions.query_db:2

# Read the full results
with open(result_file, 'r') as f:
    all_docs = json.load(f)

print(f"Total documents in civic_docs collection: {len(all_docs)}")
print(f"Sample document structure:")
print(json.dumps(all_docs[0], indent=2))
print("\n" + "="*50 + "\n")

# Explore the text content to understand project structure
for i, doc in enumerate(all_docs[:3]):
    if i >= 3:
        break
    print(f"Document {i+1} filename: {doc.get('filename', 'N/A')}")
    print(f"Document {i+1} text preview (first 500 chars):")
    print(doc.get('text', '')[:500] + "...")
    print("\n" + "-"*50 + "\n")

print("__RESULT__:")
print("Analysis started successfully")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

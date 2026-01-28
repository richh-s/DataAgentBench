code = """# Access the civic_docs data from storage
civic_docs = locals()['var_functions.query_db:2']

print(f"Type of data: {type(civic_docs)}")

# Check if it's a list or a string (file path)
if isinstance(civic_docs, str):
    print(f"File path: {civic_docs}")
    # Load from file
    import json
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")
print("Sample document preview:")
sample = civic_docs[0]
print(f"Keys: {list(sample.keys())}")
print(f"Filename: {sample.get('filename')}")
print(f"Text snippet: {sample.get('text', '')[:500]}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

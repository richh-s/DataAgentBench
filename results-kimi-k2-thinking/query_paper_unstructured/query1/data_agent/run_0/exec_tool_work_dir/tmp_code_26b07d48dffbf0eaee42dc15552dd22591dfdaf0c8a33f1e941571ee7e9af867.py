code = """# Check what variables are available
import json

# List available variables
available_vars = [var for var in dir() if var.startswith('var_')]
print("Available variables:", available_vars)

# Access the MongoDB query results using locals()
paper_docs_key = 'var_functions.query_db:4'
if paper_docs_key in locals():
    paper_docs = locals()[paper_docs_key]
    print(f"Type of paper_docs: {type(paper_docs)}")
    print(f"Is list: {isinstance(paper_docs, list)}")
    if isinstance(paper_docs, list):
        print(f"Number of documents: {len(paper_docs)}")
        if len(paper_docs) > 0:
            print(f"First document keys: {paper_docs[0].keys() if isinstance(paper_docs[0], dict) else 'Not a dict'}")
else:
    print("var_functions.query_db:4 not found in locals()")

# Also check var_functions.query_db:2
paper_docs_key2 = 'var_functions.query_db:2'
if paper_docs_key2 in locals():
    paper_docs2 = locals()[paper_docs_key2]
    print(f"\nType of paper_docs2: {type(paper_docs2)}")
    print(f"Is string (file path): {isinstance(paper_docs2, str)}")
    if isinstance(paper_docs2, str):
        print(f"File path: {paper_docs2}")
else:
    print("var_functions.query_db:2 not found in locals()")

# Check if result is stored as string (file path)
# Try to load from file if it's a string
if 'var_functions.query_db:2' in locals():
    result_path = locals()['var_functions.query_db:2']
    if isinstance(result_path, str):
        try:
            with open(result_path, 'r') as f:
                paper_docs = json.load(f)
            print(f"Successfully loaded {len(paper_docs)} documents from file")
            print(f"Type: {type(paper_docs)}")
            if len(paper_docs) > 0:
                print(f"Sample document: {paper_docs[0]}")
        except Exception as e:
            print(f"Error loading file: {e}")

print('__RESULT__:')
print(json.dumps("data_loaded"))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)

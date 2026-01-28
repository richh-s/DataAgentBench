code = """# Access the stored file paths from previous queries
paper_docs_path = locals().get('var_functions.query_db:22')
citations_path = locals().get('var_functions.query_db:24')

print("Paper docs path:", paper_docs_path)
print("Citations path:", citations_path)

# Count records to verify
import json

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)
    print(f"Paper documents loaded: {len(paper_docs)}")

with open(citations_path, 'r') as f:
    citations = json.load(f)
    print(f"Citations loaded: {len(citations)}")

print("__RESULT__:")
print(f"Loaded {len(paper_docs)} papers and {len(citations)} citation records")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)

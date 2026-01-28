code = """import json

# The results are stored as file paths, so read them directly
paper_docs_path = "/tmp/tmp7m3i4o0e.json"  # This would be var_functions.query_db:8
citations_path = "/tmp/tmp0r06q0n7.json"   # This would be var_functions.query_db:5

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

print(f"Total papers in MongoDB: {len(paper_docs)}")
print(f"Total citations in 2020: {len(citations_2020)}")

# Let's look at the structure of the data
print(f"\nFirst paper doc structure: {list(paper_docs[0].keys())}")
print(f"First paper doc filename: {paper_docs[0].get('filename')}")
print(f"First paper doc text snippet: {paper_docs[0].get('text', '')[:200]}")

print(f"\nFirst citation structure: {list(citations_2020[0].keys())}")
print(f"First citation title: {citations_2020[0].get('title')}")
print(f"First citation count: {citations_2020[0].get('citation_count')}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

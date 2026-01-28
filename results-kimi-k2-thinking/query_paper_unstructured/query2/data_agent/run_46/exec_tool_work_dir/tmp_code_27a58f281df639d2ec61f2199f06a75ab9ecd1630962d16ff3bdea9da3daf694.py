code = """import json
import ast

# Read the citations data for 2018
citations_file = var_functions.query_db:0
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_file

# Read the paper documents data
papers_file = var_functions.query_db:2
if isinstance(papers_file, str) and papers_file.endswith('.json'):
    with open(papers_file, 'r') as f:
        content = f.read()
        papers_2018 = json.loads(content)
else:
    papers_2018 = papers_file

print(f"Number of citations in 2018: {len(citations_2018)}")
print(f"Number of paper documents: {len(papers_2018)}")

# Show first few records to understand structure
print("\nFirst few citations:")
for i, c in enumerate(citations_2018[:3]):
    print(f"  {i}: {c}")

print("\nFirst few paper docs:")
for i, p in enumerate(papers_2018[:2]):
    print(f"  {i}: {p.get('filename', 'No filename')}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

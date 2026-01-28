code = """import json

# Access the citations data for 2018 from stored variables
citations_2018 = locals()['var_functions.query_db:0']

# Access the paper documents data from stored variables
paper_docs = locals()['var_functions.query_db:2']

# Check if these are file paths (strings) or actual data
if isinstance(citations_2018, str) and citations_2018.endswith('.json'):
    with open(citations_2018, 'r') as f:
        citations_2018 = json.load(f)

if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

print(f"Number of citations in 2018: {len(citations_2018)}")
print(f"Number of paper documents: {len(paper_docs)}")

# Show first few records to understand structure
print("\nFirst few citations:")
for i, c in enumerate(citations_2018[:3]):
    print(f"  {i}: title='{c.get('title', 'N/A')}', citations={c.get('citation_count', 'N/A')}")

print("\nFirst few paper docs:")
for i, p in enumerate(paper_docs[:2]):
    filename = p.get('filename', 'No filename')
    print(f"  {i}: filename='{filename}'")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

code = """import json

# Load the paper documents
paper_data = var_functions.query_db:3
print("Type of paper_data:", type(paper_data))

if isinstance(paper_data, str) and paper_data.endswith('.json'):
    with open(paper_data, 'r') as f:
        paper_docs = json.load(f)
    print("Loaded paper_docs from file")
else:
    paper_docs = paper_data
    print("Used paper_data directly")

print("Number of papers:", len(paper_docs))
print("First paper keys:", list(paper_docs[0].keys()))
print("First paper filename:", paper_docs[0].get('filename'))
print("First paper text preview:", paper_docs[0].get('text')[:200])

# Load the citations
citation_data = var_functions.query_db:2
print("\nType of citation_data:", type(citation_data))

if isinstance(citation_data, str) and citation_data.endswith('.json'):
    with open(citation_data, 'r') as f:
        citations = json.load(f)
    print("Loaded citations from file")
else:
    citations = citation_data
    print("Used citation_data directly")

print("Number of citations:", len(citations))
print("First citation:", citations[0])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

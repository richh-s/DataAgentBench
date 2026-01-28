code = """import json

# Load citation data from 2018
citations_var = var_functions.query_db:0
if isinstance(citations_var, str) and citations_var.endswith('.json'):
    with open(citations_var, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_var

# Load paper documents
papers_var = var_functions.query_db:2
if isinstance(papers_var, str) and papers_var.endswith('.json'):
    with open(papers_var, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_var

print("Number of citation records in 2018:", len(citations_data))
print("Number of paper documents:", len(papers_data))

# Preview first few records
print("\nFirst citation record:")
print(citations_data[0] if citations_data else "No data")

print("\nFirst paper document:")
print(papers_data[0] if papers_data else "No data")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

code = """import json
import re

# Load citation data from 2018
citations_data = var_citations_2018

# Load paper documents
papers_data = var_papers_docs

print(f"Number of citation records in 2018: {len(citations_data)}")
print(f"Number of paper documents: {len(papers_data)}")

# Preview first few records to understand the structure
print("\nFirst citation record:")
print(citations_data[0] if citations_data else "No data")

print("\nFirst paper document:")
print(papers_data[0] if papers_data else "No data")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

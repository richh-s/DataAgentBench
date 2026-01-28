code = """import json
import pandas as pd

# Access the results from previous queries
mongo_data = var_functions.query_db:3
citation_data = var_functions.query_db:2

# Load the data if they are file paths (strings), otherwise use directly
paper_docs = json.load(open(mongo_data, 'r')) if isinstance(mongo_data, str) and mongo_data.endswith('.json') else mongo_data
citations = json.load(open(citation_data, 'r')) if isinstance(citation_data, str) and citation_data.endswith('.json') else citation_data

print("Number of papers:", len(paper_docs))
print("Number of citations:", len(citations))

# Show structure
print("\nFirst paper sample:")
print("Keys:", list(paper_docs[0].keys()))
print("Filename:", paper_docs[0]['filename'][:100])

print("\nFirst citation sample:")
print("Keys:", list(citations[0].keys()))
print("Data:", citations[0])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

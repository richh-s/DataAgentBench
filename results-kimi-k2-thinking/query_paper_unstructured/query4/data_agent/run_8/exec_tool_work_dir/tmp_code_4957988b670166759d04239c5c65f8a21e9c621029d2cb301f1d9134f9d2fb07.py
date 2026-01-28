code = """import json
import pandas as pd
import re
from collections import defaultdict

# Check what variables are available
print("Available variables:")
for var_name in list(locals().keys()):
    if 'var_functions' in var_name:
        print(f"- {var_name}")

# Load the data from the stored variables
# Paper docs (MongoDB) - from query_db:14
paper_docs = locals().get('var_functions.query_db:14', [])
if isinstance(paper_docs, str):
    # It's a file path
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs

print(f"\nPaper docs type: {type(paper_docs)}")
print(f"Paper docs length: {len(paper_docs) if paper_docs else 'None'}")

# Citations - from query_db:15
citations_data = locals().get('var_functions.query_db:15', [])
if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_data

print(f"\nCitations data type: {type(citations_data)}")
print(f"Citations data length: {len(citations_data) if citations_data else 'None'}")

if citations_data:
    df_citations = pd.DataFrame(citations_data)
    print(f"Citations columns: {df_citations.columns.tolist()}")
    print(f"Citations sample:\n{df_citations.head()}")
else:
    print("No citations data found")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)

code = """import json
import pandas as pd
import sys

# Read the full funding data from the file
with open('var_functions.query_db:14.json', 'r') as f:
    funding_data = json.load(f)

# Convert to DataFrame
funding_df = pd.DataFrame(funding_data)

# Convert Amount to numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print(f"Total funding records: {len(funding_df)}")
print(f"Sample funding data:")
print(funding_df.head().to_string())

# Read the project documents - let's check what's in both files
with open('var_functions.query_db:2.json', 'r') as f:
    project_docs_2022 = json.load(f)

with open('var_functions.query_db:16.json', 'r') as f:
    project_docs_all = json.load(f)

print(f"\nAll project docs count: {len(project_docs_all)}")
print(f"2022 project docs count: {len(project_docs_2022)}")

# Let's work with the 2022 filtered documents
documents = project_docs_2022

print("First document:")
print(json.dumps(documents[0], indent=2)[:2000])

# Create a list of texts for parsing
texts = [doc['text'] for doc in documents]
print(f"\nNumber of texts: {len(texts)}")
print(f"Sample text excerpt: {texts[0][:500]}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)

code = """import json

# Load the citations data from storage
citations_data = locals()['var_functions.query_db:2']

# If it's a file path, load it
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_data

print('Number of citation records:', len(citations))
print('Keys in first citation record:', list(citations[0].keys()))
print('First citation:', citations[0])

# Show more samples to understand structure
for i in range(min(5, len(citations))):
    print(f'Citation {i}:', citations[i])

# Try pandas to see all columns
try:
    import pandas as pd
    df = pd.DataFrame(citations)
    print('\nAll columns:', df.columns.tolist())
    print('\nDataFrame head:')
    print(df.head())
except Exception as e:
    print('Error creating DataFrame:', e)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}}

exec(code, env_args)

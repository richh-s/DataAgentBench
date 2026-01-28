code = """import json
import pandas as pd

# Access the citations data from storage
citations_2020 = locals()['var_functions.query_db:0']

# Since the data might be a file path string for large results, let's check
if isinstance(citations_2020, str) and citations_2020.endswith('.json'):
    # It's a file path
    with open(citations_2020, 'r') as f:
        citations_2020 = json.load(f)

# Create DataFrame
df_citations = pd.DataFrame(citations_2020)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

total_records = len(citations_2020)
print('__RESULT__:')
print(f'Loaded {total_records} citation records for 2020')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

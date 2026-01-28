code = """import json
import pandas as pd

# Load the citation data from the file
citations_file_path = '/tmp/tmpkfxl1v1z.json'
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

# Create DataFrame
df_citations = pd.DataFrame(citations_2020)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

total_records = len(citations_2020)
print('__RESULT__:')
print(f'Loaded {total_records} citation records for 2020')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

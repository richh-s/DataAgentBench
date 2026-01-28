code = """import json
import pandas as pd

# Access the citations data from storage
citations_2020_data = locals().get('var_functions.query_db:0')

# Check if it's a file path string or the actual data
if isinstance(citations_2020_data, str) and citations_2020_data.endswith('.json'):
    # It's a file path
    with open(citations_2020_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    # It's the actual data
    citations_2020 = citations_2020_data

# Create DataFrame
df_citations = pd.DataFrame(citations_2020)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

total_records = len(citations_2020)
result = {"status": "success", "total_records": total_records, "message": f"Loaded {total_records} citation records for 2020"}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

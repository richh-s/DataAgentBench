code = """import pandas as pd
import json

# Load the data from the previous query
var_name = 'var_functions.query_db:2'
result_file = locals().get(var_name)

if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        data = json.load(f)
else:
    data = result_file

# Convert to DataFrame to explore structure
df = pd.DataFrame(data)
print('__RESULT__:')
print(json.dumps({
    'num_records': len(df),
    'columns': df.columns.tolist(),
    'sample_patents_info': [str(x) for x in df['Patents_info'].head(3).tolist()],
    'sample_citations': [str(x) for x in df['citation'].head(3).tolist()],
    'sample_cpc': [str(x) for x in df['cpc'].head(3).tolist()]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

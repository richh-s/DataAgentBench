code = """import json
import pandas as pd

# Read the 2015 articles metadata from the JSON file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Create a DataFrame
df_2015 = pd.DataFrame(metadata_2015)

# Show basic info about the data
result = {
    "total_articles_2015": len(df_2015),
    "columns": list(df_2015.columns),
    "sample_rows": df_2015.head(3).to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

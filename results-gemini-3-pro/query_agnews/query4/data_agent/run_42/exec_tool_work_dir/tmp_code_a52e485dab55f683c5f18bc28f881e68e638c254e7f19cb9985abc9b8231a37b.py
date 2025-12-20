code = """import json
import pandas as pd

# Get the file path from the variable
file_path = locals()['var_function-call-230048583216778633']

# Load the SQL result
with open(file_path, 'r') as f:
    metadata_records = json.load(f)

# Convert to DataFrame
df_metadata = pd.DataFrame(metadata_records)

# Get list of article_ids
article_ids = df_metadata['article_id'].astype(int).tolist()

print("__RESULT__:")
print(json.dumps({
    "count": len(article_ids),
    "sample_ids": article_ids[:10],
    "regions": df_metadata['region'].unique().tolist()
}))"""

env_args = {'var_function-call-230048583216778633': 'file_storage/function-call-230048583216778633.json'}

exec(code, env_args)

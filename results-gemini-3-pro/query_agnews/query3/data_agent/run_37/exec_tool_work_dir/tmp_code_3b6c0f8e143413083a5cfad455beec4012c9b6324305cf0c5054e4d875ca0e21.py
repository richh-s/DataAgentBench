code = """import json
import pandas as pd

# Load the SQL result
with open(locals()['var_function-call-7163315103813395117'], 'r') as f:
    metadata_records = json.load(f)

# Extract article IDs
article_ids = [r['article_id'] for r in metadata_records]

# Convert to integers if they are strings in the json (the preview showed them as strings "3", "9"...)
# The DB description says article_id is int. Let's make sure.
article_ids = [int(x) for x in article_ids]

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-7163315103813395117': 'file_storage/function-call-7163315103813395117.json'}

exec(code, env_args)

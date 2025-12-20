code = """import json
import pandas as pd

# Load the result from the previous step
with open(locals()['var_function-call-8183838540505517503'], 'r') as f:
    metadata_records = json.load(f)

# Extract article_ids
article_ids = [int(r['article_id']) for r in metadata_records]

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-8183838540505517503': 'file_storage/function-call-8183838540505517503.json'}

exec(code, env_args)

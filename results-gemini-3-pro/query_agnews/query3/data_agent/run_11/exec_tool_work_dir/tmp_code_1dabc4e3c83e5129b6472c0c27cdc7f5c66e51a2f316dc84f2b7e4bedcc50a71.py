code = """import json
import pandas as pd

# Load the metadata result
with open('var_function-call-5463793062581898541.json', 'r') as f:
    metadata = json.load(f)

# Extract article_ids
article_ids = [int(item['article_id']) for item in metadata]

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-5463793062581898541': 'file_storage/function-call-5463793062581898541.json'}

exec(code, env_args)

code = """import pandas as pd
import json

# Load the full result from the file
with open(locals()['var_function-call-4142005257738235693'], 'r') as f:
    article_metadata_2015 = json.load(f)

article_ids_2015 = [article['article_id'] for article in article_metadata_2015]
print("__RESULT__:")
print(json.dumps(article_ids_2015))"""

env_args = {'var_function-call-4142005257738235693': 'file_storage/function-call-4142005257738235693.json'}

exec(code, env_args)

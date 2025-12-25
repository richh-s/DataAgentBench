code = """import json
import pandas as pd

with open(locals()['var_function-call-17865766690995657723'], 'r') as f:
    europe_articles_metadata = json.load(f)

article_ids = [str(article["article_id"]) for article in europe_articles_metadata]

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-17865766690995657723': 'file_storage/function-call-17865766690995657723.json'}

exec(code, env_args)

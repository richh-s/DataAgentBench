code = """import json
import pandas as pd

with open(locals()['var_function-call-13108544427236254645'], 'r') as f:
    europe_articles_metadata = json.load(f)

eu_article_ids = [article['article_id'] for article in europe_articles_metadata]

print("__RESULT__:")
print(json.dumps(eu_article_ids))"""

env_args = {'var_function-call-13108544427236254645': 'file_storage/function-call-13108544427236254645.json'}

exec(code, env_args)

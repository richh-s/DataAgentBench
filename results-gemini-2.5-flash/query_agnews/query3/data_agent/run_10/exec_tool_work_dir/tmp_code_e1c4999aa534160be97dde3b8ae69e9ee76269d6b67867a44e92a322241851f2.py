code = """import json
import pandas as pd

with open(locals()['var_function-call-5043850807955082015'], 'r') as f:
    europe_articles_metadata = json.load(f)

article_ids = [article['article_id'] for article in europe_articles_metadata]
print('__RESULT__:')
print(json.dumps(article_ids))"""

env_args = {'var_function-call-5043850807955082015': 'file_storage/function-call-5043850807955082015.json'}

exec(code, env_args)

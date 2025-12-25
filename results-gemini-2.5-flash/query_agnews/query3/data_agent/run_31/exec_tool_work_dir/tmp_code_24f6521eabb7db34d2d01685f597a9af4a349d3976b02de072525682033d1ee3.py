code = """import pandas as pd
import json

with open(locals()['var_function-call-17178962666327171362'], 'r') as f:
    europe_articles_metadata = json.load(f)

article_ids = [article['article_id'] for article in europe_articles_metadata]
article_ids_str = ', '.join(f'\'''''''{id}''''''''' for id in article_ids)

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-17178962666327171362': 'file_storage/function-call-17178962666327171362.json'}

exec(code, env_args)

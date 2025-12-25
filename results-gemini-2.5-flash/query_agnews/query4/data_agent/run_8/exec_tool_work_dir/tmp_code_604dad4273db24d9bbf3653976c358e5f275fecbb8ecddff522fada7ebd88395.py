code = """import json
import pandas as pd

with open(locals()['var_function-call-5769398487781995713'], 'r') as f:
    article_metadata_2015 = json.load(f)

article_ids_2015 = [article['article_id'] for article in article_metadata_2015]
print("__RESULT__:")
print(json.dumps(article_ids_2015))"""

env_args = {'var_function-call-5769398487781995713': 'file_storage/function-call-5769398487781995713.json'}

exec(code, env_args)

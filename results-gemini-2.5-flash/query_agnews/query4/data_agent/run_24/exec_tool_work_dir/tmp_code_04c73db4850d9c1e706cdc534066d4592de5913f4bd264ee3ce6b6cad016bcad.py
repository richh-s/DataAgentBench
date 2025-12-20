code = """import pandas as pd
import json

with open(locals()["var_function-call-10874147460494608809"], "r") as f:
    articles_2015 = json.load(f)

article_ids_2015 = [article["article_id"] for article in articles_2015]
print("__RESULT__:")
print(json.dumps(article_ids_2015))"""

env_args = {'var_function-call-10874147460494608809': 'file_storage/function-call-10874147460494608809.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# The variable holds the path
path = locals()['var_function-call-7712258569316983833']

with open(path, 'r') as f:
    metadata = json.load(f)

df_meta = pd.DataFrame(metadata)
# The preview showed article_id as strings, but let's see.
article_ids = df_meta['article_id'].tolist()

# Convert to int because Mongo schema says int.
article_ids_int = [int(x) for x in article_ids]

print("__RESULT__:")
print(json.dumps({"count": len(article_ids_int), "ids": article_ids_int}))"""

env_args = {'var_function-call-7712258569316983833': 'file_storage/function-call-7712258569316983833.json'}

exec(code, env_args)

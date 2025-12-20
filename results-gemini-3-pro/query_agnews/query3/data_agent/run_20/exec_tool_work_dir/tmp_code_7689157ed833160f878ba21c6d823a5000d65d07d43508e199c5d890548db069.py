code = """import json
import pandas as pd

# Load the result from the previous query
with open('var_function-call-7712258569316983833.json', 'r') as f:
    metadata = json.load(f)

df_meta = pd.DataFrame(metadata)
article_ids = df_meta['article_id'].tolist()
# Ensure article_ids are integers if they are stored as such in Mongo.
# In the preview they look like "3" (string) or numbers. The database description says article_id is int.
# However, the preview shows "3", "9" etc. as strings if they are quoted. But wait, the preview shows ` "article_id": "3" `.
# The database description says `article_id (int)`.
# Let's handle both or convert. The SQL result came as strings probably? Or the preview formatter did it.
# I'll convert them to int just in case the Mongo schema expects int.

article_ids = [int(x) for x in article_ids]

print("__RESULT__:")
print(json.dumps({"count": len(article_ids), "sample": article_ids[:10]}))"""

env_args = {'var_function-call-7712258569316983833': 'file_storage/function-call-7712258569316983833.json'}

exec(code, env_args)

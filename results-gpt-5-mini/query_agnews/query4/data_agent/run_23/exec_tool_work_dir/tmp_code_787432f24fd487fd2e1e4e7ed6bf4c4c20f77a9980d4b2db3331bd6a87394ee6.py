code = """import json
from pathlib import Path
# var_call_s92epc8s6ZPW1a1CQbTAvYyW is available in storage
data_path = var_call_s92epc8s6ZPW1a1CQbTAvYyW
with open(data_path, 'r') as f:
    records = json.load(f)
# extract article_id as integers
article_ids = [int(r['article_id']) for r in records]
# prepare JSON-serializable output
out = json.dumps(article_ids)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_wgMhGs49Dd75ZYDmKjsPgn1N': ['articles'], 'var_call_hqHuuBktfuXB0n5Pqb01qHF7': ['authors', 'article_metadata'], 'var_call_s92epc8s6ZPW1a1CQbTAvYyW': 'file_storage/call_s92epc8s6ZPW1a1CQbTAvYyW.json'}

exec(code, env_args)

code = """import json
from pathlib import Path
p = Path(var_call_SgR6L4G39ERD0I0uBygA9Iie)
with p.open() as f:
    data = json.load(f)
# extract unique article_ids
article_ids = sorted({int(item['article_id']) for item in data})
result = {'count': len(article_ids), 'sample_ids': article_ids[:20]}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lWz7iHXHJfUOvbbLTESfglyU': ['articles'], 'var_call_SgR6L4G39ERD0I0uBygA9Iie': 'file_storage/call_SgR6L4G39ERD0I0uBygA9Iie.json'}

exec(code, env_args)

code = """import json
from pathlib import Path
p = Path(var_call_kxFllybx6r9YKgy79LKiHcq5)
with p.open('r', encoding='utf-8') as f:
    data = json.load(f)
# data is a list of records with filename and text
titles = []
for rec in data:
    fn = rec.get('filename','')
    if fn.endswith('.txt'):
        titles.append(fn[:-4])
    else:
        titles.append(fn)
# Remove duplicates
titles = list(dict.fromkeys(titles))
import json as _json
print("__RESULT__:")
print(_json.dumps(titles))"""

env_args = {'var_call_kxFllybx6r9YKgy79LKiHcq5': 'file_storage/call_kxFllybx6r9YKgy79LKiHcq5.json'}

exec(code, env_args)

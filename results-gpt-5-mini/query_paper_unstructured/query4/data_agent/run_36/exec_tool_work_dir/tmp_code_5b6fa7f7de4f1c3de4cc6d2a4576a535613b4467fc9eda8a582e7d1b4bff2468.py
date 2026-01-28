code = """import json
from pathlib import Path
# var_call_Kk1CUB2iKCjhNpcEBh5LAyro contains the path to the JSON result from Mongo query
data_path = Path(var_call_Kk1CUB2iKCjhNpcEBh5LAyro)
with data_path.open('r', encoding='utf-8') as f:
    docs = json.load(f)

# Extract titles from filenames by removing .txt
titles = []
for d in docs:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    titles.append(title)

# deduplicate and sort
titles = sorted(list(dict.fromkeys(titles)))

import json
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_Kk1CUB2iKCjhNpcEBh5LAyro': 'file_storage/call_Kk1CUB2iKCjhNpcEBh5LAyro.json'}

exec(code, env_args)

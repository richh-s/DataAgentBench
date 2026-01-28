code = """import json
from pathlib import Path
# Load the JSON file produced by the previous query_db call
p = Path(var_call_qggRiSRpvqlRO8R3PwFvdyvT)
with p.open('r', encoding='utf-8') as f:
    docs = json.load(f)
# Extract titles from filenames (remove .txt extension)
titles = []
for d in docs:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        titles.append(fn[:-4])
    else:
        titles.append(fn)
# Deduplicate and sort
unique_titles = sorted(set(titles))
import json
result = json.dumps(unique_titles)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_qggRiSRpvqlRO8R3PwFvdyvT': 'file_storage/call_qggRiSRpvqlRO8R3PwFvdyvT.json'}

exec(code, env_args)

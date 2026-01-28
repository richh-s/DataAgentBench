code = """import re, json
from pathlib import Path

# Load full Mongo results
path_mongo = Path(var_call_ki9HnaSSuccx1hktaJhdFb4t)
import pandas as pd
mongo_records = pd.read_json(path_mongo)

# Extract year (look for 2016) and ensure domain physical activity via text contains phrase
filtered = []
for _, row in mongo_records.iterrows():
    text = row['text'] or ''
    # crude year detection: must contain 2016
    if '2016' not in text:
        continue
    if 'physical activity' not in text.lower():
        continue
    # title from filename
    filename = row['filename']
    title = re.sub(r"\.txt$", "", filename)
    filtered.append({'title': title})

# unique titles
titles = sorted({r['title'] for r in filtered})

result = json.dumps(titles)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ki9HnaSSuccx1hktaJhdFb4t': 'file_storage/call_ki9HnaSSuccx1hktaJhdFb4t.json', 'var_call_3pitrofj5olkOlatXKZ4BWWV': 'file_storage/call_3pitrofj5olkOlatXKZ4BWWV.json'}

exec(code, env_args)

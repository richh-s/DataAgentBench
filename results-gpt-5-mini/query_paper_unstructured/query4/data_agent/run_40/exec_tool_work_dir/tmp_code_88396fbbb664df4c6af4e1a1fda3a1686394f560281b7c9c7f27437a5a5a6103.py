code = """import json
import re
# Load the Mongo query result from the provided storage file
path = var_call_dZcb7oiZgAHY4QVK8xj1Nin6
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

titles = []
for d in docs:
    text = d.get('text', '')
    filename = d.get('filename', '')
    if not filename:
        continue
    # derive title from filename
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # check for domain and year
    if re.search(r'physical activity', text, re.IGNORECASE) and re.search(r'\b2016\b', text):
        titles.append(title)

# deduplicate and sort
titles = sorted(list(dict.fromkeys(titles)))

import json
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_dZcb7oiZgAHY4QVK8xj1Nin6': 'file_storage/call_dZcb7oiZgAHY4QVK8xj1Nin6.json'}

exec(code, env_args)

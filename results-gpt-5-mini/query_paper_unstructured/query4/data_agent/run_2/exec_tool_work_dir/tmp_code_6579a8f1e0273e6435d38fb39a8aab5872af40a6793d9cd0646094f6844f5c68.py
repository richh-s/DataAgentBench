code = """import json, re
# Load the MongoDB query result stored in var_call_MaQoQdQ19RyHzpTiYGP6O6ye
path = var_call_MaQoQdQ19RyHzpTiYGP6O6ye
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

titles_2016 = []
for d in docs:
    filename = d.get('filename','')
    text = d.get('text','')
    if text and re.search(r'\b2016\b', text):
        title = filename[:-4] if filename.lower().endswith('.txt') else filename
        titles_2016.append(title)

# Deduplicate and sort
titles_2016 = sorted(list(dict.fromkeys(titles_2016)))

import json
print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_call_MaQoQdQ19RyHzpTiYGP6O6ye': 'file_storage/call_MaQoQdQ19RyHzpTiYGP6O6ye.json', 'var_call_OxHAjomhDAL727R6akib7nUG': [], 'var_call_SjDbXdlbTIlTwAv4YaezRHuq': 'file_storage/call_SjDbXdlbTIlTwAv4YaezRHuq.json'}

exec(code, env_args)

code = """import json, re
# Load the 2016 docs result
path = var_call_SjDbXdlbTIlTwAv4YaezRHuq
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Filter docs that mention 'physical activity' (case-insensitive) in their text
titles = []
for d in docs:
    text = d.get('text','')
    if text and re.search(r'physical activity', text, re.I):
        filename = d.get('filename','')
        title = filename[:-4] if filename.lower().endswith('.txt') else filename
        titles.append(title)

# Deduplicate and sort
titles = sorted(list(dict.fromkeys(titles)))

import json
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_MaQoQdQ19RyHzpTiYGP6O6ye': 'file_storage/call_MaQoQdQ19RyHzpTiYGP6O6ye.json', 'var_call_OxHAjomhDAL727R6akib7nUG': [], 'var_call_SjDbXdlbTIlTwAv4YaezRHuq': 'file_storage/call_SjDbXdlbTIlTwAv4YaezRHuq.json', 'var_call_fVXhCX2dTWyXDOejIG8uZim5': [], 'var_call_ErSdE1tZujPBsbnNtv5ajzjU': 'file_storage/call_ErSdE1tZujPBsbnNtv5ajzjU.json'}

exec(code, env_args)

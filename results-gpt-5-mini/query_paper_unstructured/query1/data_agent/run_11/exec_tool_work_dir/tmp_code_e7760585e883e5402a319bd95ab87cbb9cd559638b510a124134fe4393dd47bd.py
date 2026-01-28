code = """import json
# Load the query_db result stored in var_call_d33OhPPShnOm3wrRSC0Gr9N9
path = var_call_d33OhPPShnOm3wrRSC0Gr9N9
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract titles from filenames (remove .txt extension)
titles = []
for doc in data:
    fn = doc.get('filename')
    if fn and fn.lower().endswith('.txt'):
        titles.append(fn[:-4])
    elif fn:
        titles.append(fn)

# Deduplicate and sort for stable ordering
unique_titles = sorted(list(set(titles)))

import json as _json
print("__RESULT__:")
print(_json.dumps(unique_titles))"""

env_args = {'var_call_hkMip2AYjGLuQ0ED0Epixc21': ['paper_docs'], 'var_call_d33OhPPShnOm3wrRSC0Gr9N9': 'file_storage/call_d33OhPPShnOm3wrRSC0Gr9N9.json'}

exec(code, env_args)

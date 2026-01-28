code = """import json, re
path = var_call_VUXvOspLetLt5Con2KvfAtOt
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

selected_titles = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','') or ''
    # domain already matched by Mongo query, but double-check
    if not re.search(r'physical activity', text, re.I):
        continue
    # check for publication year 2016 anywhere
    if re.search(r'\b2016\b', text):
        selected_titles.append(title)

# dedupe and sort
selected_titles = sorted(list(dict.fromkeys(selected_titles)))
import json as _json
print("__RESULT__:")
print(_json.dumps(selected_titles))"""

env_args = {'var_call_IGldEbXgZoelD1zKxMwMtdEX': ['paper_docs'], 'var_call_XACNxD8OT8SN9vqerPeW7TT0': ['Citations', 'sqlite_sequence'], 'var_call_VUXvOspLetLt5Con2KvfAtOt': 'file_storage/call_VUXvOspLetLt5Con2KvfAtOt.json', 'var_call_fqeblluy4MCxoD3QTv0TmFbA': [], 'var_call_MNhg9l6BcC75PtwFc5e5j8E2': 'file_storage/call_MNhg9l6BcC75PtwFc5e5j8E2.json'}

exec(code, env_args)

code = """import json
# var_call_rTQp7MxVakpeqHDYVds2V0FT is provided by previous query_db call and contains the file path to the JSON result
fp = var_call_rTQp7MxVakpeqHDYVds2V0FT
with open(fp, 'r', encoding='utf-8') as f:
    records = json.load(f)

titles = []
for r in records:
    fn = r.get('filename')
    if not fn:
        continue
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    titles.append(title)

# deduplicate and sort
unique_titles = sorted(list(dict.fromkeys(titles)))
import json as _json
out = _json.dumps(unique_titles)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rTQp7MxVakpeqHDYVds2V0FT': 'file_storage/call_rTQp7MxVakpeqHDYVds2V0FT.json'}

exec(code, env_args)

code = """import json
# var_call_FpTMMwOGOy6ZNUAgkfnMqrT5 is provided by previous query_db call and contains the JSON file path
path = var_call_FpTMMwOGOy6ZNUAgkfnMqrT5
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# Extract filenames and convert to titles (remove .txt)
titles = []
for r in records:
    fn = r.get('filename')
    if not fn:
        continue
    title = fn
    if title.lower().endswith('.txt'):
        title = title[:-4]
    titles.append(title)
# deduplicate
unique_titles = sorted(list(dict.fromkeys(titles)))
# produce JSON string
out = json.dumps(unique_titles)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_FpTMMwOGOy6ZNUAgkfnMqrT5': 'file_storage/call_FpTMMwOGOy6ZNUAgkfnMqrT5.json'}

exec(code, env_args)

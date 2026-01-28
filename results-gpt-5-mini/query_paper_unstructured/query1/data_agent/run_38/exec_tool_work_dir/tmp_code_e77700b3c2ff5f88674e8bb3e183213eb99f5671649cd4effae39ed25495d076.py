code = """import json
# var_call_GQH5IuhVIHmcCdXyM6xXuSlx contains the file path to the Mongo query result JSON
p = var_call_GQH5IuhVIHmcCdXyM6xXuSlx
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

titles = []
for d in data:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    titles.append(title)

# deduplicate while preserving order
seen = set()
unique_titles = []
for t in titles:
    if t not in seen:
        seen.add(t)
        unique_titles.append(t)

# Escape single quotes for SQL
escaped = [t.replace("'", "''") for t in unique_titles]
# Build SQL IN clause
if escaped:
    in_clause = "(" + ",".join("'{}'".format(t) for t in escaped) + ")"
else:
    in_clause = "()"

output = {"count_titles": len(unique_titles), "in_clause": in_clause, "titles_sample": unique_titles[:20]}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_3bNQTcXv6jBC8JvR5KVu7vYW': ['paper_docs'], 'var_call_GQH5IuhVIHmcCdXyM6xXuSlx': 'file_storage/call_GQH5IuhVIHmcCdXyM6xXuSlx.json'}

exec(code, env_args)

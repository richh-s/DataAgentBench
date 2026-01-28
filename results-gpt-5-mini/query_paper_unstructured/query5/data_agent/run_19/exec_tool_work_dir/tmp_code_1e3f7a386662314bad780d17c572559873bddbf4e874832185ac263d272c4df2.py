code = """import json
# var_call_ZIHcDwCJatnW8gkvZPHj3AVM is provided by previous query_db call and contains the path to the full JSON result
with open(var_call_ZIHcDwCJatnW8gkvZPHj3AVM, 'r') as f:
    data = json.load(f)

titles = []
for rec in data:
    fn = rec.get('filename','')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    if title:
        titles.append(title)
# deduplicate and sort
seen = set()
uniq_titles = []
for t in titles:
    if t not in seen:
        seen.add(t)
        uniq_titles.append(t)

# build SQL IN clause safely by escaping single quotes
def sql_quote(s):
    return "'" + s.replace("'", "''") + "'"

in_clause = "(" + ",".join(sql_quote(t) for t in uniq_titles) + ")"

out = {"titles": uniq_titles, "in_clause": in_clause}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ZIHcDwCJatnW8gkvZPHj3AVM': 'file_storage/call_ZIHcDwCJatnW8gkvZPHj3AVM.json'}

exec(code, env_args)

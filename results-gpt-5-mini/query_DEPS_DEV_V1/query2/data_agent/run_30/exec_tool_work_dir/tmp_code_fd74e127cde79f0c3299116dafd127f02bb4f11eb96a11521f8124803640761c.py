code = """import json
# var_call_ahEJxFjLRUBjBFLTYlcUqhv9 is a file path to JSON
with open(var_call_ahEJxFjLRUBjBFLTYlcUqhv9, 'r', encoding='utf-8') as f:
    data = json.load(f)
# Extract unique (Name, Version)
pairs = [(r['Name'], r['Version']) for r in data]
# deduplicate
seen = set()
unique = []
for n,v in pairs:
    if (n,v) not in seen:
        seen.add((n,v))
        unique.append({'Name': n, 'Version': v})
# Output as JSON string
result = json.dumps(unique)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_ahEJxFjLRUBjBFLTYlcUqhv9': 'file_storage/call_ahEJxFjLRUBjBFLTYlcUqhv9.json'}

exec(code, env_args)

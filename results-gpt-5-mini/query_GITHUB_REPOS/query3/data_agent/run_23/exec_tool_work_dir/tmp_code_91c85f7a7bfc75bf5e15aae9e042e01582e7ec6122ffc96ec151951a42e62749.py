code = """import json
path = var_call_b5lYIPqmwcy0Rnf7st2Cf8Ed
with open(path, 'r') as f:
    chunks = json.load(f)
queries = []
for chunk in chunks:
    if not chunk:
        continue
    # build IN list
    in_list = ",".join(["'{}'".format(s.replace("'","''")) for s in chunk])
    q = (
        "SELECT COUNT(*) AS cnt FROM commits "
        "WHERE repo_name IN (" + in_list + ") "
        "AND message IS NOT NULL "
        "AND message <> '' "
        "AND length(message) < 1000 "
        "AND lower(message) NOT LIKE 'merge%' "
        "AND lower(message) NOT LIKE 'update%' "
        "AND lower(message) NOT LIKE 'test%';"
    )
    queries.append(q)
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_HDcK5iM8SUpW9eZ5veiEaqeT': 'file_storage/call_HDcK5iM8SUpW9eZ5veiEaqeT.json', 'var_call_8OQSJvogJ0rD1HbLbKrfTgci': 'file_storage/call_8OQSJvogJ0rD1HbLbKrfTgci.json', 'var_call_b5lYIPqmwcy0Rnf7st2Cf8Ed': 'file_storage/call_b5lYIPqmwcy0Rnf7st2Cf8Ed.json'}

exec(code, env_args)

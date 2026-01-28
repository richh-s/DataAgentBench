code = """import json

path = var_call_XgSDe5Ce6OMsj82l8GW6iy1y
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

def sql_quote(s):
    return "'" + s.replace("'", "''") + "'"

if not repo_names:
    out = json.dumps({"repo_count": 0, "chunks": []})
else:
    chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
    queries = []
    for ch in chunks:
        in_list = ','.join(sql_quote(x) for x in ch)
        q = (
            "SELECT COUNT(*) AS cnt FROM commits "
            f"WHERE repo_name IN ({in_list}) "
            "AND message IS NOT NULL "
            "AND length(message) < 1000 "
            "AND lower(message) NOT LIKE 'merge%' "
            "AND lower(message) NOT LIKE 'update%' "
            "AND lower(message) NOT LIKE 'test%';"
        )
        queries.append(q)
    out = json.dumps({"repo_count": len(repo_names), "chunks": queries})

print('__RESULT__:')
print(out)"""

env_args = {'var_call_XgSDe5Ce6OMsj82l8GW6iy1y': 'file_storage/call_XgSDe5Ce6OMsj82l8GW6iy1y.json', 'var_call_ErqNY2aK18MkyRAfvm5kGJgR': [{'cnt': '15016'}]}

exec(code, env_args)

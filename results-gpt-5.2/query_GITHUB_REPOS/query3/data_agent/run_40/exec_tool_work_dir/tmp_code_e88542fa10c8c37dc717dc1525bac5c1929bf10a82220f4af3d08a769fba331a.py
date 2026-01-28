code = """import json

path = var_call_6ghUCeTpzkBHxS6cHTSx5sFH
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

def sql_quote(s):
    return "'" + s.replace("'","''") + "'"

chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ",".join(sql_quote(x) for x in chunk)
    q = (
        "SELECT COUNT(*) AS cnt FROM commits "
        f"WHERE repo_name IN ({in_list}) "
        "AND message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND lower(message) NOT LIKE 'merge%' "
        "AND lower(message) NOT LIKE 'update%' "
        "AND lower(message) NOT LIKE 'test%';"
    )
    chunks.append(q)

print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_names), 'queries': chunks}))"""

env_args = {'var_call_6ghUCeTpzkBHxS6cHTSx5sFH': 'file_storage/call_6ghUCeTpzkBHxS6cHTSx5sFH.json', 'var_call_4iFh2crZvLUOEQwJDlI9kBiX': [{'commit_message_count': '0'}]}

exec(code, env_args)

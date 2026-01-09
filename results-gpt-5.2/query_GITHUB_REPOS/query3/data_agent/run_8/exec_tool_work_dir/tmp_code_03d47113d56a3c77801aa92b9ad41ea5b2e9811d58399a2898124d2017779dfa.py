code = """import json
path = var_call_36Id3lYz6wUmBCcqmMy1OaLT
with open(path,'r',encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# build a single VALUES list query in chunks to avoid too-long statement
chunks = [repo_names[i:i+20000] for i in range(0,len(repo_names),20000)]
cts = []
for ch in chunks:
    values = ','.join(["('"+s.replace("'","''")+"')" for s in ch])
    q = (
        "WITH sel(repo_name) AS (VALUES " + values + ") "
        "SELECT COUNT(*) AS c FROM commits "
        "WHERE message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND lower(message) NOT LIKE 'merge%' "
        "AND lower(message) NOT LIKE 'update%' "
        "AND lower(message) NOT LIKE 'test%' "
        "AND repo_name IN (SELECT repo_name FROM sel);"
    )
    cts.append(q)

print('__RESULT__:')
print(json.dumps({'queries': cts, 'chunk_count': len(cts), 'repo_count': len(repo_names)}))"""

env_args = {'var_call_36Id3lYz6wUmBCcqmMy1OaLT': 'file_storage/call_36Id3lYz6wUmBCcqmMy1OaLT.json', 'var_call_la0n574krMowWjMHKbq4aBFv': 'file_storage/call_la0n574krMowWjMHKbq4aBFv.json', 'var_call_UoCIEVi3rO3q5V3hcCSZ8ZvH': [{'1': '1'}]}

exec(code, env_args)

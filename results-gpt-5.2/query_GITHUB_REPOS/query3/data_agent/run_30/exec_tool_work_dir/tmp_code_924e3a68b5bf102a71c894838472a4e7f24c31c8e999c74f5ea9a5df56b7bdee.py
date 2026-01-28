code = """import json
repo_res = var_call_TGu244PIHit9FXE0sGs30iDh
if isinstance(repo_res,str):
    with open(repo_res,'r') as f: repo_res=json.load(f)
repos=[r['repo_name'] for r in repo_res]
# check intersection with commits table for first 200
sample=repos[:200]
in_list=','.join(["'"+x.replace("'","''")+"'" for x in sample])
print('__RESULT__:')
print(json.dumps({'in_list_len': len(sample), 'in_list_preview': in_list[:200]}))"""

env_args = {'var_call_TGu244PIHit9FXE0sGs30iDh': 'file_storage/call_TGu244PIHit9FXE0sGs30iDh.json', 'var_call_p7JnMWQOQCwiG105SU70LgxQ': [{'1': '1'}], 'var_call_S8iTRUB8rKBcAOUS9yTMM59o': 'file_storage/call_S8iTRUB8rKBcAOUS9yTMM59o.json', 'var_call_hSxG58jo4321bV62xIw8Kuir': {'n_queries': 230, 'first_query': "SELECT COUNT(*) AS cnt FROM commits WHERE message IS NOT NULL AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%' "}, 'var_call_wp8301mOmI2CGfiAtiyg139X': [{'cnt': '0'}]}

exec(code, env_args)

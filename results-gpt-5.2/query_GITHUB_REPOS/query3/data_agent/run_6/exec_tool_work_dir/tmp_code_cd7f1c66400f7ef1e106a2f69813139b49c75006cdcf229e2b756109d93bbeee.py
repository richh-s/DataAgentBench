code = """import json
path = var_call_nGLywJAQH49e5D4vwSR60bUF
with open(path, 'r', encoding='utf-8') as f:
    queries = json.load(f)['queries']
union = ' UNION ALL '.join([q.replace(';','') for q in queries])
final_q = f"SELECT SUM(cnt) AS commit_message_count FROM ({union}) t;"
print('__RESULT__:')
print(json.dumps({'final_query': final_q}))"""

env_args = {'var_call_cBY07VVhdToJgICFJgfLQOnv': 'file_storage/call_cBY07VVhdToJgICFJgfLQOnv.json', 'var_call_GiBXcbU1ci2vywFpdconRX7P': [{'commit_message_count': '15016'}], 'var_call_nGLywJAQH49e5D4vwSR60bUF': 'file_storage/call_nGLywJAQH49e5D4vwSR60bUF.json', 'var_call_MU64o5xSlSwu2jcGeH47rOjx': {'n_queries': 230, 'first_query': "SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ('juliandunn/rackspacecloud','rupakg/lorry','Nordstrom/al_agents','fuellab/bootstrap','brint/rax-wordpress-cookbook','rarenerd/train','wallyqs/ru"}}

exec(code, env_args)

code = """import json
p = var_call_w084PNVwsgr7OJGySoIsAbrX
with open(p,'r',encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]
repo_names_escaped = [rn.replace("'","''") for rn in repo_names]
clauses=[]
chunk_size=400
for i in range(0,len(repo_names_escaped),chunk_size):
    chunk=repo_names_escaped[i:i+chunk_size]
    in_list=",".join(["'"+x+"'" for x in chunk])
    clauses.append("repo_name IN ("+in_list+")")
where_repo=" OR ".join(["("+c+")" for c in clauses])
q="SELECT COUNT(*) AS commit_message_count FROM commits WHERE message IS NOT NULL AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%' AND ("+where_repo+");"
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_call_w084PNVwsgr7OJGySoIsAbrX': 'file_storage/call_w084PNVwsgr7OJGySoIsAbrX.json', 'var_call_Q90Pp5czommQNWVuEpKqyo9Z': 'file_storage/call_Q90Pp5czommQNWVuEpKqyo9Z.json', 'var_call_ty3hOsLNjgrqUMOeEr18Pd0G': []}

exec(code, env_args)

code = """import json

citation_file = var_functions.query_db:0
with open(citation_file, 'r') as f:
    citations_2018 = json.load(f)

print('__RESULT__:')
print(json.dumps({"count": len(citations_2018), "sample": citations_2018[:3]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

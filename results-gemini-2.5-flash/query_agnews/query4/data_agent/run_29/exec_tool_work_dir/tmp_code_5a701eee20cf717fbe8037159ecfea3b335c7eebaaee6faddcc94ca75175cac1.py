code = """import json

with open(locals()['var_function-call-17249384934174781588'], 'r') as f:
    article_ids_2015_str = json.load(f)

article_ids_2015_int = [int(article_id) for article_id in article_ids_2015_str]

print("__RESULT__:")
print(json.dumps(article_ids_2015_int))"""

env_args = {'var_function-call-106986608686761931': 'file_storage/function-call-106986608686761931.json', 'var_function-call-10777639638167933225': 'file_storage/function-call-10777639638167933225.json', 'var_function-call-17249384934174781588': 'file_storage/function-call-17249384934174781588.json'}

exec(code, env_args)

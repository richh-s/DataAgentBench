code = """import json

with open(locals()['var_function-call-121859605526448438'], 'r') as f:
    articles_2015 = json.load(f)

ids = [int(a['article_id']) for a in articles_2015]
batch1 = ids[:2000]
print("__RESULT__:")
print(json.dumps(batch1))"""

env_args = {'var_function-call-121859605526448438': 'file_storage/function-call-121859605526448438.json', 'var_function-call-951208037007644572': 'file_storage/function-call-951208037007644572.json', 'var_function-call-8352185799025476041': [{'count(*)': '127600'}], 'var_function-call-6206586464072558012': 47788, 'var_function-call-12195274356503434995': {'min': 13, 'max': 127570}}

exec(code, env_args)

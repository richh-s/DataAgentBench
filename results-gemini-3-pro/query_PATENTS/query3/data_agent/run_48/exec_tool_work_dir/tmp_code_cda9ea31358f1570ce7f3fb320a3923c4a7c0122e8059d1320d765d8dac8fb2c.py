code = """import json

with open(locals()['var_function-call-17903063529508047535'], 'r') as f:
    data = json.load(f)
    cpc_example = ""
    if data and 'cpc' in data[0]:
        cpc_example = data[0]['cpc']

print("__RESULT__:")
print(json.dumps(cpc_example))"""

env_args = {'var_function-call-16690190514013585570': 'file_storage/function-call-16690190514013585570.json', 'var_function-call-11770702646543958360': 'file_storage/function-call-11770702646543958360.json', 'var_function-call-17903063529508047535': 'file_storage/function-call-17903063529508047535.json'}

exec(code, env_args)

code = """import json

# Load first few chars to inspect cpc structure
with open(locals()['var_function-call-17903063529508047535'], 'r') as f:
    data = json.load(f)
    if data and 'cpc' in data[0]:
        print(data[0]['cpc'])"""

env_args = {'var_function-call-16690190514013585570': 'file_storage/function-call-16690190514013585570.json', 'var_function-call-11770702646543958360': 'file_storage/function-call-11770702646543958360.json', 'var_function-call-17903063529508047535': 'file_storage/function-call-17903063529508047535.json'}

exec(code, env_args)

code = """import json
path = locals()['var_function-call-7175199923807763808']
with open(path, 'r') as f:
    d = json.load(f)
s = d[0]['Symbol']
q = "SELECT '{0}' FROM \"{0}\"".format(s)
print("__RESULT__:")
print(json.dumps(q))"""

env_args = {'var_function-call-8419409271616832498': 'file_storage/function-call-8419409271616832498.json', 'var_function-call-4151914565756568448': 'file_storage/function-call-4151914565756568448.json', 'var_function-call-7175199923807763808': 'file_storage/function-call-7175199923807763808.json', 'var_function-call-1526171119472406754': 234, 'var_function-call-761790631451459462': [{'Date': '1987-09-30'}], 'var_function-call-13952986258041756676': 'file_storage/function-call-13952986258041756676.json', 'var_function-call-10146214134899326186': 'file_storage/function-call-10146214134899326186.json', 'var_function-call-14865291104312683632': 'test', 'var_function-call-18363194978560378977': 234, 'var_function-call-16116604006856398769': "SELECT 'AEFC' FROM  + s + "}

exec(code, env_args)

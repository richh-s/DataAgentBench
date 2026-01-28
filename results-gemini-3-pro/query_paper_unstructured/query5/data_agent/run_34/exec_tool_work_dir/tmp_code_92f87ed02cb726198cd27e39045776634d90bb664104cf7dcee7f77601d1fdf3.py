code = """import json

file_path = locals()['var_function-call-4971371690399904807']
with open(file_path, 'r') as f:
    citations = json.load(f)

filenames = [r['title'] + ".txt" for r in citations]
mid = len(filenames) // 2
part1 = filenames[:mid]

print("__RESULT__:")
print(json.dumps(part1))"""

env_args = {'var_function-call-4971371690399904807': 'file_storage/function-call-4971371690399904807.json', 'var_function-call-3762194081429222261': 'Sundroid: Solar Radiation Awareness with Smartphones', 'var_function-call-2236088385608498934': 'file_storage/function-call-2236088385608498934.json', 'var_function-call-10711844707141309926': 188, 'var_function-call-15307267055768926188': 'file_storage/function-call-15307267055768926188.json', 'var_function-call-10692757650084218033': 4, 'var_function-call-3707955499525086918': 'file_storage/function-call-3707955499525086918.json'}

exec(code, env_args)

code = """import json

# Get filenames
k1 = 'var_function-call-17042838615002828598'
k2 = 'var_function-call-1654927262755686554'
f1 = locals()[k1]
f2 = locals()[k2]

with open(f1, 'r') as f:
    d1 = json.load(f)
with open(f2, 'r') as f:
    d2 = json.load(f)

print("__RESULT__:")
print(json.dumps("OK"))"""

env_args = {'var_function-call-17042838615002828598': 'file_storage/function-call-17042838615002828598.json', 'var_function-call-1654927262755686554': 'file_storage/function-call-1654927262755686554.json', 'var_function-call-8866745000760518391': 'file_storage/function-call-8866745000760518391.json', 'var_function-call-802954950120546445': 1435}

exec(code, env_args)

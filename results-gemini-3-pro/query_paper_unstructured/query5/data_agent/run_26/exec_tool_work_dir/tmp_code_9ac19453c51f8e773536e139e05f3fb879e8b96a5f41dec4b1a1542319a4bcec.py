code = """import json

# Load docs
with open(locals()['var_function-call-5489290469044726866'], 'r') as f:
    docs = json.load(f)

# Print first 10 filenames from docs
print("First 10 filenames in docs:")
for d in docs[:10]:
    print(d['filename'])

# Check if "Sundroid: Solar Radiation Awareness with Smartphones.txt" is in docs
target = "Sundroid: Solar Radiation Awareness with Smartphones.txt"
found = False
for d in docs:
    if d['filename'] == target:
        found = True
        break
print(f"'{target}' found: {found}")

# Also check if any filename contains "Sundroid"
for d in docs:
    if "Sundroid" in d['filename']:
        print(f"Found match: {d['filename']}")

print("__RESULT__:")
print(json.dumps(True))"""

env_args = {'var_function-call-2890407691846929350': ['Citations', 'sqlite_sequence'], 'var_function-call-2890407691846929759': 'file_storage/function-call-2890407691846929759.json', 'var_function-call-1018587870991830331': 'file_storage/function-call-1018587870991830331.json', 'var_function-call-13985119328028857859': 'file_storage/function-call-13985119328028857859.json', 'var_function-call-6633830581226945890': 'file_storage/function-call-6633830581226945890.json', 'var_function-call-5489290469044726866': 'file_storage/function-call-5489290469044726866.json', 'var_function-call-15377808340814584921': {'count_filenames': 188}, 'var_function-call-2561381756646521997': 'file_storage/function-call-2561381756646521997.json'}

exec(code, env_args)

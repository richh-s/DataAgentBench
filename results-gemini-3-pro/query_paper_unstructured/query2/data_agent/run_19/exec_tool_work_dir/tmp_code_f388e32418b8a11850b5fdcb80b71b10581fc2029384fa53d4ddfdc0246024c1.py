code = """import json

# Load citations result
with open(locals()['var_function-call-10411215990845860402'], 'r') as f:
    citations = json.load(f)

# Extract titles and create filenames
filenames = [c['title'] + ".txt" for c in citations]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-10411215990845860402': 'file_storage/function-call-10411215990845860402.json', 'var_function-call-10411215990845858223': 'file_storage/function-call-10411215990845858223.json', 'var_function-call-17822327619243240138': [{'count(*)': '158'}], 'var_function-call-17822327619243238473': 'file_storage/function-call-17822327619243238473.json', 'var_function-call-8942426573761665136': 'file_storage/function-call-8942426573761665136.json'}

exec(code, env_args)

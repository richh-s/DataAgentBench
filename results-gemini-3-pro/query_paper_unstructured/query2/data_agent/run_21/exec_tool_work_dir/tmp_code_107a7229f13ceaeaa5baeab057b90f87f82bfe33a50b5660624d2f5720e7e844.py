code = """import json

# Load citations result
with open(locals()['var_function-call-15503541887771276820'], 'r') as f:
    citations = json.load(f)

# Extract titles and map to citation count
# The problem asks for average citation count for papers *published by ACM* cited in 2018.
# We have papers cited in 2018 in 'citations'.
# We need to filter these by source=ACM.

titles = [c['title'] for c in citations]
filenames = [t + ".txt" for t in titles]

print(f"__RESULT__:\n{json.dumps(filenames)}")"""

env_args = {'var_function-call-15503541887771276820': 'file_storage/function-call-15503541887771276820.json'}

exec(code, env_args)

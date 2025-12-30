code = """import json

# Load civic docs
with open(locals()['var_function-call-13241760497320549299'], 'r') as f:
    civic_docs = json.load(f)

# Load funding
with open(locals()['var_function-call-8006204082577017619'], 'r') as f:
    funding = json.load(f)

# Get project names
project_names = [r['Project_Name'] for r in funding]

text = civic_docs[0]['text']

# Find snippets with "Spring 2022"
snippets = []
lines = text.split('\n')
for i, line in enumerate(lines):
    if "Spring 2022" in line or "Spring, 2022" in line:
        snippets.append(line)
        # Context
        # snippets.append(lines[i-1] + " || " + line + " || " + lines[i+1])

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-14343582955729451491': 'file_storage/function-call-14343582955729451491.json', 'var_function-call-8006204082577017619': 'file_storage/function-call-8006204082577017619.json', 'var_function-call-13241760497320549299': 'file_storage/function-call-13241760497320549299.json'}

exec(code, env_args)

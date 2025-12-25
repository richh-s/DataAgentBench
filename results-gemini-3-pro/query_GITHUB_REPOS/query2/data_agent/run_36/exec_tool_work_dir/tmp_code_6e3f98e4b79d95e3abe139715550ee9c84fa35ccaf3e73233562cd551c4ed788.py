code = """import json
import re

file_path = locals()['var_function-call-2573461402379613798']
with open(file_path, 'r') as f:
    data = json.load(f)

max_count = -1
max_id = None
max_desc = ""

pattern = re.compile(r'(?:duplicated|appearing|seen|repeated|copied|appears) (\d+) times')

for item in data:
    desc = item.get('repo_data_description', '')
    match = pattern.search(desc)
    if match:
        count = int(match.group(1))
        if count > max_count:
            max_count = count
            max_id = item['id']
            max_desc = desc

print("__RESULT__:")
print(json.dumps({"max_id": max_id, "max_count": max_count, "description": max_desc}))"""

env_args = {'var_function-call-17567642971942000785': ['commits', 'contents', 'files'], 'var_function-call-13361138901660454113': ['languages', 'repos', 'licenses'], 'var_function-call-13259296133069852295': 'file_storage/function-call-13259296133069852295.json', 'var_function-call-15549765763826830593': [{'count_star()': '105'}], 'var_function-call-2573461402379613798': 'file_storage/function-call-2573461402379613798.json'}

exec(code, env_args)

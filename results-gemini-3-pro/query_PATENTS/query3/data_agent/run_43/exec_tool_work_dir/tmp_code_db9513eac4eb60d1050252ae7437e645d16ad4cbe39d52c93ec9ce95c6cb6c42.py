code = """import json
import re

file_path = locals()['var_function-call-8863344319814314671']
with open(file_path, 'r') as f:
    data = json.load(f)

uc_pub_nums = set()
regex = r"(?:publication|pub\.?)\s+(?:number|no\.?)\s+([A-Z]{2}-[\w\d]+-[A-Z\d]+)"

for record in data:
    info = record.get('Patents_info', '')
    match = re.search(regex, info, re.IGNORECASE)
    if match:
        uc_pub_nums.add(match.group(1))

print("__RESULT__:")
print(json.dumps(list(uc_pub_nums)))"""

env_args = {'var_function-call-1646624266495231220': 'file_storage/function-call-1646624266495231220.json', 'var_function-call-1337059842938340613': [{'COUNT(*)': '277813'}], 'var_function-call-8863344319814314671': 'file_storage/function-call-8863344319814314671.json'}

exec(code, env_args)

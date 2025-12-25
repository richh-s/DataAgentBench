code = """import json
import re

# Load the result from the previous query
file_path = locals()['var_function-call-8863344319814314671']
with open(file_path, 'r') as f:
    data = json.load(f)

uc_pub_nums = set()
# Regex to find publication number
# Patterns seen:
# "publication number US-11081687-B2"
# "pub. number US-2022074631-A1"
# "publication no. US-..."
# "pub. number ..."
# generic pattern for pub num: [A-Z]{2}-[\w\d]+-[A-Z\d]+
regex = r"(?:publication|pub\.?)\s+(?:number|no\.?)\s+([A-Z]{2}-[\w\d]+-[A-Z\d]+)"

for record in data:
    info = record.get('Patents_info', '')
    match = re.search(regex, info, re.IGNORECASE)
    if match:
        uc_pub_nums.add(match.group(1))

print("__RESULT__:")
print(len(uc_pub_nums))
print(list(uc_pub_nums)[:10]) # Print first 10 for verification"""

env_args = {'var_function-call-1646624266495231220': 'file_storage/function-call-1646624266495231220.json', 'var_function-call-1337059842938340613': [{'COUNT(*)': '277813'}], 'var_function-call-8863344319814314671': 'file_storage/function-call-8863344319814314671.json'}

exec(code, env_args)

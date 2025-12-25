code = """import json
import re

# Load the result from the file provided in the previous step
# The key was var_function-call-3777495731154721435
with open(locals()['var_function-call-3777495731154721435'], 'r') as f:
    data = json.load(f)

uc_pub_nums = []
# Regex to capture the publication number at the end of the sentence or clause
# Patterns observed: 
# "has pub. number <ID>."
# "with pub. number <ID>."
# "has publication number <ID>."
# "with publication no. <ID>."
# "has publication no. <ID>."
# "with publication number <ID>."

pattern = re.compile(r"(?:publication|pub\.?)\s+(?:number|no\.?)\s+([A-Z]{2}-[\w\d-]+)(?:[.\s]|$)")

for row in data:
    info = row.get('Patents_info', '')
    match = pattern.search(info)
    if match:
        uc_pub_nums.append(match.group(1))

# deduplicate
uc_pub_nums = list(set(uc_pub_nums))

print("__RESULT__:")
print(json.dumps(uc_pub_nums))"""

env_args = {'var_function-call-12063958642635742957': 'file_storage/function-call-12063958642635742957.json', 'var_function-call-18128361621768259394': 'file_storage/function-call-18128361621768259394.json', 'var_function-call-3777495731154721435': 'file_storage/function-call-3777495731154721435.json'}

exec(code, env_args)

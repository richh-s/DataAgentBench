code = """import json
import re

key = 'var_function-call-1072305036396177702'
path = locals()[key]
with open(path, 'r') as f:
    uc_patents_data = json.load(f)

uc_pub_numbers = set()
for row in uc_patents_data:
    info = row['Patents_info']
    match = re.search(r'(?:publication|pub\.?)\s+(?:number|no\.)\s+([A-Za-z0-9-]+)', info, re.IGNORECASE)
    if match:
        uc_pub_numbers.add(match.group(1))

print("__RESULT__:")
print(json.dumps(list(uc_pub_numbers)))"""

env_args = {'var_function-call-2317850229295354016': 'file_storage/function-call-2317850229295354016.json', 'var_function-call-1072305036396177702': 'file_storage/function-call-1072305036396177702.json'}

exec(code, env_args)

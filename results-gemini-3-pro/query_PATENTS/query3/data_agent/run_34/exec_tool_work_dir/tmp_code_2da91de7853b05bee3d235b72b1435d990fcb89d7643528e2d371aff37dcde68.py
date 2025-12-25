code = """import json
import re

# Load the previous result containing UNIV CALIFORNIA patents
# Use the exact key string with hyphens
key = 'var_function-call-7767822148411352002'
with open(locals()[key], 'r') as f:
    uc_records = json.load(f)

uc_pub_numbers = set()
# Regex to extract publication number. 
pattern = re.compile(r"(?:publication number|pub\. number|publication no\.)\s+([A-Z0-9\-]+)")

for rec in uc_records:
    info = rec['Patents_info']
    match = pattern.search(info)
    if match:
        p_num = match.group(1).rstrip('.')
        uc_pub_numbers.add(p_num)

print("__RESULT__:")
print(json.dumps(list(uc_pub_numbers)))"""

env_args = {'var_function-call-4904949375881535909': ['publicationinfo'], 'var_function-call-5806259679188140388': 'file_storage/function-call-5806259679188140388.json', 'var_function-call-14332834778126203785': [{'COUNT(*)': '277813'}], 'var_function-call-7767822148411352002': 'file_storage/function-call-7767822148411352002.json', 'var_function-call-12562776810017493768': [{'COUNT(*)': '169'}]}

exec(code, env_args)

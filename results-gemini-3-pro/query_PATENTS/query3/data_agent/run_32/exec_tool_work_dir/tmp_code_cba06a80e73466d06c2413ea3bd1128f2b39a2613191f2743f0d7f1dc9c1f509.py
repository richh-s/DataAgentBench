code = """import json
import re

file_path = locals()['var_function-call-5726066764159210267']
with open(file_path, 'r') as f:
    univ_cal_data = json.load(f)

univ_cal_pub_nums = set()
# patterns
p1 = re.compile(r"publication number\s+([A-Z]{2}-[0-9A-Z-]+)")
p2 = re.compile(r"pub\. number\s+([A-Z]{2}-[0-9A-Z-]+)")
p3 = re.compile(r"publication no\.\s+([A-Z]{2}-[0-9A-Z-]+)")

# The examples showed: "US-2022074631-A1." -> The regex should handle the trailing dot or space.
# Revised regex to be more robust.
p_general = re.compile(r"(?:publication|pub\.)\s*(?:number|no\.|no)\s*([A-Z]{2}-[0-9]+-[A-Z0-9]+)")

for entry in univ_cal_data:
    text = entry.get('Patents_info', '')
    match = p_general.search(text)
    if match:
        univ_cal_pub_nums.add(match.group(1))

result = list(univ_cal_pub_nums)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5447102030661239686': 'file_storage/function-call-5447102030661239686.json', 'var_function-call-5726066764159210267': 'file_storage/function-call-5726066764159210267.json'}

exec(code, env_args)

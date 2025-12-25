code = """import json
import re

# Load the result from the previous query
file_path = locals()['var_function-call-3051103024558862659']
with open(file_path, 'r') as f:
    data = json.load(f)

# Extract publication numbers
univ_cal_pub_nums = set()
pattern = re.compile(r"publication (?:no\.|number) ([\w-]+)")

for row in data:
    info = row['Patents_info']
    match = pattern.search(info)
    if match:
        univ_cal_pub_nums.add(match.group(1))

print(f"__RESULT__:\n{json.dumps(list(univ_cal_pub_nums))}")"""

env_args = {'var_function-call-7292629965275044235': 'file_storage/function-call-7292629965275044235.json', 'var_function-call-3051103024558862659': 'file_storage/function-call-3051103024558862659.json', 'var_function-call-1533827457722000501': [{'count(*)': '277813'}]}

exec(code, env_args)

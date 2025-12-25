code = """import json
import re

# Load the UNIV CAL patents result
uc_patents_file = locals()['var_function-call-13353732409083150801']
with open(uc_patents_file, 'r') as f:
    uc_patents_data = json.load(f)

# Extract publication numbers
# Patterns to capture publication number from Patents_info
pub_num_pattern = re.compile(r"publication no\.? ([\w-]+)\.?|pub\.? number ([\w-]+)\.?|publication number ([\w-]+)\.?")

uc_pub_nums = set()

for entry in uc_patents_data:
    info = entry['Patents_info']
    match = pub_num_pattern.search(info)
    if match:
        # get the non-None group
        p_num = next((g for g in match.groups() if g is not None), None)
        if p_num:
            uc_pub_nums.add(p_num)

print(f"__RESULT__:\n{json.dumps(list(uc_pub_nums))}")"""

env_args = {'var_function-call-10578193635103741538': 'file_storage/function-call-10578193635103741538.json', 'var_function-call-13926955435789849247': [{'count(*)': '277813'}], 'var_function-call-13353732409083150801': 'file_storage/function-call-13353732409083150801.json'}

exec(code, env_args)

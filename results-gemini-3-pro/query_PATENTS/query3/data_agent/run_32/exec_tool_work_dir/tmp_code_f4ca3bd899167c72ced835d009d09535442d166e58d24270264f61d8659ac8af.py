code = """import json
import re

# Load the result from the previous query
file_path = locals()['var_function-call-5726066764159210267']
with open(file_path, 'r') as f:
    univ_cal_data = json.load(f)

univ_cal_pub_nums = set()
# Regex to find publication number. 
# Pattern based on "publication number US-12345-A" or "pub. number US-12345-A" or "publication no. ..."
# Looking at the data: "... publication number US-2022074631-A1."
pattern = re.compile(r"publication (?:number|no\.|no)\s*([A-Za-z0-9-]+)")
pattern2 = re.compile(r"pub\. number\s*([A-Za-z0-9-]+)")

for entry in univ_cal_data:
    text = entry.get('Patents_info', '')
    match = pattern.search(text)
    if match:
        univ_cal_pub_nums.add(match.group(1).rstrip('.')) # remove trailing dot if any
    else:
        match2 = pattern2.search(text)
        if match2:
            univ_cal_pub_nums.add(match2.group(1).rstrip('.'))

print(f"Found {len(univ_cal_pub_nums)} UNIV CALIFORNIA publication numbers.")
print(list(univ_cal_pub_nums)[:10])

# Verify if we have enough numbers or if the regex needs tuning."""

env_args = {'var_function-call-5447102030661239686': 'file_storage/function-call-5447102030661239686.json', 'var_function-call-5726066764159210267': 'file_storage/function-call-5726066764159210267.json'}

exec(code, env_args)

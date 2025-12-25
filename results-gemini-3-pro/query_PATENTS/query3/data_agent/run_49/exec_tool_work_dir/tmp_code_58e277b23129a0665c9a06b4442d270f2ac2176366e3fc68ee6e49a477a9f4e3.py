code = """import json
import re

# Load UC patents
with open(locals()['var_function-call-3627068258271379600'], 'r') as f:
    uc_records = json.load(f)

uc_pub_numbers = set()

# Regex to capture publication number
# Patterns seen:
# "pub. number [A-Z0-9-]+"
# "publication number [A-Z0-9-]+"
# "publication no. [A-Z0-9-]+"
# "publication no [A-Z0-9-]+"
pub_num_pattern = re.compile(r'(?:pub\.?|publication)\s+(?:number|no\.?)\s+([A-Z]{2}-?[0-9]+-?[A-Z0-9]*)', re.IGNORECASE)

for rec in uc_records:
    info = rec['Patents_info']
    match = pub_num_pattern.search(info)
    if match:
        uc_pub_numbers.add(match.group(1))

print(f"__RESULT__:\n{json.dumps(list(uc_pub_numbers)[:10])}") # Print a sample to verify"""

env_args = {'var_function-call-12868220818788144791': 'file_storage/function-call-12868220818788144791.json', 'var_function-call-2492118762681271268': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_function-call-18177144468656687824': [{'COUNT(*)': '277813'}], 'var_function-call-6015838364880532085': [{'COUNT(*)': '0'}], 'var_function-call-3627068258271379600': 'file_storage/function-call-3627068258271379600.json'}

exec(code, env_args)

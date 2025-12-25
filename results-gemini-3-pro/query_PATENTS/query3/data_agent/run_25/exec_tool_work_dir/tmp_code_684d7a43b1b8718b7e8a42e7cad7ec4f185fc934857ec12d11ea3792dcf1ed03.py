code = """import json
import re

# Load the result from the previous query
with open('var_function-call-6448478139818768888.json', 'r') as f:
    uc_patents_data = json.load(f)

uc_pub_numbers = set()
# Regex to find publication number
# Patterns seen: 
# "publication number US-11081687-B2."
# "publication no. US-2017194630-A1."
# "pub. number TW-201925402-A."
# "publication number US-2022074631-A1" (maybe without dot at end)

regex = re.compile(r"pub(?:lication)?(?:\s+no\.|lication\s+no\.|lication\s+number|\.\s+number)\s+([A-Za-z0-9-]+)")

for row in uc_patents_data:
    info = row.get('Patents_info', '')
    match = regex.search(info)
    if match:
        uc_pub_numbers.add(match.group(1))

print(f"Found {len(uc_pub_numbers)} unique UC publication numbers.")
print("__RESULT__:")
print(json.dumps(list(uc_pub_numbers)))"""

env_args = {'var_function-call-6728768727131286423': 'file_storage/function-call-6728768727131286423.json', 'var_function-call-6448478139818768888': 'file_storage/function-call-6448478139818768888.json'}

exec(code, env_args)

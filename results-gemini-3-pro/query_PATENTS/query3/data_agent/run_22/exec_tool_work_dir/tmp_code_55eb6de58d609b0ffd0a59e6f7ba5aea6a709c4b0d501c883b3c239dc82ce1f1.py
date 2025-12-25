code = """import json
import re

# Load the result from the previous query (UC patents)
with open('var_function-call-8877768949099455839.json', 'r') as f:
    uc_patents_data = json.load(f)

print(f"Loaded {len(uc_patents_data)} UC patents.")

uc_pub_nums = set()
# Regex to find publication number
# Patterns seen: "publication number X", "pub. number X", "publication no. X"
# Also ends with dot or space.
regex = re.compile(r'(?:publication|pub\.)\s+(?:number|no\.|num\.)\s+([A-Za-z0-9\-]+)', re.IGNORECASE)

for row in uc_patents_data:
    info = row.get('Patents_info', '')
    match = regex.search(info)
    if match:
        # Remove trailing dot if captured (though \w usually doesn't capture dot, - is included)
        # The captured group might have a trailing dot if the regex is not precise.
        # [A-Za-z0-9\-] should be safe.
        pub_num = match.group(1).rstrip('.')
        uc_pub_nums.add(pub_num)

print(f"Extracted {len(uc_pub_nums)} unique UC publication numbers.")
print(list(uc_pub_nums)[:5]) # Print sample

print("__RESULT__:")
print(json.dumps(list(uc_pub_nums)))"""

env_args = {'var_function-call-9375773847238378810': ['publicationinfo'], 'var_function-call-17877599462760533689': 'file_storage/function-call-17877599462760533689.json', 'var_function-call-12779896554036072402': [{'count(*)': '277813'}], 'var_function-call-8877768949099455839': 'file_storage/function-call-8877768949099455839.json'}

exec(code, env_args)

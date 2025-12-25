code = """import json
import re

# Load the UC patents result
with open('15481659902855548868.json', 'r') as f:
    uc_data = json.load(f)

print(f"Total UC records: {len(uc_data)}")

# Extract publication numbers
# Pattern seems to be: "publication number X" or "pub. number X" or "publication no. X"
# followed by the number until space or dot or end.
# The number usually looks like CC-NNNNN-KC.

pub_nums = set()
for row in uc_data:
    info = row['Patents_info']
    # Regex to capture the number
    # Looking for 'publication number', 'pub. number', 'publication no.' case insensitive
    match = re.search(r'(?:publication|pub\.?)\s+(?:number|no\.)\s+([A-Z]{2}-[\w\d]+-[A-Z\d]+)', info, re.IGNORECASE)
    if match:
        pub_nums.add(match.group(1))
    else:
        # Try finding just the pattern if the text is slightly different
        # Or look for pattern after "has " or "with "
        pass

print(f"Extracted {len(pub_nums)} unique UC publication numbers.")
print("__RESULT__:")
print(json.dumps(list(pub_nums)))"""

env_args = {'var_function-call-530179975509141049': 'file_storage/function-call-530179975509141049.json', 'var_function-call-8727398071354351262': [{'COUNT(*)': '277813'}], 'var_function-call-15481659902855548868': 'file_storage/function-call-15481659902855548868.json'}

exec(code, env_args)

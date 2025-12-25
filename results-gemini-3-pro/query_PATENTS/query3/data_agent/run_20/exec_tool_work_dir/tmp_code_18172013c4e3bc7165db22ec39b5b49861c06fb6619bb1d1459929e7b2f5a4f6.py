code = """import json
import re

# Get the file path from the variable
file_path = locals()['var_function-call-15481659902855548868']

# Load the UC patents result
with open(file_path, 'r') as f:
    uc_data = json.load(f)

print(f"Total UC records: {len(uc_data)}")

pub_nums = set()
for row in uc_data:
    info = row['Patents_info']
    # Regex to capture the number
    match = re.search(r'(?:publication|pub\.?)\s+(?:number|no\.)\s+([A-Z]{2}-[\w\d]+-[A-Z\d]+)', info, re.IGNORECASE)
    if match:
        pub_nums.add(match.group(1))

print(f"Extracted {len(pub_nums)} unique UC publication numbers.")
print("__RESULT__:")
print(json.dumps(list(pub_nums)))"""

env_args = {'var_function-call-530179975509141049': 'file_storage/function-call-530179975509141049.json', 'var_function-call-8727398071354351262': [{'COUNT(*)': '277813'}], 'var_function-call-15481659902855548868': 'file_storage/function-call-15481659902855548868.json'}

exec(code, env_args)

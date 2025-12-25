code = """import json
import re

# Load the result from the previous query
file_path = locals()['var_function-call-163982095095483053']
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records found: {len(data)}")

# Extract publication numbers
uc_pubs = set()
pattern = re.compile(r"(?:publication|pub\.)\s+(?:number|no\.)\s+([A-Z]{2}-[\w\d-]+)")

for row in data:
    info = row['Patents_info']
    match = pattern.search(info)
    if match:
        uc_pubs.add(match.group(1))

print(f"Unique UNIV CALIFORNIA publication numbers: {len(uc_pubs)}")
print("__RESULT__:")
print(json.dumps(list(uc_pubs)[:10])) # Print first 10"""

env_args = {'var_function-call-3523691000772885977': 'file_storage/function-call-3523691000772885977.json', 'var_function-call-163982095095483053': 'file_storage/function-call-163982095095483053.json'}

exec(code, env_args)

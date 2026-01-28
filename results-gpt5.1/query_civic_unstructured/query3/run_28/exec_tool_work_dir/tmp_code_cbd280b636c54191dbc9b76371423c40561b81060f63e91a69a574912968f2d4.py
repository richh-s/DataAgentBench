code = """import json, re
from pathlib import Path

# Load full funding data
funding_path = var_call_7yhmipQ3JEx8yqjvPcu9Mkex
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Filter funding records whose Project_Name suggests emergency/FEMA relevance
pattern = re.compile(r"emergency|FEMA", re.IGNORECASE)
relevant = [r for r in funding if pattern.search(r.get('Project_Name',''))]

result = json.dumps(relevant)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_7yhmipQ3JEx8yqjvPcu9Mkex': 'file_storage/call_7yhmipQ3JEx8yqjvPcu9Mkex.json', 'var_call_soquy0zFnA5pN7S59PQyQTEI': 'file_storage/call_soquy0zFnA5pN7S59PQyQTEI.json'}

exec(code, env_args)

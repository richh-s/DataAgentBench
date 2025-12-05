code = """import json
from pathlib import Path

path = Path(var_call_ik3xz94UXVjQ6L4EKwDFB5l9)
with open(path) as f:
    union_query = json.load(f)

print("__RESULT__:")
print(json.dumps(union_query))"""

env_args = {'var_call_Vze9xVeDncn7VRYU7xzfW3y9': 'file_storage/call_Vze9xVeDncn7VRYU7xzfW3y9.json', 'var_call_j4fu3NAjWGHxAbozr67qCFVu': [{'cnt': '15016'}], 'var_call_ik3xz94UXVjQ6L4EKwDFB5l9': 'file_storage/call_ik3xz94UXVjQ6L4EKwDFB5l9.json'}

exec(code, env_args)

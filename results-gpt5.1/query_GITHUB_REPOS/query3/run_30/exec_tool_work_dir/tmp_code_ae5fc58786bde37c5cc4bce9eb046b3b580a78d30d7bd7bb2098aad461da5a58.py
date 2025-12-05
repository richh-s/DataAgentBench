code = """import json
from pathlib import Path

path = Path(var_call_zhWBVP5Pyj2ekBPFGybQUTm9)
text = json.loads(path.read_text())
repos = [r.strip() for r in text.split("','")]  # split back
# Clean leading/trailing quotes/spaces
repos = [r.strip().strip("'").strip() for r in repos]
# Remove possible empty strings
repos = [r for r in repos if r]

# Build batched IN clauses to avoid overly long query
batches = []
batch_size = 300
for i in range(0, len(repos), batch_size):
    batch = repos[i:i+batch_size]
    # escape single quotes in repo names
    batch_escaped = [r.replace("'", "''") for r in batch]
    clause = "('" + "','".join(batch_escaped) + "')"
    batches.append(clause)

result = batches

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_deO56blwR8JXCKwqFpYbHUU2': 'file_storage/call_deO56blwR8JXCKwqFpYbHUU2.json', 'var_call_O7cD7J6JI4PEkd3pSndM23uv': [{'1': '1'}], 'var_call_zhWBVP5Pyj2ekBPFGybQUTm9': 'file_storage/call_zhWBVP5Pyj2ekBPFGybQUTm9.json'}

exec(code, env_args)

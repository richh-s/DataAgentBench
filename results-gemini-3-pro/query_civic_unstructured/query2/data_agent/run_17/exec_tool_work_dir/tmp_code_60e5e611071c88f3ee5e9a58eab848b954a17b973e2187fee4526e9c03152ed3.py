code = """import json
import re

with open(locals()['var_function-call-10057184920144794313'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-10057184920144796126'], 'r') as f:
    civic_docs = json.load(f)

target_name = "Bluffs Park Shade Structure"
found = False
context = ""

for doc in civic_docs:
    text = doc['text']
    if target_name in text:
        found = True
        idx = text.find(target_name)
        context = text[idx:idx+500]
        break

print("__RESULT__:")
print(json.dumps({"found": found, "context": context}))"""

env_args = {'var_function-call-10057184920144794313': 'file_storage/function-call-10057184920144794313.json', 'var_function-call-10057184920144796126': 'file_storage/function-call-10057184920144796126.json', 'var_function-call-16463367332335965304': {'total_funding': 0, 'projects': [], 'debug': []}}

exec(code, env_args)

code = """import json
import re

with open(locals()['var_function-call-16179877025922844511'], 'r') as f:
    civic_docs = json.load(f)

target_name = "Permanent Skate Park"
escaped_name = re.escape(target_name)

found_info = []

for doc in civic_docs:
    text = doc['text']
    matches = list(re.finditer(escaped_name, text, re.IGNORECASE))
    for m in matches:
        start = m.start()
        # Look ahead for next project header or just take a chunk
        # Just take 500 chars for debugging
        chunk = text[start:start+1000]
        
        lines = chunk.splitlines()
        for line in lines:
            l = line.lower()
            if "design" in l:
                continue
            if ("complete" in l or "completion" in l) and "2022" in l:
                found_info.append(f"Doc: {doc['filename']}, Line: {line}")

print("__RESULT__:")
print(json.dumps(found_info))"""

env_args = {'var_function-call-13030964589425589265': 'file_storage/function-call-13030964589425589265.json', 'var_function-call-13030964589425590204': 'file_storage/function-call-13030964589425590204.json', 'var_function-call-16179877025922844511': 'file_storage/function-call-16179877025922844511.json', 'var_function-call-15826040215521897163': {'total': 118000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Permanent Skate Park', 'amount': 97000}]}}

exec(code, env_args)

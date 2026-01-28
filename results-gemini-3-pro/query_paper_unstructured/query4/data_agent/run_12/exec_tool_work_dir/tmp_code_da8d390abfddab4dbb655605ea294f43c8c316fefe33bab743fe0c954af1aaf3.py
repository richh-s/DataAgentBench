code = """import json
import re

file_path = locals()['var_function-call-5896966146300588964']
with open(file_path, 'r') as f:
    papers = json.load(f)

count = 0
headers = []
for p in papers:
    text = p.get('text', '')
    if 'physical activity' in text.lower():
        headers.append(text[:500])
        count += 1
        if count >= 5:
            break

print('__RESULT__:')
print(json.dumps(headers))"""

env_args = {'var_function-call-2683298839036433804': ['paper_docs'], 'var_function-call-17469928963468779101': 'file_storage/function-call-17469928963468779101.json', 'var_function-call-5896966146300588964': 'file_storage/function-call-5896966146300588964.json', 'var_function-call-15408307413232285076': []}

exec(code, env_args)

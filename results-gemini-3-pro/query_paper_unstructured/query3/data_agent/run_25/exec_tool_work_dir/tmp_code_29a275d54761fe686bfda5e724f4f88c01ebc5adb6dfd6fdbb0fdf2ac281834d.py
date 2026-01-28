code = """import json
import re

with open(locals()['var_function-call-4403390195297864469'], 'r') as f:
    docs = json.load(f)

doc = docs[0]
text = doc['text']
text_lower = text.lower()

result = {}
result['length'] = len(text)
result['has_empirical'] = 'empirical' in text_lower
result['has_contribution'] = 'contribution' in text_lower

matches = list(re.finditer(r"contribution", text, re.IGNORECASE))
snippets = []
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 50)
    snippets.append(text[start:end].replace("\n", " "))
result['contribution_snippets'] = snippets

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4403390195297864469': 'file_storage/function-call-4403390195297864469.json', 'var_function-call-5079307557547688021': ['paper_docs'], 'var_function-call-3097430276196367090': 'file_storage/function-call-3097430276196367090.json'}

exec(code, env_args)

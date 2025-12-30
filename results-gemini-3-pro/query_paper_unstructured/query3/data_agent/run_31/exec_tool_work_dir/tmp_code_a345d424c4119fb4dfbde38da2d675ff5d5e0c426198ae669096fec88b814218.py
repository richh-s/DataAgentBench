code = """import json

with open(locals()['var_function-call-5623558947517056704'], 'r') as f:
    data = json.load(f)

doc = data[0]
text = doc['text']

print("Start of text:")
print(text[:500])
print("\nEnd of text:")
print(text[-500:])

print("\nSearching for metadata...")
lower_text = text.lower()
if "contribution" in lower_text:
    idx = lower_text.find("contribution")
    print("Found 'contribution':")
    print(text[idx:idx+100])

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-5623558947517056704': 'file_storage/function-call-5623558947517056704.json'}

exec(code, env_args)

code = """import json, re
# var_call_9LUcJa07UacZD6oGJc9q86b9 is available in storage as a path to the full JSON result
path = var_call_9LUcJa07UacZD6oGJc9q86b9
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []
for doc in data:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    # consider publication year 2016 if '2016' appears in the text
    if re.search(r'\b2016\b', text):
        results.append(title)

# deduplicate
titles_2016 = sorted(list(set(results)))
output = json.dumps(titles_2016)
print('__RESULT__:')
print(output)"""

env_args = {'var_call_9LUcJa07UacZD6oGJc9q86b9': 'file_storage/call_9LUcJa07UacZD6oGJc9q86b9.json'}

exec(code, env_args)

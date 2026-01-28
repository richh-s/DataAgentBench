code = """import json
import re

# Load data
with open(locals()['var_function-call-7459141219968339162'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
print("DEBUG INFO:")
count = 0
for p in papers:
    text = p['text']
    if 'food' in text.lower():
        count += 1
        # Find where 'food' is
        idx = text.lower().find('food')
        snippet = text[max(0, idx-50):min(len(text), idx+50)].replace('\n', ' ')
        print(f"Match in: {p['filename']} -> ...{snippet}...")
        if count > 5:
            break

print(f"Total papers with 'food' in text: {len([p for p in papers if 'food' in p['text'].lower()])}")"""

env_args = {'var_function-call-3676184941267040123': 'file_storage/function-call-3676184941267040123.json', 'var_function-call-6873213907714452995': 'file_storage/function-call-6873213907714452995.json', 'var_function-call-17043150740226976793': 'file_storage/function-call-17043150740226976793.json', 'var_function-call-7459141219968339162': 'file_storage/function-call-7459141219968339162.json', 'var_function-call-4763535483607380': {'total_citations': 0, 'papers': []}}

exec(code, env_args)

code = """import json
import re

funding_path = locals()['var_function-call-13164751492978107468']
civic_path = locals()['var_function-call-9869211362583101527']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

all_text = ""
for d in civic_data:
    all_text += d.get('text', '') + ' '

# Debug for Bluffs Park Shade Structure
target = "Bluffs Park Shade Structure"
print(f"DEBUG: Searching for '{target}'")

# Check if target is in all_text
if target in all_text:
    print("DEBUG: Exact string found in text.")
else:
    print("DEBUG: Exact string NOT found in text.")

# Check case insensitive
matches = [m.start() for m in re.finditer(re.escape(target), all_text, re.IGNORECASE)]
print(f"DEBUG: Found {len(matches)} matches.")

for start in matches:
    snippet = all_text[start:start+200]
    print(f"DEBUG Snippet: {json.dumps(snippet)}")
    
    snippet_lower = snippet.lower()
    if 'completed' in snippet_lower and '2022' in snippet_lower:
        print("DEBUG: Condition Met")
    else:
        print("DEBUG: Condition NOT Met")

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-13164751492978107468': 'file_storage/function-call-13164751492978107468.json', 'var_function-call-13164751492978107155': 'file_storage/function-call-13164751492978107155.json', 'var_function-call-9869211362583101527': 'file_storage/function-call-9869211362583101527.json', 'var_function-call-4590254566354638505': {'confirmed_projects': [], 'total_funding': 0}}

exec(code, env_args)

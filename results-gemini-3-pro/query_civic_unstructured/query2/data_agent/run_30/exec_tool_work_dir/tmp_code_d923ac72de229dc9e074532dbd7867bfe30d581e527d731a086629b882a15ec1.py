code = """import json
import re

with open(locals()['var_function-call-3018582044476683837'], 'r') as f:
    civic_docs = json.load(f)

projects_of_interest = ["Malibu Park Drainage Improvements", "Legacy Park Paver Repair Project", "Legacy Park Benches", "Bluffs Park Shade Structure"]

full_text = chr(10).join([d['text'] for d in civic_docs])

# Simple text search for these names and surrounding text
results = {}

for name in projects_of_interest:
    # Find all occurrences
    indices = [m.start() for m in re.finditer(re.escape(name), full_text)]
    snippets = []
    for idx in indices:
        # Grab 500 chars after
        snippets.append(full_text[idx:idx+500])
    results[name] = snippets

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3018582044476684640': 'file_storage/function-call-3018582044476684640.json', 'var_function-call-3018582044476683837': 'file_storage/function-call-3018582044476683837.json', 'var_function-call-8938805927192840560': {'total_funding': 21000, 'projects': ['Bluffs Park Shade Structure']}, 'var_function-call-2182818405605862330': 'file_storage/function-call-2182818405605862330.json'}

exec(code, env_args)

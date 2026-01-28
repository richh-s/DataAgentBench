code = """import json
import re

file_path = locals()['var_function-call-18099153275120727410']
with open(file_path, 'r') as f:
    papers = json.load(f)

debug_output = []

for p in papers:
    debug_output.append('='*20)
    debug_output.append(f"Title: {p['filename']}")
    text = p['text']
    
    lines = text.splitlines()
    found_contrib = False
    for line in lines:
        if 'contribution' in line.lower():
            # Avoid overly long lines
            debug_output.append(f"COORD contribution: {line.strip()[:100]}")
            found_contrib = True
    
    if not found_contrib:
        debug_output.append('No contribution keyword found in lines.')

    match = re.search(r'Copyright (20[0-9]{2})', text)
    if match:
        debug_output.append(f"Year (Copyright): {match.group(1)}")
    else:
        debug_output.append('Year not found via Copyright')

    if 'empirical' in text.lower():
        debug_output.append('Contains empirical: Yes')
    else:
        debug_output.append('Contains empirical: No')

print("__RESULT__:")
print(json.dumps(debug_output))"""

env_args = {'var_function-call-10449789667232023992': ['paper_docs'], 'var_function-call-10449789667232022543': 'file_storage/function-call-10449789667232022543.json', 'var_function-call-10449789667232025190': 'file_storage/function-call-10449789667232025190.json', 'var_function-call-18099153275120727410': 'file_storage/function-call-18099153275120727410.json'}

exec(code, env_args)

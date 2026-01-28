code = """import json
import re

# Load the sample paper
with open(locals()['var_function-call-5688695509175080773'], 'r') as f:
    papers = json.load(f)

paper = papers[0]
text = paper['text']
print("Title:", paper['filename'])
print("First 300 chars:", repr(text[:300]))

# Check for "Contribution" pattern
print("--- Searching for 'Contribution' ---")
for m in re.finditer(r'contribution', text, re.IGNORECASE):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 50)
    snippet = text[start:end].replace('\n', ' ')
    print(f"Match: ...{snippet}...")
    if len(snippet) > 500: break # just print a few

print("--- Searching for 'Empirical' ---")
for m in re.finditer(r'empirical', text, re.IGNORECASE):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 50)
    snippet = text[start:end].replace('\n', ' ')
    print(f"Match: ...{snippet}...")
    if len(snippet) > 500: break"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json'}

exec(code, env_args)

code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-9278851709122145007'], 'r') as f:
    papers_data = json.load(f)

results = []
for paper in papers_data:
    text = paper['text']
    # Search for 'food'
    matches = [m.start() for m in re.finditer(r'food', text, re.IGNORECASE)]
    if matches:
        # Get context for first match
        start = max(0, matches[0] - 50)
        end = min(len(text), matches[0] + 50)
        context = text[start:end].replace('\n', ' ')
        results.append({"filename": paper['filename'], "context": context})

print("__RESULT__:")
print(json.dumps(results[:5])) # Show first 5"""

env_args = {'var_function-call-10309278563115687463': ['paper_docs'], 'var_function-call-17310270331774513134': 'file_storage/function-call-17310270331774513134.json', 'var_function-call-14859437005275468977': 'file_storage/function-call-14859437005275468977.json', 'var_function-call-9278851709122145007': 'file_storage/function-call-9278851709122145007.json', 'var_function-call-2702061835981032480': 0, 'var_function-call-14459346751113599875': 'Done'}

exec(code, env_args)

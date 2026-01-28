code = """import json, pandas as pd
from pathlib import Path

# Load full results
with open(var_call_25H4rIme747rQDxJ7GorMxhp, 'r') as f:
    chi_files = json.load(f)
with open(var_call_TC9KUmYjlZ3G8KaZOvuJs6Ha, 'r') as f:
    citations_2020 = json.load(f)

chi_titles = {d['filename'].rsplit('.txt', 1)[0] for d in chi_files}

# Sum citations for titles that are CHI papers

total = 0
for row in citations_2020:
    if row['title'] in chi_titles:
        total += int(row['total_citations'])

result = total

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_25H4rIme747rQDxJ7GorMxhp': 'file_storage/call_25H4rIme747rQDxJ7GorMxhp.json', 'var_call_TC9KUmYjlZ3G8KaZOvuJs6Ha': 'file_storage/call_TC9KUmYjlZ3G8KaZOvuJs6Ha.json'}

exec(code, env_args)

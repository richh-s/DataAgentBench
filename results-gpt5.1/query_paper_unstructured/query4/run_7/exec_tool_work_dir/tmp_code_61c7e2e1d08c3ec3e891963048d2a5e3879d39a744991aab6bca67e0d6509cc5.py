code = """import re, json
from pathlib import Path

# Load full citation aggregates
with open(var_call_1FXe2g6onr80R4px9lwxyA6E, 'r') as f:
    citations = json.load(f)

# Load paper docs preview list from var_call_XLleyTElRSMJDFxjI7sji4nS (already full or partial list)
papers = var_call_XLleyTElRSMJDFxjI7sji4nS

# Heuristic: extract year from text via regex for 2016, and domain via 'physical activity'
results = []
for p in papers:
    text = p.get('text', '')
    # Require explicit 2016 mention near ACM reference lines or year patterns
    if '2016' not in text:
        continue
    if 'physical activity' not in text.lower():
        continue
    # Title is filename without .txt
    filename = p.get('filename', '')
    title = re.sub(r"\.txt$", '', filename)
    # Find total citations for this title
    total = 0
    for c in citations:
        if c['title'] == title:
            total = int(c['total_citations'])
            break
    results.append({'title': title, 'total_citations': total})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_XLleyTElRSMJDFxjI7sji4nS': 'file_storage/call_XLleyTElRSMJDFxjI7sji4nS.json', 'var_call_1FXe2g6onr80R4px9lwxyA6E': 'file_storage/call_1FXe2g6onr80R4px9lwxyA6E.json'}

exec(code, env_args)

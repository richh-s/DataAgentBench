code = """import re, json
from pathlib import Path

# Load full citation aggregates
with open(var_call_lQY5754ZruRtv61k3F7BUc1O, 'r') as f:
    citations = json.load(f)

# Build mapping title -> total_citations (int)
cit_map = {c['title']: int(c['total_citations']) for c in citations}

# Load paper docs and filter by year 2016 and domain 'physical activity'
with open(var_call_zB4ItiInlVhwlFDBA6SYYEvy, 'r') as f:
    docs = json.load(f)

results = []
for d in docs:
    text = d.get('text', '')
    # Extract year: look for 2016 explicitly
    if '2016' not in text:
        continue
    # Domain filter: 'physical activity' substring, case-insensitive
    if re.search(r'physical activity', text, re.IGNORECASE) is None:
        continue
    # Title from filename
    fn = d.get('filename','')
    title = re.sub(r'\.txt$', '', fn)
    # Match citations title exactly
    total_cit = cit_map.get(title)
    if total_cit is None:
        continue
    results.append({'title': title, 'total_citations': total_cit})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_zB4ItiInlVhwlFDBA6SYYEvy': 'file_storage/call_zB4ItiInlVhwlFDBA6SYYEvy.json', 'var_call_lQY5754ZruRtv61k3F7BUc1O': 'file_storage/call_lQY5754ZruRtv61k3F7BUc1O.json'}

exec(code, env_args)

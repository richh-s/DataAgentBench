code = """import json, re

path = var_call_QqRXYIisemYrUlTibJ8VYOlC
with open(path, 'r') as f:
    records = json.load(f)

filtered = []
for r in records:
    name = r.get('assignee','').strip()
    if not name:
        continue
    if name.upper() == 'UNIV CALIFORNIA':
        continue
    if re.match(r'^(US|EP|WO|JP|KR|TW|CN|FR|DE|ID)-', name):
        continue
    if re.match(r'^[A-Z]{2,}-?\d', name):
        continue
    filtered.append((name, r.get('cpc_titles', [])))

agg = {}
for name, titles in filtered:
    agg.setdefault(name, [])
    for t in titles:
        if t not in agg[name]:
            agg[name].append(t)

lines = []
for name in sorted(agg.keys(), key=lambda s: s.upper()):
    titles = agg[name]
    clean_titles = [ (t if t is not None else 'Unknown CPC title') for t in titles ]
    line = name + ': ' + '; '.join(clean_titles)
    lines.append(line)

final_text = '\n'.join(lines)

print("__RESULT__:")
print(json.dumps(final_text))"""

env_args = {'var_call_6Kreubw6sda70vrL4hVhh4Px': ['publicationinfo'], 'var_call_c23BeMWTAwQXdF8yov9bBp9t': ['cpc_definition'], 'var_call_l55xEibBEPLvcbgsB4ym2Tu7': 'file_storage/call_l55xEibBEPLvcbgsB4ym2Tu7.json', 'var_call_F0XFlqDiYITWL1MBYbrkembO': 'file_storage/call_F0XFlqDiYITWL1MBYbrkembO.json', 'var_call_lRNyp9wRymrVkIyIL4PoXol6': 'file_storage/call_lRNyp9wRymrVkIyIL4PoXol6.json', 'var_call_QqRXYIisemYrUlTibJ8VYOlC': 'file_storage/call_QqRXYIisemYrUlTibJ8VYOlC.json'}

exec(code, env_args)

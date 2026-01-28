code = """import json, re

# Read the stored execute_python result file
path = var_call_QqRXYIisemYrUlTibJ8VYOlC
with open(path, 'r') as f:
    records = json.load(f)

# Filter function to exclude publication-number-like assignees and exclude UNIV CALIFORNIA exact
exclude_prefixes = re.compile(r'^(US|EP|WO|JP|KR|TW|CN|FR|DE|ID|WO)\b|-\d')

filtered = []
for r in records:
    name = r.get('assignee','').strip()
    if not name:
        continue
    if name.upper() == 'UNIV CALIFORNIA':
        continue
    # exclude if starts with known publication prefixes like 'US-' or 'EP-'
    if re.match(r'^(US|EP|WO|JP|KR|TW|CN|FR|DE|ID)-', name):
        continue
    # exclude if name ends with a period and looks like a publication id
    if re.match(r'^[A-Z]{2,}-?\d', name):
        continue
    # otherwise include
    filtered.append((name, r.get('cpc_titles', [])))

# Aggregate by assignee, combine titles
agg = {}
for name, titles in filtered:
    if name not in agg:
        agg[name] = []
    for t in titles:
        if t not in agg[name]:
            agg[name].append(t)

# Build final plain-text answer lines
lines = []
for name in sorted(agg.keys(), key=lambda s: s.upper()):
    titles = agg[name]
    # represent None as 'Unknown CPC title'
    clean_titles = [ (t if t is not None else 'Unknown CPC title') for t in titles ]
    line = f"{name}: {"; ".join(clean_titles)}"
    lines.append(line)

final_text = "\n".join(lines)

# Print result according to format
print("__RESULT__:")
print(json.dumps(final_text))"""

env_args = {'var_call_6Kreubw6sda70vrL4hVhh4Px': ['publicationinfo'], 'var_call_c23BeMWTAwQXdF8yov9bBp9t': ['cpc_definition'], 'var_call_l55xEibBEPLvcbgsB4ym2Tu7': 'file_storage/call_l55xEibBEPLvcbgsB4ym2Tu7.json', 'var_call_F0XFlqDiYITWL1MBYbrkembO': 'file_storage/call_F0XFlqDiYITWL1MBYbrkembO.json', 'var_call_lRNyp9wRymrVkIyIL4PoXol6': 'file_storage/call_lRNyp9wRymrVkIyIL4PoXol6.json', 'var_call_QqRXYIisemYrUlTibJ8VYOlC': 'file_storage/call_QqRXYIisemYrUlTibJ8VYOlC.json'}

exec(code, env_args)

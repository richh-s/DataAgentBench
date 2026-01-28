code = """import json, re

# var_call_7Dsc4rWoxdyH7aeAHw2bEOrG is a file path to the JSON result from previous step
path = var_call_7Dsc4rWoxdyH7aeAHw2bEOrG
with open(path, 'r') as f:
    data = json.load(f)

# Build final lines: Assignee: title1; title2
lines = []
for r in data:
    name = r.get('assignee','').strip()
    if not name:
        continue
    titles = r.get('cpc_titles') or []
    clean_titles = [(t if t is not None else 'Unknown CPC title') for t in titles]
    line = name + ': ' + '; '.join(clean_titles)
    lines.append(line)

final_text = '\n'.join(lines)

print("__RESULT__:")
print(json.dumps(final_text))"""

env_args = {'var_call_6Kreubw6sda70vrL4hVhh4Px': ['publicationinfo'], 'var_call_c23BeMWTAwQXdF8yov9bBp9t': ['cpc_definition'], 'var_call_l55xEibBEPLvcbgsB4ym2Tu7': 'file_storage/call_l55xEibBEPLvcbgsB4ym2Tu7.json', 'var_call_F0XFlqDiYITWL1MBYbrkembO': 'file_storage/call_F0XFlqDiYITWL1MBYbrkembO.json', 'var_call_lRNyp9wRymrVkIyIL4PoXol6': 'file_storage/call_lRNyp9wRymrVkIyIL4PoXol6.json', 'var_call_QqRXYIisemYrUlTibJ8VYOlC': 'file_storage/call_QqRXYIisemYrUlTibJ8VYOlC.json', 'var_call_7Dsc4rWoxdyH7aeAHw2bEOrG': 'file_storage/call_7Dsc4rWoxdyH7aeAHw2bEOrG.json'}

exec(code, env_args)

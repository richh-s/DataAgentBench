code = """import json
import re

funding_path = locals()['var_function-call-13164751492978107468']
civic_path = locals()['var_function-call-9869211362583101527']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

all_text = ""
for d in civic_data:
    all_text += d.get('text', '') + ' '

debug_info = {}
debug_info['text_length'] = len(all_text)
debug_info['funding_count'] = len(funding_data)

target = "Bluffs Park Shade Structure"
debug_info['target_found_exact'] = target in all_text

matches = [m.start() for m in re.finditer(re.escape(target), all_text, re.IGNORECASE)]
debug_info['matches_count'] = len(matches)

snippets = []
for start in matches:
    snippets.append(all_text[start:start+200])
debug_info['snippets'] = snippets

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-13164751492978107468': 'file_storage/function-call-13164751492978107468.json', 'var_function-call-13164751492978107155': 'file_storage/function-call-13164751492978107155.json', 'var_function-call-9869211362583101527': 'file_storage/function-call-9869211362583101527.json', 'var_function-call-4590254566354638505': {'confirmed_projects': [], 'total_funding': 0}, 'var_function-call-11353638954296130998': 'Done'}

exec(code, env_args)

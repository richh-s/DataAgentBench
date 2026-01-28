code = """import json, re
p = var_call_wImwkSyb52z6GhaPMqPSk2rh
with open(p, 'r', encoding='utf-8') as f:
    docs = json.load(f)
found = set()
for d in docs:
    text = d.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'\bpark\b', line, re.I):
            snippet = ' '.join(lines[max(0, i-2):i+1]).strip()
            following = ' '.join(lines[i:i+6])
            if re.search(r'completed', following, re.I) and re.search(r'2022', following):
                m = re.search(r'([A-Z][A-Za-z0-9 &\-]{0,80}Park(?: [A-Za-z0-9 &\-]*)?)', snippet)
                if m:
                    name = m.group(1).strip()
                    found.add(name)
result = sorted(found)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wImwkSyb52z6GhaPMqPSk2rh': 'file_storage/call_wImwkSyb52z6GhaPMqPSk2rh.json'}

exec(code, env_args)

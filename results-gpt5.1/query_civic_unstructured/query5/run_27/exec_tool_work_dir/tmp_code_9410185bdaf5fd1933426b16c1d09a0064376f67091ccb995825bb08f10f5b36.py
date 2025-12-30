code = """import re, json
from pathlib import Path

path = Path(var_call_HRI4PW8QV1GTGI4uWDKyXvYP)
with path.open() as f:
    civic_docs = json.load(f)

disaster_projects_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    blocks = re.split(r'\n\s*\n', text)
    for b in blocks:
        lb = b.lower()
        if 'disaster' not in lb and 'fema' not in lb and 'woolsey' not in lb:
            continue
        if '2022' not in b:
            continue
        lines = [ln.strip() for ln in b.split('\n') if ln.strip()]
        for i, ln in enumerate(lines):
            if re.search(r'project', ln, re.I):
                around = '\n'.join(lines[max(0, i-2):i+3])
                if any(k in around for k in ['Begin Construction', 'Start', 'Design', 'Not Started', '2022']):
                    name = re.sub(r'[\u200b\ufeff]', '', ln)
                    disaster_projects_2022.add(name)

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    for m in re.finditer(r'([A-Z0-9][A-Za-z0-9 &/\.-]+?(?:\s*\((?:FEMA|CalOES|CalJPIA)[^)]*\)))', text):
        span = m.group(1)
        if 'project' in span.lower():
            disaster_projects_2022.add(span.strip())

result = sorted(disaster_projects_2022)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HRI4PW8QV1GTGI4uWDKyXvYP': 'file_storage/call_HRI4PW8QV1GTGI4uWDKyXvYP.json', 'var_call_P6B4Pp4mHIL5Skb0Zvflh20B': 'file_storage/call_P6B4Pp4mHIL5Skb0Zvflh20B.json'}

exec(code, env_args)

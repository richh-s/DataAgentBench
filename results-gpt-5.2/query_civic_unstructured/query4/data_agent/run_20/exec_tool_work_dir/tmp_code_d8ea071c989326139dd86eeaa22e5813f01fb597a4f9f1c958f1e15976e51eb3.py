code = """import json, re

p_docs = var_call_7D8EP2WAYggkcSvlh6EUsyhx
with open(p_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

pattern = re.compile(r"Spring\s*,?\s*2022|Spring\s+2022|2022\s*-\s*Spring|2022\s*Spring", re.IGNORECASE)
examples = []
for d in docs:
    text = d.get('text','')
    m = pattern.search(text)
    if m:
        lines = text.splitlines()
        found = False
        for idx, ln in enumerate(lines):
            if pattern.search(ln):
                start = max(0, idx-3)
                end = min(len(lines), idx+4)
                snippet = "\\n".join(lines[start:end])
                examples.append({'filename': d.get('filename'), 'snippet': snippet})
                found = True
                break
        if found and len(examples) >= 5:
            break

print('__RESULT__:')
print(json.dumps(examples))"""

env_args = {'var_call_1EWiZF0MWHnDBQUWPaYA512M': ['Funding'], 'var_call_7D8EP2WAYggkcSvlh6EUsyhx': 'file_storage/call_7D8EP2WAYggkcSvlh6EUsyhx.json', 'var_call_gkn6QJLGZl3ts1HELo7BGVOs': 'file_storage/call_gkn6QJLGZl3ts1HELo7BGVOs.json', 'var_call_aiIe4m3TtHHVjzNjac9me70B': {'count': 0, 'total_funding': 0, 'projects_started_spring_2022': [], 'missing_funding_projects': []}}

exec(code, env_args)

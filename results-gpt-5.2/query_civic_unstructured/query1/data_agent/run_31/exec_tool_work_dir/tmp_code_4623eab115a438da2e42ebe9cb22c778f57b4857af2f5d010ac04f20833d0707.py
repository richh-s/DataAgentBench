code = """import json, re

# Load funding projects with max_amount > 50000
path = var_call_4lH1Bphw4GYOlgJbXzwIJdOJ
with open(path, 'r', encoding='utf-8') as f:
    funding_max = json.load(f)
funding_set = {r['Project_Name'] for r in funding_max}

# Load civic docs
docs_path = var_call_P5RhoV0OlFfkTK7hvafKgjYt
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

project_names = set()

stop_re = re.compile(r"\n\s*(capital improvement projects\s*\(|disaster recovery projects\s*\(|disaster recovery projects|capital improvement projects\s*\(construction\)|capital improvement projects\s*\(not started\))", re.IGNORECASE)

for d in docs:
    text = d.get('text','') or ''
    low = text.lower()
    for m in re.finditer(r"capital improvement projects\s*\(design\)", low):
        tail = text[m.end():]
        sm = stop_re.search(tail)
        section = tail[:sm.start()] if sm else tail
        for line in section.splitlines():
            l = line.strip()
            if not l:
                continue
            if re.match(r"^(\(cid:|page\s+\d+\s+of\s+\d+|agenda item)", l, flags=re.IGNORECASE):
                continue
            if re.search(r"updates\s*:?$", l, flags=re.IGNORECASE):
                continue
            if re.search(r"project schedule", l, flags=re.IGNORECASE):
                continue
            if ':' in l:
                continue
            if len(l.split()) > 12:
                continue
            if not re.search(r"[A-Za-z]", l):
                continue
            project_names.add(l)

qualifying = sorted(project_names & funding_set)
result = {"count": len(qualifying)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4zzbOb3qZK6ZAC8V3SWf0OOz': [{'cnt': '276'}], 'var_call_P5RhoV0OlFfkTK7hvafKgjYt': 'file_storage/call_P5RhoV0OlFfkTK7hvafKgjYt.json', 'var_call_4lH1Bphw4GYOlgJbXzwIJdOJ': 'file_storage/call_4lH1Bphw4GYOlgJbXzwIJdOJ.json', 'var_call_JsBcrBhrcKWnNNOJh7iAbByL': 'file_storage/call_JsBcrBhrcKWnNNOJh7iAbByL.json'}

exec(code, env_args)

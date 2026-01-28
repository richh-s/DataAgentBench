code = """import json, re
from pathlib import Path

raw = var_call_R4XAkIbysGnUFFK0TcQb1VNg
if isinstance(raw, str) and raw.endswith('.json'):
    docs = json.loads(Path(raw).read_text())
else:
    docs = raw

spring2022_projects = set()

def extract_projects_from_doc(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = []
    for i, ln in enumerate(lines):
        if ln in ("Project Schedule:", "Estimated Schedule:", "Project Schedule (pending the MOU extension approval):"):
            j = i - 1
            while j >= 0 and (lines[j] == "" or lines[j].startswith("(cid") or lines[j].startswith("Page ") or lines[j].startswith("Agenda Item")):
                j -= 1
            if j >= 0:
                pname = lines[j]
                window = lines[i+1:i+12]
                joined = "\n".join(window)
                if re.search(r"\b(Begin (Construction|construction)|Start|Begin)\b\s*:\s*Spring\s+2022\b", joined, flags=re.I):
                    projects.append(pname)
    return projects

for d in docs:
    text = d.get('text','') or ''
    for p in extract_projects_from_doc(text):
        spring2022_projects.add(p)

result = {"projects_started_spring_2022": sorted(spring2022_projects), "count": len(spring2022_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_4zbtptmslrFMDJ0pQvTXodbd': ['Funding'], 'var_call_tgfFKO10EfK4xI3P4ci9kBpY': ['civic_docs'], 'var_call_R4XAkIbysGnUFFK0TcQb1VNg': 'file_storage/call_R4XAkIbysGnUFFK0TcQb1VNg.json'}

exec(code, env_args)

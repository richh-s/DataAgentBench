code = """import json, re
from pathlib import Path

path = Path(var_call_STc47Hfs7JDMpc3RELxloaMP)
recs = json.loads(path.read_text())

patterns = [
    re.compile(r"^\s*([A-Z][\w&'\-/()., ]+?)\s*\n\s*\(.*?\)\s*\n.*?\bBegin\s+(?:Construction|Design)\s*:\s*Spring\s+2022\b", re.IGNORECASE | re.MULTILINE | re.DOTALL),
    re.compile(r"^\s*([A-Z][\w&'\-/()., ]+?)\s*\n.*?\bBegin\s+(?:Construction|Design)\s*:\s*Spring\s+2022\b", re.IGNORECASE | re.MULTILINE | re.DOTALL),
]

projects = set()
for r in recs:
    text = r.get('text','')
    # restrict to relevant sections by searching for the schedule lines first
    for m in re.finditer(r"Begin\s+(?:Construction|Design)\s*:\s*Spring\s+2022", text, flags=re.IGNORECASE):
        start = max(0, text.rfind('\n\n', 0, m.start()))
        chunk = text[start:m.end()+200]
        name = None
        for pat in patterns:
            mm = pat.search(chunk)
            if mm:
                name = mm.group(1).strip()
                break
        if not name:
            # fallback: find nearest preceding non-empty line that looks like a project title
            pre = text[:m.start()].splitlines()
            for line in reversed(pre[-40:]):
                line=line.strip()
                if not line: 
                    continue
                if re.search(r"Project Schedule|Estimated Schedule|Updates|Project Description|Capital Improvement|Disaster Projects|Agenda Item", line, re.I):
                    continue
                if len(line) < 4 or len(line) > 120:
                    continue
                name=line
                break
        if name:
            # normalize spacing
            name = re.sub(r"\s+", " ", name)
            projects.add(name)

projects_list = sorted(projects)
print('__RESULT__:')
print(json.dumps({'projects_started_spring_2022': projects_list, 'count': len(projects_list)}, ensure_ascii=False))"""

env_args = {'var_call_STc47Hfs7JDMpc3RELxloaMP': 'file_storage/call_STc47Hfs7JDMpc3RELxloaMP.json'}

exec(code, env_args)

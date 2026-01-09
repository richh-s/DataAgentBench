code = """import json, re
from pathlib import Path

path = Path(var_call_STc47Hfs7JDMpc3RELxloaMP)
recs = json.loads(path.read_text())

pat = re.compile(r'^\s*([A-Z][\w&\'\-/()., ]+?)\s*\n.*?\bBegin\s+(?:Construction|Design)\s*:\s*Spring\s+2022\b', re.IGNORECASE | re.MULTILINE | re.DOTALL)

projects = set()
for r in recs:
    text = r.get('text','')
    for m in re.finditer(r'Begin\s+(?:Construction|Design)\s*:\s*Spring\s+2022', text, flags=re.IGNORECASE):
        prev_break = text.rfind('\n\n', 0, m.start())
        if prev_break == -1:
            prev_break = max(0, m.start()-500)
        chunk = text[prev_break:m.end()+200]
        mm = pat.search(chunk)
        if mm:
            name = re.sub(r'\s+', ' ', mm.group(1).strip())
            projects.add(name)
        else:
            pre_lines = text[:m.start()].splitlines()
            name = None
            for line in reversed(pre_lines[-60:]):
                line = line.strip()
                if not line:
                    continue
                if re.search(r'Project Schedule|Estimated Schedule|Updates|Project Description|Capital Improvement|Disaster Projects|Agenda Item|Page \d+ of \d+', line, re.I):
                    continue
                if len(line) < 4 or len(line) > 120:
                    continue
                name = re.sub(r'\s+', ' ', line)
                break
            if name:
                projects.add(name)

projects_list = sorted(projects)
print('__RESULT__:')
print(json.dumps({'projects_started_spring_2022': projects_list, 'count': len(projects_list)}, ensure_ascii=False))"""

env_args = {'var_call_STc47Hfs7JDMpc3RELxloaMP': 'file_storage/call_STc47Hfs7JDMpc3RELxloaMP.json'}

exec(code, env_args)

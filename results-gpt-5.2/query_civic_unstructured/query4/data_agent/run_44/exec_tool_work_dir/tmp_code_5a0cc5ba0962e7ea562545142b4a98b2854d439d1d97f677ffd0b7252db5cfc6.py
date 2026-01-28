code = """import json, re
from pathlib import Path

text = json.loads(Path(var_call_jYX42JPGN9j3efwnUYbgiC6p).read_text())[0]['text']

# Extract titles preceding 'Begin Construction: Spring 2022' or 'Begin Design: Spring 2022'
lines = text.splitlines()
projects = set()
for i, line in enumerate(lines):
    if re.search(r'Begin\s+(Construction|Design)\s*:\s*Spring\s+2022\b', line, re.I):
        # look back for the nearest plausible title line
        title = None
        for j in range(i-1, max(-1, i-80), -1):
            cand = lines[j].strip()
            if not cand:
                continue
            if re.search(r'Project Schedule|Estimated Schedule|Updates|Project Description|Capital Improvement|Disaster Projects|Agenda Item|Page \d+ of \d+|\(cid', cand, re.I):
                continue
            if ':' in cand and len(cand.split())<=3:
                continue
            if len(cand) < 4 or len(cand) > 120:
                continue
            title = cand
            break
        if title:
            projects.add(re.sub(r'\s+', ' ', title))

projects_list = sorted(projects)
print('__RESULT__:')
print(json.dumps({'projects': projects_list, 'count': len(projects_list)}, ensure_ascii=False))"""

env_args = {'var_call_STc47Hfs7JDMpc3RELxloaMP': 'file_storage/call_STc47Hfs7JDMpc3RELxloaMP.json', 'var_call_jYX42JPGN9j3efwnUYbgiC6p': 'file_storage/call_jYX42JPGN9j3efwnUYbgiC6p.json'}

exec(code, env_args)

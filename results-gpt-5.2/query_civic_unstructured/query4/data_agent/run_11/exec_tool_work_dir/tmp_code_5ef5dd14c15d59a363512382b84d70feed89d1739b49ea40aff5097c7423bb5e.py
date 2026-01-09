code = """import json, re
from pathlib import Path

path = Path(var_call_Xiaqyh7c6Gike1PzxA4xLEez)
docs = json.loads(path.read_text())

projects = set()

for d in docs:
    lines = d.get('text','').splitlines()
    for idx, line in enumerate(lines):
        if 'Begin Construction:' in line and 'Spring 2022' in line:
            # walk up to find nearest plausible project name line (not bullet, not schedule label)
            j = idx-1
            while j>=0:
                s = lines[j].strip()
                if not s:
                    j -= 1
                    continue
                if s.startswith('(cid:') or s.startswith('(cid:'):
                    j -= 1
                    continue
                if 'Project Schedule' in s or 'Estimated Schedule' in s or 'Updates' in s:
                    j -= 1
                    continue
                if s.startswith('Page ') or s.startswith('Agenda Item'):
                    j -= 1
                    continue
                # stop at first reasonable candidate
                projects.add(s)
                break

projects = sorted(projects)
print('__RESULT__:')
print(json.dumps({'projects': projects, 'count': len(projects)}))"""

env_args = {'var_call_TpPn0yAmA3vLsADt1sJwRJSb': ['Funding'], 'var_call_357DOrmSTlhzjregOEGXC2P6': ['civic_docs'], 'var_call_DQLKJrtf3yYi1VEkTJZXOohY': 'file_storage/call_DQLKJrtf3yYi1VEkTJZXOohY.json', 'var_call_Iw0tspcMNdI7eyL6QtP7EKU2': {'spring22_projects': ['(cid:131) Advertise: Spring 2022', '(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: January 2022', '(cid:131) Complete Design: March 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Complete Design: Winter 2021', '(cid:131) Complete Design: Winter 2021/2022'], 'count': 7}, 'var_call_Xiaqyh7c6Gike1PzxA4xLEez': 'file_storage/call_Xiaqyh7c6Gike1PzxA4xLEez.json'}

exec(code, env_args)

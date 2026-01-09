code = """import json, re
from pathlib import Path

p=Path(var_call_990QjnLpYNipFGlrpvba9P6S)
docs=json.loads(p.read_text())

results=[]
for d in docs:
    lines=d.get('text','').splitlines()
    for i,ln in enumerate(lines):
        if re.search(r'Construction was completed.*November 2022', ln, re.I):
            ctx_lines=[l.rstrip() for l in lines[max(0,i-15):min(len(lines),i+5)]]
            context='\n'.join(ctx_lines)
            results.append({'filename': d.get('filename'), 'context': context})

print('__RESULT__:')
print(json.dumps(results, ensure_ascii=False))"""

env_args = {'var_call_bj6z98fjH5u3abeSfc8CTfv8': ['Funding'], 'var_call_XhroUxAsfCyHp0eY88ACVcNh': ['civic_docs'], 'var_call_990QjnLpYNipFGlrpvba9P6S': 'file_storage/call_990QjnLpYNipFGlrpvba9P6S.json', 'var_call_J1ylmyIUyXF6iOhWBk1dyPNp': {'park_completed_2022': [], 'all_completed_2022': []}, 'var_call_UvwfRpanUXVlxQ3fZAtVWHQg': [], 'var_call_CNvRQISTZi4PJhObgN0UV6VM': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'line': 'draft plans are expected to be completed in early 2022. The Planning'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'line': 'started and is anticipated to be completed by the Spring of 2022.'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'line': 'draft plans are expected to be completed in early 2022. The Planning'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'line': 'completed by Spring 2022.'}, {'filename': 'malibucity_agenda__06222022-1919.txt', 'line': 'draft plans are expected to be completed in Spring 2022. The Planning'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed November 2022.'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed, November 2022'}, {'filename': 'malibucity_agenda__06282023-2116.txt', 'line': '(cid:131) Construction was completed November 2022'}, {'filename': 'malibucity_agenda__07272022-1939.txt', 'line': 'draft plans are expected to be completed in Spring 2022. The Planning'}, {'filename': 'malibucity_agenda__11102022-1995.txt', 'line': 'draft plans are expected to be completed in Winter 2022/23. The'}]}

exec(code, env_args)

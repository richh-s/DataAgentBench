code = """import json, re

res_path = var_call_8xwJ1pZLTA8JwRyCTw75Jdh2
with open(res_path, 'r', encoding='utf-8') as f:
    d = json.load(f)
projects_set = set(d['projects'])

pi_path = var_call_31RGmg6Il16HV6EVTB8T7ZVh
with open(pi_path, 'r', encoding='utf-8') as f:
    pi = json.load(f)

pat = re.compile(r'project\s+([^\s]+/[^\s]+).*?\b([0-9][0-9,]*)\s+forks', re.IGNORECASE)

rows = []
for rec in pi:
    s = rec.get('Project_Information') or ''
    m = pat.search(s)
    if not m:
        continue
    name = m.group(1).strip().rstrip('.,')
    forks = int(m.group(2).replace(',', ''))
    if name in projects_set:
        rows.append((name, forks))

rows.sort(key=lambda x: x[1], reverse=True)
top5 = rows[:5]

answer_lines = []
for i, (name, forks) in enumerate(top5, start=1):
    answer_lines.append(str(i) + '. ' + name + ' — ' + str(forks) + ' forks')
answer = '\n'.join(answer_lines) if answer_lines else 'No matching projects found.'

print('__RESULT__:')
print(json.dumps({'answer': answer, 'top5': [{'ProjectName': n, 'Forks': f} for n, f in top5], 'matched_count': len(rows)}))"""

env_args = {'var_call_IUrDFHuO1a8K3JIVdX8YuuV0': 'file_storage/call_IUrDFHuO1a8K3JIVdX8YuuV0.json', 'var_call_FvpxTPB9pEfLiDdGEELxBAle': 'file_storage/call_FvpxTPB9pEfLiDdGEELxBAle.json', 'var_call_8xwJ1pZLTA8JwRyCTw75Jdh2': 'file_storage/call_8xwJ1pZLTA8JwRyCTw75Jdh2.json', 'var_call_31RGmg6Il16HV6EVTB8T7ZVh': 'file_storage/call_31RGmg6Il16HV6EVTB8T7ZVh.json'}

exec(code, env_args)

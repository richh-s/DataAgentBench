code = """import json, re

res_path = var_call_8xwJ1pZLTA8JwRyCTw75Jdh2
with open(res_path, 'r', encoding='utf-8') as f:
    d = json.load(f)
projects_set = set(d['projects'])

pi_path = var_call_31RGmg6Il16HV6EVTB8T7ZVh
with open(pi_path, 'r', encoding='utf-8') as f:
    pi = json.load(f)

# more flexible extraction: find 'project <name>' and 'fork' count
name_pat = re.compile(r'project\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', re.IGNORECASE)
fork_pat = re.compile(r'([0-9][0-9,]*)\s+forks?', re.IGNORECASE)

rows = []
for rec in pi:
    s = rec.get('Project_Information') or ''
    nm = name_pat.search(s)
    fm = fork_pat.search(s)
    if not (nm and fm):
        continue
    name = nm.group(1)
    forks = int(fm.group(1).replace(',', ''))
    if name in projects_set:
        rows.append((name, forks))

rows.sort(key=lambda x: x[1], reverse=True)
top5 = rows[:5]

answer_lines = [str(i+1) + '. ' + name + ' — ' + str(forks) + ' forks' for i, (name, forks) in enumerate(top5)]
answer = "\\n".join(answer_lines) if answer_lines else 'No matching projects found.'

print('__RESULT__:')
print(json.dumps({'answer': answer, 'top5': [{'ProjectName': n, 'Forks': f} for n, f in top5], 'matched_count': len(rows)}))"""

env_args = {'var_call_IUrDFHuO1a8K3JIVdX8YuuV0': 'file_storage/call_IUrDFHuO1a8K3JIVdX8YuuV0.json', 'var_call_FvpxTPB9pEfLiDdGEELxBAle': 'file_storage/call_FvpxTPB9pEfLiDdGEELxBAle.json', 'var_call_8xwJ1pZLTA8JwRyCTw75Jdh2': 'file_storage/call_8xwJ1pZLTA8JwRyCTw75Jdh2.json', 'var_call_31RGmg6Il16HV6EVTB8T7ZVh': 'file_storage/call_31RGmg6Il16HV6EVTB8T7ZVh.json', 'var_call_7x6xNnIwJPMR3NkTP6WglvT4': {'answer': 'No matching projects found.', 'top5': [], 'matched_count': 0}}

exec(code, env_args)

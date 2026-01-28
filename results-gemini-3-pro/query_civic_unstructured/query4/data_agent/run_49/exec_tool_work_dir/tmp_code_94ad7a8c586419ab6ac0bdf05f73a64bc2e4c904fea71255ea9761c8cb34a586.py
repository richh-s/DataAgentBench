code = """import json

f_p = locals()['var_function-call-1003584179187242714']
c_p = locals()['var_function-call-1003584179187241629']

with open(f_p, 'r') as f:
    fd = json.load(f)
with open(c_p, 'r') as f:
    cd = json.load(f)

fd_map = {x['Project_Name'].lower().strip(): x for x in fd}
started = set()

for d in cd:
    txt = d['text']
    curr = None
    for line in txt.splitlines():
        ln = line.strip().lower()
        if not ln: continue
        
        if ln in fd_map:
            curr = fd_map[ln]['Project_Name']
            continue
        
        if curr:
            if 'begin construction' in ln or 'start' in ln:
                if 'spring 2022' in ln or 'march 2022' in ln or 'april 2022' in ln or 'may 2022' in ln:
                    started.add(curr)

total = 0
for p in started:
    total += int(fd_map[p.lower().strip()]['Amount'])

print('__RESULT__:')
print(json.dumps({'count': len(started), 'total_funding': total, 'projects': list(started)}))"""

env_args = {'var_function-call-1003584179187242714': 'file_storage/function-call-1003584179187242714.json', 'var_function-call-1003584179187241629': 'file_storage/function-call-1003584179187241629.json'}

exec(code, env_args)

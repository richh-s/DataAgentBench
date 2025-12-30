code = """import json

f_path = locals()['var_function-call-1003584179187242714']
c_path = locals()['var_function-call-1003584179187241629']

with open(f_path, 'r') as f:
    fd = json.load(f)
with open(c_path, 'r') as f:
    cd = json.load(f)

# Funding dict mapping lower case to original record
fd_dict = {}
for x in fd:
    fd_dict[x['Project_Name'].lower().strip()] = x

t_dates = ['spring 2022', 'march 2022', 'april 2022', 'may 2022']

started = set()
for d in cd:
    txt = d['text']
    curr = None
    for line in txt.split('\n'):
        ln = line.strip().lower()
        if not ln: continue
        
        # Check project name
        if ln in fd_dict:
            curr = fd_dict[ln]['Project_Name']
            continue
            
        if curr:
            # Check keywords
            if 'begin construction' in ln or 'start' in ln:
                # Check date
                for t in t_dates:
                    if t in ln:
                        started.add(curr)
                        break

amt = 0
real_map = {x['Project_Name']: x['Amount'] for x in fd}
for p in started:
    amt += int(real_map[p])

print('__RESULT__:')
print(json.dumps({'count': len(started), 'total_funding': amt, 'projects': list(started)}))"""

env_args = {'var_function-call-1003584179187242714': 'file_storage/function-call-1003584179187242714.json', 'var_function-call-1003584179187241629': 'file_storage/function-call-1003584179187241629.json'}

exec(code, env_args)

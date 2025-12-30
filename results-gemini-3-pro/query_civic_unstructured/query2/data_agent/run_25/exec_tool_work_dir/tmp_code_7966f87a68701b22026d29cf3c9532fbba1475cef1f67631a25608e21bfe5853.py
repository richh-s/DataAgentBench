code = """import json
import re

civic_docs = json.load(open(locals()['var_function-call-7157939871696024413']))
funding_data = json.load(open(locals()['var_function-call-17433077485285005998']))

full_text = chr(10).join([d['text'] for d in civic_docs])
lines = full_text.split(chr(10))

projects = []
current_project = None
current_block = []

pattern = re.compile(r'^\(cid:\d+\)')

for i in range(len(lines)):
    line = lines[i].strip()
    if not line: continue
    
    is_header = False
    if not pattern.match(line) and 'Page' not in line and 'Agenda Item' not in line:
        if i + 1 < len(lines):
            nxt = lines[i+1].strip()
            if '(cid:190)' in nxt or 'Updates:' in nxt or 'Project Description:' in nxt:
                is_header = True
            elif nxt == '' and i + 2 < len(lines):
                nxt2 = lines[i+2].strip()
                if '(cid:190)' in nxt2 or 'Updates:' in nxt2 or 'Project Description:' in nxt2:
                    is_header = True
    
    if is_header:
        if current_project:
            projects.append({'name': current_project, 'text': chr(10).join(current_block)})
        current_project = line
        current_block = []
    else:
        if current_project:
            current_block.append(line)

if current_project:
    projects.append({'name': current_project, 'text': chr(10).join(current_block)})

completed = []
for p in projects:
    nm = p['name']
    txt = p['text'].lower()
    
    if 'park' in nm.lower() or 'park' in txt:
        if 'completed' in txt and '2022' in txt:
            if re.search(r'completed.{1,50}2022', txt):
                completed.append(nm)
            elif re.search(r'complete construction.{1,50}2022', txt):
                completed.append(nm)

total = 0
found_projects = []
unique_p = list(set(completed))

for p_name in unique_p:
    c_name = p_name.strip().lower()
    p_total = 0
    matched = False
    for f in funding_data:
        f_name = f['Project_Name'].strip().lower()
        if f_name == c_name:
            p_total += int(f['Amount'])
            matched = True
    
    if matched:
        total += p_total
        found_projects.append(p_name)

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': found_projects}))"""

env_args = {'var_function-call-7157939871696024413': 'file_storage/function-call-7157939871696024413.json', 'var_function-call-17433077485285005998': 'file_storage/function-call-17433077485285005998.json'}

exec(code, env_args)

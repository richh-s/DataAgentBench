code = """import json

key_fund = 'var_function-call-1599065279211733274'
key_docs = 'var_function-call-1599065279211735013'

with open(locals()[key_fund], 'r') as f:
    funding = json.load(f)
with open(locals()[key_docs], 'r') as f:
    docs = json.load(f)

funded_names = set()
for x in funding:
    try:
        s = str(x.get('Amount', '0')).replace(',', '').replace('$', '')
        if float(s) > 50000:
            funded_names.add(x.get('Project_Name', '').strip())
    except:
        pass

design_names = set()
marker_start = 'Capital Improvement Projects (Design)'
markers_end = ['Capital Improvement Projects (Construction)', 'Agenda Item', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']

for d in docs:
    txt = d.get('text', '')
    idx = txt.find(marker_start)
    if idx < 0: continue
    
    sub = txt[idx + len(marker_start):]
    
    limit = len(sub)
    for m in markers_end:
        i = sub.find(m)
        if i >= 0 and i < limit:
            limit = i
    
    section = sub[:limit]
    lines = [l.strip() for l in section.split('\n') if l.strip()]
    
    for i in range(len(lines) - 1):
        line = lines[i]
        next_line = lines[i+1]
        
        is_title = False
        if 'Updates:' in next_line: is_title = True
        elif 'cid:' in next_line: is_title = True
        elif 'Project Schedule' in next_line: is_title = True
        elif 'Project Description' in next_line: is_title = True
        elif 'Staff is working' in next_line: is_title = True
        
        if is_title:
             if 'Updates' not in line and 'Page ' not in line:
                 design_names.add(line)

final = design_names.intersection(funded_names)
print('__RESULT__:')
print(json.dumps({'count': len(final), 'projects': list(final), 'extracted': list(design_names)}))"""

env_args = {'var_function-call-1599065279211733274': 'file_storage/function-call-1599065279211733274.json', 'var_function-call-1599065279211735013': 'file_storage/function-call-1599065279211735013.json'}

exec(code, env_args)

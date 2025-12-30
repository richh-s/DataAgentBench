code = """import json
import re
from datetime import datetime

funding_file = locals()['var_function-call-4778954659486180916']
docs_file = locals()['var_function-call-10827667462848878709']

with open(funding_file, 'r') as f:
    data = json.load(f)

high = set()
for r in data:
    try:
        if float(r['Amount']) > 50000:
            high.add(r['Project_Name'])
    except: pass

with open(docs_file, 'r') as f:
    docs = json.load(f)

tracker = {}
heads = {
    'Capital Improvement Projects (Design)': 'design',
    'Capital Improvement Projects (Construction)': 'construction',
    'Capital Improvement Projects (Not Started)': 'not started'
}
marks = [
    'Capital Improvement Projects (', 
    'Disaster Recovery Projects', 
    'Staff has also prepared', 
    'Agenda Item'
]

for doc in docs:
    fname = doc.get('filename', '')
    text = doc.get('text', '')
    
    m = re.search('(\\d{8})', fname)
    if not m: continue
    try:
        dt = datetime.strptime(m.group(1), '%m%d%Y')
    except: continue
    
    for h, s in heads.items():
        st = text.find(h)
        while st != -1:
            c_st = st + len(h)
            c_end = len(text)
            for mk in marks:
                idx = text.find(mk, c_st)
                if idx != -1 and idx < c_end:
                    c_end = idx
            
            c = text[c_st:c_end]
            lines = c.split('\n')
            for l in lines:
                ln = l.strip()
                if ln in high:
                    if ln not in tracker:
                        tracker[ln] = (dt, s)
                    else:
                        if dt >= tracker[ln][0]:
                            tracker[ln] = (dt, s)
            st = text.find(h, c_end)

cnt = 0
found = []
for n in tracker:
    if tracker[n][1] == 'design':
        cnt += 1
        found.append(n)

print('__RESULT__:')
print(json.dumps({'count': cnt, 'projects': found}))"""

env_args = {'var_function-call-4778954659486180916': 'file_storage/function-call-4778954659486180916.json', 'var_function-call-4778954659486182233': 'file_storage/function-call-4778954659486182233.json', 'var_function-call-10827667462848878709': 'file_storage/function-call-10827667462848878709.json'}

exec(code, env_args)

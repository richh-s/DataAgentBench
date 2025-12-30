code = """import json
import re
from datetime import datetime

funding_file = locals()['var_function-call-4778954659486180916']
docs_file = locals()['var_function-call-10827667462848878709']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

funding_high = set()
for r in funding_data:
    try:
        if float(r['Amount']) > 50000:
            funding_high.add(r['Project_Name'])
    except:
        pass

with open(docs_file, 'r') as f:
    docs = json.load(f)

project_tracker = {}

headers = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction",
    "Capital Improvement Projects (Not Started)": "not started"
}

markers = [
    "Capital Improvement Projects (", 
    "Disaster Recovery Projects", 
    "Staff has also prepared", 
    "Agenda Item"
]

for doc in docs:
    fname = doc.get('filename', '')
    text = doc.get('text', '')
    
    m = re.search(r"(\d{8})", fname)
    if not m: continue
    try:
        doc_date = datetime.strptime(m.group(1), "%m%d%Y")
    except: continue
    
    for header, status in headers.items():
        start = text.find(header)
        while start != -1:
            content_start = start + len(header)
            content_end = len(text)
            
            for m_str in markers:
                idx = text.find(m_str, content_start)
                if idx != -1 and idx < content_end:
                    content_end = idx
            
            content = text[content_start:content_end]
            
            lines = content.split('\n')
            for line in lines:
                ln = line.strip()
                if not ln: continue
                if ln in funding_high:
                    if ln not in project_tracker:
                        project_tracker[ln] = (doc_date, status)
                    else:
                        if doc_date >= project_tracker[ln][0]:
                            project_tracker[ln] = (doc_date, status)
            
            start = text.find(header, content_end)

count = 0
found = []
for name, (date, status) in project_tracker.items():
    if status == 'design':
        count += 1
        found.append(name)

print("__RESULT__:")
print(json.dumps({"count": count, "projects": found}))"""

env_args = {'var_function-call-4778954659486180916': 'file_storage/function-call-4778954659486180916.json', 'var_function-call-4778954659486182233': 'file_storage/function-call-4778954659486182233.json', 'var_function-call-10827667462848878709': 'file_storage/function-call-10827667462848878709.json'}

exec(code, env_args)

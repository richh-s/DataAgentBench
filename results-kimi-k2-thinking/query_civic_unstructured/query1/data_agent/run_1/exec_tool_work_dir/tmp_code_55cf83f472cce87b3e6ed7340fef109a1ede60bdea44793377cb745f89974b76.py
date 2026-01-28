code = """import json, re

funding_file = locals()['var_functions.query_db:0']
with open(funding_file) as f:
    funding_data = json.load(f)

civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_docs = json.load(f)

funding_map = {r['Project_Name']: int(r['Amount']) for r in funding_data if int(r['Amount']) > 50000}

design_projects = set()

for doc in civic_docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    sections = re.split(r'Capital Improvement Projects \(Design\)', text)
    if len(sections) < 2:
        continue
    
    design_text = sections[1].split('Capital Improvement Projects')[0]
    lines = design_text.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 10 or not line[0].isupper():
            continue
        
        keywords = ['Project', 'Improvements', 'Repair', 'Replacement', 'Road', 'Park']
        if not any(kw in line for kw in keywords):
            continue
        
        if line in funding_map:
            design_projects.add(line)
        else:
            for funded in funding_map:
                if line.startswith(funded) or funded.startswith(line.split('(')[0].strip()):
                    design_projects.add(funded)
                    break

print('__RESULT__:')
print(json.dumps({'count': len(design_projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)

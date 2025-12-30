code = """import json

# Access variables
funding_file = locals()['var_function_call_14956260562366733902']
docs_file = locals()['var_function_call_4179271317217180395']

with open(funding_file, 'r') as f:
    funding = json.load(f)

with open(docs_file, 'r') as f:
    docs = json.load(f)

# Funding set > 50k
funded = set()
for x in funding:
    try:
        if float(x['Amount']) > 50000:
            funded.add(x['Project_Name'].strip())
    except:
        pass

# Extract
extracted = set()
for doc in docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    active = False
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            active = True
            continue
        if 'Capital Improvement Projects' in line and '(Design)' not in line:
            active = False
            continue
        if 'Disaster Recovery Projects' in line:
            active = False
            continue
            
        if active:
            # Filters
            if not line or line.startswith('(') or 'Updates:' in line or 'Schedule:' in line or 'Page' in line or 'Agenda' in line:
                continue
            if 'Prepared by' in line or 'Approved by' in line:
                continue
            if len(line) < 5:
                continue
            extracted.add(line)

# Intersection
matches = [p for p in extracted if p in funded]
print('__RESULT__:')
print(json.dumps({'count': len(matches), 'matches': matches, 'extracted': list(extracted)}))"""

env_args = {'var_function-call-14956260562366733902': 'file_storage/function-call-14956260562366733902.json', 'var_function-call-4179271317217180395': 'file_storage/function-call-4179271317217180395.json'}

exec(code, env_args)

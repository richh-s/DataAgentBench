code = """import json

# Load funding data
with open('/tmp/tmp_results/query_db_2.json', 'r') as f:
    funding = json.load(f)

# Load civic documents  
with open('/tmp/tmp_results/query_db_6.json', 'r') as f:
    civic = json.load(f)

# Count funding records > $50,000
count_funding = sum(1 for item in funding if float(item['Amount']) > 50000)

# Extract potential project names from civic docs
project_names = set()
for doc in civic:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Find the design section and extract lines that look like project names
        lines = text.split('\n')
        in_design = False
        for line in lines:
            line = line.strip()
            if 'Capital Improvement Projects (Design)' in line:
                in_design = True
            elif 'Capital Improvement Projects (Construction)' in line:
                in_design = False
            
            if in_design and len(line) > 15:
                if 'FEMA' not in line and 'CalOES' not in line and 'fire' not in line:
                    if 'Page' not in line and 'Agenda' not in line:
                        if 'RECOMMENDED' not in line.upper():
                            project_names.add(line)

# Create mapping from funding
funding_names = {}
for item in funding:
    if float(item['Amount']) > 50000:
        name = item['Project_Name']
        funding_names[name] = float(item['Amount'])

# Count matches
count = 0
for name in project_names:
    if name in funding_names:
        count += 1

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)

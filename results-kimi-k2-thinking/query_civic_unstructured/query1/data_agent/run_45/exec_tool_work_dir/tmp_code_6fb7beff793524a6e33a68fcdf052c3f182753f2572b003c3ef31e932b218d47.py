code = """import json, re

# Get the funding data
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_list = json.load(f)

# Get the civic documents
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_list = json.load(f)

# Create funding dictionary for projects > 50000
fund_dict = {}
for item in funding_list:
    if float(item['Amount']) > 50000:
        fund_dict[item['Project_Name']] = float(item['Amount'])

# Find capital design projects in civic documents
design_projects = set()

for doc in civic_list:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        start = text.find('Capital Improvement Projects (Design)')
        segment = text[start:]
        end = segment.find('Capital Improvement Projects (Construction)')
        if end > 0:
            segment = segment[:end]
        
        for line in segment.split('\n'):
            line = line.strip()
            if len(line) > 15 and 'FEMA' not in line and 'CalOES' not in line:
                if 'Page' not in line and 'Agenda' not in line:
                    if 'RECOMMENDED' not in line.upper():
                        design_projects.add(line)

# Count matches
count = 0
for proj in design_projects:
    if proj in fund_dict:
        count += 1

print('__RESULT__')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)

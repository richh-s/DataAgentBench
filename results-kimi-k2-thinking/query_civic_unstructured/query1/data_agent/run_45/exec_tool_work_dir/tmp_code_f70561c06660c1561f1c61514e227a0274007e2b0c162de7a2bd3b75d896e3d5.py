code = """import json
import re

# Load data
with open('/tmp/tmp_results/query_db_2.json', 'r') as f:
    funding = json.load(f)

with open('/tmp/tmp_results/query_db_6.json', 'r') as f:
    civic = json.load(f)

# Build funding map for projects > 50000
funding_map = {}
for item in funding:
    amt = float(item['Amount'])
    if amt > 50000:
        name = item['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amt
        funding_map[clean] = amt

# Find capital design projects
cap_design = set()

for doc in civic:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        design_start = text.index('Capital Improvement Projects (Design)')
        construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start > design_start:
            design_section = text[design_start:construction_start]
        else:
            design_section = text[design_start:]
        
        for line in design_section.split('\n'):
            line = line.strip()
            if line and len(line) > 15 and not line.startswith('(') and 'Page' not in line and 'Agenda' not in line:
                if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line and 'fire' not in line:
                    if 'RECOMMENDED' not in line.upper() and 'Updates:' not in line and 'Schedule:' not in line and 'Capital Improvement Projects' not in line:
                        cap_design.add(line)

# Count matches
count = 0
for proj in cap_design:
    clean_proj = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in funding_map or clean_proj in funding_map:
        count += 1

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)

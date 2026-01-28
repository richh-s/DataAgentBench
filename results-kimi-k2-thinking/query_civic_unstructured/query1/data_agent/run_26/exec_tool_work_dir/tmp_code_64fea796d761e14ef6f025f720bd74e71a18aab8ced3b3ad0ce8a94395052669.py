code = """import json
import re

# Load funding data (> $50K projects)
funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    docs = json.load(f)

# Create funding lookup dictionary
funded = {}
for rec in funding:
    fund_name = rec['Project_Name'].strip().lower()
    funded[fund_name] = int(rec['Amount'])

# Extract design capital projects
design_capital = []
for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Find the design section
        design_start = text.index('Capital Improvement Projects (Design)')
        design_end = text.find('Capital Improvement Projects (Construction)', design_start)
        if design_end == -1:
            design_end = len(text)
        
        section = text[design_start:design_end]
        lines = section.split('\n')
        
        # Extract project names (lines followed by project metadata)
        for i in range(len(lines)):
            line = lines[i].strip()
            if line and len(line) > 5 and '▪' not in line and 'Updates:' not in line and 'Project Schedule:' not in line:
                if 'Capital Improvement' not in line and 'Page' not in line and 'RECOMMENDED' not in line:
                    if i + 1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                        design_capital.append(line.lower())

# Count projects funded over $50,000
count = sum(1 for proj in design_capital if proj in funded and funded[proj] > 50000)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)

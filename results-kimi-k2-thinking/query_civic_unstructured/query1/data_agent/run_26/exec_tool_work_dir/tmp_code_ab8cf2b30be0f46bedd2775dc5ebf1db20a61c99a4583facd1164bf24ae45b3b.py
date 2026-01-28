code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build lookup of funded projects
funded_projects = {}
for rec in funding_data:
    project_name = rec['Project_Name'].strip().lower()
    funded_projects[project_name] = int(rec['Amount'])

# Extract capital projects with design status
capital_design = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        design_start = text.find('Capital Improvement Projects (Design)')
        design_end = text.find('Capital Improvement Projects (Construction)', design_start)
        if design_end == -1:
            design_end = len(text)
        design_section = text[design_start:design_end]
        
        lines = design_section.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line and len(line) > 5:
                if '▪' not in line and 'Updates:' not in line and 'Project Schedule:' not in line:
                    if 'Capital Improvement' not in line and 'Page' not in line and 'RECOMMENDED' not in line:
                        if i + 1 < len(lines):
                            next_line = lines[i+1]
                            if 'Updates:' in next_line or 'Project Schedule:' in next_line:
                                capital_design.append(line.lower())

# Count projects with funding > $50,000
unique_projects = list(set(capital_design))
count_over_50000 = 0

for project in unique_projects:
    if project in funded_projects and funded_projects[project] > 50000:
        count_over_50000 += 1

print('__RESULT__:')
print(json.dumps(count_over_50000))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)

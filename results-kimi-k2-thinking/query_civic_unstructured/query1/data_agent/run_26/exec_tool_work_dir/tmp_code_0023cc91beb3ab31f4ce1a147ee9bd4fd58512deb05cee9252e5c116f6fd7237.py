code = """import json
import re
import os

# Load the funding data
funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:2

# Load JSON data from files
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_documents = json.load(f)

# Build lookup for funded projects (> $50,000)
funded_lookup = {}
for rec in funding_records:
    amount = int(rec['Amount'])
    if amount > 50000:
        project_name = rec['Project_Name'].strip().lower()
        funded_lookup[project_name] = amount

# Extract capital projects with design status from civic documents
design_projects = []
for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find capital improvement projects in design section
    design_section_start = text.find('Capital Improvement Projects (Design)')
    if design_section_start != -1:
        # Find end of design section
        design_section_end = text.find('Capital Improvement Projects (Construction)', design_section_start)
        if design_section_end == -1:
            design_section_end = len(text)
        
        design_section = text[design_section_start:design_section_end]
        lines = design_section.split('\n')
        
        # Extract project names - look for lines followed by project metadata
        for i in range(len(lines)):
            line = lines[i].strip()
            if line and len(line) > 5:
                # Skip control lines, bullets, and metadata
                if (not line.startswith('(') and not line.startswith('▪') and 
                    'Updates:' not in line and 'Project Schedule:' not in line and
                    'Estimated Schedule:' not in line and 'Project Description:' not in line and
                    'RECOMMENDED ACTION:' not in line and 'DISCUSSION:' not in line and
                    'Capital Improvement Projects' not in line and 'Page' not in line):
                    
                    # Check if this line is followed by project details
                    if i + 1 < len(lines):
                        next_line = lines[i+1].strip()
                        if ('Updates:' in next_line or 'Project Schedule:' in next_line or 
                            'Estimated Schedule:' in next_line):
                            design_projects.append(line.lower())

# Count unique design projects with funding > $50,000
unique_design_projects = list(set(design_projects))
count_over_50000 = 0

for project in unique_design_projects:
    if project in funded_lookup:
        count_over_50000 += 1

# Return the result as JSON
print('__RESULT__:')
print(json.dumps(count_over_50000))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0, 'var_functions.execute_python:72': {'funding': 'var_functions.query_db:0', 'civic': 'var_functions.query_db:2'}, 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)

code = """import json
import os

# Load funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_file = var_functions.query_db:1
with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

# Create mapping of project names to funding amounts
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

# Find capital projects with design status from civic docs
projects_in_design = []

for doc in civic_docs_data:
    if 'text' not in doc:
        continue
    
    text = doc['text']
    
    # Look for Capital Improvement Projects (Design) section
    if 'Capital Improvement Projects (Design)' in text:
        # Extract section content
        start_idx = text.index('Capital Improvement Projects (Design)') + len('Capital Improvement Projects (Design)')
        section_text = text[start_idx:]
        
        # Find end of section (look for next major heading or double newline)
        end_markers = ['\n\nCapital Improvement Projects (Construction)', 
                       '\n\nCapital Improvement Projects (Not Started)',
                       '\n\nDisaster Recovery Projects']
        
        end_idx = len(section_text)
        for marker in end_markers:
            if marker in section_text:
                end_idx = min(end_idx, section_text.index(marker))
        
        design_section = section_text[:end_idx]
        
        # Split into lines and look for project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines, bullet points, and markers
            if (not line or line.startswith('(') or line.startswith('-') or 
                line.startswith('•') or 'Updates' in line or 'Schedule' in line or
                'Complete Design' in line or 'Advertise' in line or 'Begin Construction' in line):
                continue
            
            # Check if this is a project name with funding > 50000
            if line in funding_map and funding_map[line] > 50000:
                projects_in_design.append({
                    'Project_Name': line,
                    'Amount': funding_map[line]
                })

# Remove duplicates
unique_projects = {}
for proj in projects_in_design:
    unique_projects[proj['Project_Name']] = proj

final_count = len(unique_projects)
project_names = sorted(list(unique_projects.keys()))

# Prepare result
result_dict = {
    'count': final_count,
    'projects': project_names
}

# Print in required format
print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)

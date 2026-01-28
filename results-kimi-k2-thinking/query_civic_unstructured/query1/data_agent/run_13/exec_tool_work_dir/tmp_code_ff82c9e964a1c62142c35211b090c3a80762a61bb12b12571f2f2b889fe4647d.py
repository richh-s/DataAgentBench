code = """import json
import re

# Load the funding data
def load_funding_data():
    funding_file = var_functions.query_db:0
    with open(funding_file, 'r') as f:
        return json.load(f)

funding_records = load_funding_data()
funding_project_names = [record['Project_Name'] for record in funding_records]

# Load civic documents
def load_civic_docs():
    civic_file = var_functions.query_db:5
    with open(civic_file, 'r') as f:
        return json.load(f)

civic_docs = load_civic_docs()

# Extract design projects from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find design section
    design_start = text.find('capital improvement projects (design)')
    if design_start == -1:
        continue
        
    # Find where design section ends
    construction_start = text.find('capital improvement projects (construction)', design_start)
    not_started_start = text.find('capital improvement projects (not started)', design_start)
    
    # Get the end position
    end_pos = construction_start
    if not_started_start > 0 and not_started_start < end_pos:
        end_pos = not_started_start
    if end_pos == -1:
        end_pos = len(text)
    
    design_section = text[design_start:end_pos]
    
    # Split into lines
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Skip lines that are status/schedule info
        skip_indicators = ['updates:', 'schedule:', 'advertise:', 'begin', 'complete:', 'project is', 'staff', 'city is', 'estimated schedule:', 'complete design:', 'final design:']
        if any(indicator in line for indicator in skip_indicators):
            continue
            
        # Skip document metadata lines
        if line.startswith(('to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'agenda', 'item', 'page', 'public works', 'commission', 'malibucity_agenda')):
            continue
            
        # Skip lines with special characters at start
        if line.startswith(('(', 'cid:')):
            continue
            
        # This looks like a project name
        project_name = line.strip().title()
        if project_name and project_name not in capital_design_projects:
            capital_design_projects.append(project_name)

# Match with funding data
matches = []
for design_project in capital_design_projects:
    # Clean design project name for matching
    clean_design = re.sub(r'\s*\([^)]+\)$', '', design_project).strip().lower()
    
    for funding_project in funding_project_names:
        clean_funding = re.sub(r'\s*\([^)]+\)$', '', funding_project).strip().lower()
        
        # Check for match
        if (design_project.lower() == clean_funding or
            clean_design == clean_funding or
            clean_design in clean_funding or
            clean_funding in clean_design):
            if design_project not in matches:
                matches.append(design_project)

# Count matches
count = len(matches)

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'matches': matches
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Access the civic documents data from storage
civic_docs_result = var_functions.query_db:5

# If the result is a file path string, read it
if isinstance(civic_docs_result, str) and civic_docs_result.endswith('.json'):
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
else:
    # Otherwise, use it directly
    civic_docs = civic_docs_result

print(f"Number of civic docs: {len(civic_docs)}")

# Extract all project information from the text
all_projects = []
for doc_index, doc in enumerate(civic_docs):
    text = doc.get('text', '')
    if not text:
        continue
        
    # Split by sections to find projects
    lines = text.split('\n')
    current_section = None
    current_project_type = 'capital'  # default
    
    # First, identify sections for disaster vs capital projects
    in_disaster_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if we're entering a disaster recovery section
        if 'DISASTER RECOVERY' in line.upper():
            in_disaster_section = True
            if '(Design)' in line:
                current_section = 'design'
            elif '(Construction)' in line:
                current_section = 'construction'
            elif '(Not Started)' in line:
                current_section = 'not_started'
            continue
            
        # Check if we're entering a capital improvement section
        if 'CAPITAL IMPROVEMENT' in line.upper():
            in_disaster_section = False
            if '(Design)' in line:
                current_section = 'design'
            elif '(Construction)' in line:
                current_section = 'construction'
            elif '(Not Started)' in line:
                current_section = 'not_started'
            continue
        
        # Look for project names - heuristic approach
        # Project names are typically:
        # - Not bullet points or special characters
        # - Not schedule/status lines
        # - Capitalized or mixed case (not all caps)
        # - Standalone lines
        if (current_section and 
            len(line) > 5 and
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('-') and 
            not line.startswith('▪') and
            not any(indicator in line.lower() for indicator in ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'project description:', 'estimated schedule:', 'project updates:', 'complete construction:']) and
            not line.isupper() and
            not line.lower().startswith('page') and
            not 'Agenda Item' in line and
            not line.startswith('cid:') and
            'PROJECTS' not in line.upper() and
            not any(status_word == line.lower() for status_word in ['design', 'construction', 'not started'])
            ):
            
            project_name = line.strip()
            
            # Additional cleanup
            # Remove common prefixes
            for prefix in ['·', '•', '-', '▪']:
                if project_name.startswith(prefix):
                    project_name = project_name[1:].strip()
            
            # Skip if it's just a date or page number
            if any(char.isdigit() for char in project_name) and len(project_name) < 15:
                # Might be a date like "03-22-23" or page reference
                continue
                
            # Skip common header/footer lines
            if any(phrase in project_name.lower() for phrase in ['public works', 'commission', 'agenda', 'report', 'meeting', 'prepared by', 'approved by', 'date prepared', 'subject']):
                continue
            
            project_type = 'disaster' if in_disaster_section else 'capital'
            
            all_projects.append({
                'Project_Name': project_name,
                'status': current_section,
                'type': project_type
            })

# Remove duplicates while preserving order
seen = set()
unique_projects = []
for proj in all_projects:
    key = (proj['Project_Name'], proj['status'], proj['type'])
    if key not in seen:
        seen.add(key)
        unique_projects.append(proj)

print(f"Extracted {len(unique_projects)} unique projects")
print("\nFirst 15 projects:")
for i, proj in enumerate(unique_projects[:15]):
    print(f"  {i+1}. {proj['Project_Name']} - status: {proj['status']}, type: {proj['type']}")

# Filter for capital projects with design status
 design_capital_projects = [p for p in unique_projects if p['type'] == 'capital' and p['status'] == 'design']

print(f"\nFound {len(design_capital_projects)} capital projects with design status:")
for proj in design_capital_projects:
    print(f"  - {proj['Project_Name']}")

# Save to proper JSON format
result = json.dumps(design_capital_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

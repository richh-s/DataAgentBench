code = """import json
import pandas as pd

# Load the civic documents data
civic_docs_path = var_functions.query_db:5
civic_docs_path = json.loads(civic_docs_path) if isinstance(civic_docs_path, str) else civic_docs_path

if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_path

print(f"Number of civic docs: {len(civic_docs)}")
print(f"First doc keys: {list(civic_docs[0].keys()) if civic_docs else 'No docs'}")

# Let's extract all project information from the text
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Split by sections to find projects
    lines = text.split('\n')
    current_section = None
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Look for section headers
        if 'Capital Improvement Projects (Design)' in line or 'Disaster Recovery Projects (Design)' in line:
            current_section = 'design'
        elif 'Capital Improvement Projects (Construction)' in line or 'Disaster Recovery Projects (Construction)' in line:
            current_section = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in line or 'Disaster Recovery Projects (Not Started)' in line:
            current_section = 'not_started'
        elif line.startswith('DISASTER RECOVERY PROJECTS') or 'Disaster Recovery Projects' in line:
            # Reset section context for disaster projects
            if '(Design)' in line:
                current_section = 'design'
            elif '(Construction)' in line:
                current_section = 'construction'
            elif '(Not Started)' in line:
                current_section = 'not_started'
        
        # Look for project names (lines that start with a project name, typically not bullet points)
        # This is a heuristic - project names are usually standalone lines not starting with special characters
        if (current_section and 
            line and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('-') and 
            not line.lower().startswith('updates:') and 
            not line.lower().startswith('project schedule:') and 
            not any(keyword in line.lower() for keyword in ['complete design:', 'advertise:', 'begin construction:', 'updates', 'project description', 'project updates']) and
            len(line) > 5 and  # Not too short
            not line.isupper()  # Not all caps (usually headers)
            ):
            
            # This looks like a project name
            project_name = line.strip()
            
            # Determine project type based on section header context
            project_type = 'capital'  # Default
            if 'DISASTER RECOVERY' in text.upper() and current_section:
                # If we're in a disaster recovery section
                section_start = text.find(line)
                disaster_section_start = text.find('DISASTER RECOVERY PROJECTS')
                if disaster_section_start > 0 and section_start > disaster_section_start:
                    # Find the end of disaster section
                    next_capital = text.find('CAPITAL IMPROVEMENT', disaster_section_start + 1)
                    if next_capital == -1 or section_start < next_capital:
                        project_type = 'disaster'
            
            # Clean up project name
            if '·' in project_name:
                project_name = project_name.split('·')[-1].strip()
            if '•' in project_name:
                project_name = project_name.split('•')[-1].strip()
            
            # Skip if it's just a status word
            if project_name.lower() in ['design', 'construction', 'not started', 'updates', 'project schedule']:
                continue
                
            all_projects.append({
                'Project_Name': project_name,
                'status': current_section,
                'type': project_type
            })

print(f"Extracted {len(all_projects)} projects")
for i, proj in enumerate(all_projects[:10]):
    print(f"  {i+1}. {proj['Project_Name']} - {proj['status']} - {proj['type']}")

# Save to JSON in proper format
result = json.dumps(all_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

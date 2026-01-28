code = """import json
import re
import os

# Get the file paths from storage
civic_docs_path = locals()['var_functions.query_db:16']
funding_data_path = locals()['var_functions.query_db:17']

# Read the data files
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded ' + str(len(civic_docs)) + ' civic documents')
print('Loaded ' + str(len(funding_data)) + ' funding records')

# Sample data
print('Sample civic doc keys: ' + str(list(civic_docs[0].keys())))
print('Sample funding record: ' + str(funding_data[0]))

# Now let's extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project information patterns
    # We need to find projects, their status, and completion dates
    
    # Pattern 1: "Construction was completed, [Date]"
    completed_pattern = r'Construction was completed[\s,]*([A-Za-z]+\s+\d{4})'
    completed_matches = re.findall(completed_pattern, text, re.IGNORECASE)
    
    # Pattern 2: "Complete Construction: [Date]"  
    complete_constr_pattern = r'Complete Construction:\s*([A-Za-z\d\s-]+\d{4})'
    complete_constr_matches = re.findall(complete_constr_pattern, text, re.IGNORECASE)
    
    # Pattern 3: Project names (common patterns)
    project_lines = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if (line and not line.startswith('(') and not line.startswith('•') and 
            len(line) > 10 and '.' not in line[:5] and 
            ('Project' not in line or len(line.split()) < 15)):
            # This might be a project name
            project_lines.append(line)
    
    if completed_matches or complete_constr_matches:
        # Look for what projects these completion dates refer to
        # Usually the project name is mentioned just before the completion statement
        
        # Find lines with both project names and completion info
        for line in lines:
            if 'completed' in line.lower() and '2022' in line:
                # Find project name (previous non-empty line)
                for i, prev_line in enumerate(reversed(lines[:lines.index(line)])):
                    if prev_line.strip() and not prev_line.startswith('('):
                        project_name = prev_line.strip()
                        # Clean up project name
                        if '•' in project_name:
                            project_name = project_name.split('•')[1].strip()
                        elif '◦' in project_name:
                            project_name = project_name.split('◦')[1].strip()
                        
                        projects.append({
                            'project_name': project_name,
                            'completion_date': '2022',
                            'source': filename
                        })
                        break

print('\nExtracted ' + str(len(projects)) + ' potential projects with completion info')
if projects:
    print('Sample extracted project: ' + str(projects[0]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)

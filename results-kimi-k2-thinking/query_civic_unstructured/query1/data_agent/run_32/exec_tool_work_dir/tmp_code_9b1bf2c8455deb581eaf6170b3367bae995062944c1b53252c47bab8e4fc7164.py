code = """import json
import re

# Read the civic documents data
civic_docs_path = var_functions.query_db:5
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
funding_path = var_functions.query_db:2
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Create a dictionary of funding amounts for easy lookup
funding_dict = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if amount > 50000:
        funding_dict[project_name] = amount

# Parse civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Split into sections for different project types and statuses
    # Look for capital projects with design status
    
    # Pattern to find project sections
    # Look for "Capital Improvement Projects (Design)" section
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)'
    
    design_match = re.search(design_section_pattern, text, re.DOTALL)
    
    if design_match:
        design_section = design_match.group(1)
        
        # Extract project names - they typically appear as bolded or on their own line
        # Look for patterns like project names followed by updates or schedules
        
        # Split by lines and look for project name patterns
        lines = design_section.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and common headers
            if not line or line in ['Capital Improvement Projects (Design)', 'Updates:', 'Project Schedule:']:
                i += 1
                continue
            
            # Look for project names - they usually don't start with bullet points or special chars
            # and are followed by project details
            if (line and 
                not line.startswith('(') and 
                not line.startswith('●') and 
                not line.startswith('•') and 
                not line.startswith('cid:') and
                not line.startswith('Complete Design:') and
                not line.startswith('Advertise:') and
                not line.startswith('Begin Construction:') and
                not line.startswith('Final Design:') and
                not line.startswith('Project is') and
                'Updates:' not in line and
                'Project Schedule:' not in line and
                len(line) > 5):
                
                # This might be a project name
                project_name = line
                
                # Clean up project name
                project_name = re.sub(r'\(cid:\d+\)', '', project_name).strip()
                
                # Check if this project has funding > 50000
                if project_name in funding_dict:
                    # Extract project details from following lines
                    details = []
                    j = i + 1
                    while j < len(lines) and not (lines[j].strip() and 
                                                   not lines[j].strip().startswith('(') and 
                                                   not lines[j].strip().startswith('●') and 
                                                   not lines[j].strip().startswith('•') and
                                                   not lines[j].strip().startswith('cid:') and
                                                   'Updates:' not in lines[j] and
                                                   'Project Schedule:' not in lines[j] and
                                                   len(lines[j].strip()) > 5 and
                                                   not 'Complete Design:' in lines[j] and
                                                   not 'Advertise:' in lines[j] and
                                                   not 'Begin Construction:' in lines[j]):
                        if lines[j].strip():
                            details.append(lines[j].strip())
                        j += 1
                    
                    # Add project to list
                    projects.append({
                        'Project_Name': project_name,
                        'type': 'capital',
                        'status': 'design',
                        'details': ' '.join(details),
                        'amount': funding_dict[project_name]
                    })
                
                # Skip to next potential project
                i = j
            else:
                i += 1

# Also check for other patterns that might indicate capital design projects
# Some projects might have "(Design)" in their name or be in other sections
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for any mention of projects with design status
    # Pattern: project name followed by "Design" status
    
    for project_name in funding_dict.keys():
        if project_name in text:
            # Check the context to see if it's a capital design project
            # Look for surrounding text
            idx = text.find(project_name)
            context_window = 500
            context_start = max(0, idx - context_window)
            context_end = min(len(text), idx + len(project_name) + context_window)
            context = text[context_start:context_end]
            
            # Check if it's mentioned as a capital project in design phase
            if ('design' in context.lower() or 'Design' in context) and not any(p['Project_Name'] == project_name for p in projects):
                # Check if it's a capital project (not disaster)
                is_capital = True
                if 'FEMA' in project_name or 'disaster' in context.lower():
                    is_capital = False
                
                if is_capital:
                    projects.append({
                        'Project_Name': project_name,
                        'type': 'capital',
                        'status': 'design',
                        'details': context[:200],  # First 200 chars of context
                        'amount': funding_dict[project_name]
                    })

# Remove duplicates
trimmed = []
seen = set()
for p in projects:
    if p['Project_Name'] not in seen:
        trimmed.append(p)
        seen.add(p['Project_Name'])

projects = trimmed

# Result
result = {
    'count': len(projects),
    'projects': projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

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
    
    # Try to find capital projects in design sections
    # Look for the design section header
    if 'Capital Improvement Projects (Design)' in text:
        # Get the section
        sections = text.split('Capital Improvement Projects (Design)')
        if len(sections) > 1:
            design_section = sections[1].split('Capital Improvement Projects (Construction)')[0]
            
            # Extract lines that look like project names
            lines = design_section.split('\n')
            current_project = None
            
            for line in lines:
                line = line.strip()
                
                # Skip empty lines and obvious non-project lines
                if not line or len(line) < 5:
                    continue
                
                # Skip lines with scheduling info
                skip_patterns = ['Complete Design:', 'Advertise:', 'Begin Construction:', 'Final Design:', 
                               'Project Schedule:', 'Updates:', 'cid:', '(cid:', '●', '•', 'Project is']
                
                should_skip = False
                for pattern in skip_patterns:
                    if pattern in line:
                        should_skip = True
                        break
                
                if should_skip:
                    continue
                
                # If we find a line with reasonable length and no special markers, it might be a project name
                if line and not line.startswith('(') and not line.startswith('●'):
                    # Clean up
                    clean_line = re.sub(r'\(cid:\d+\)', '', line).strip()
                    
                    # Check if this project has funding
                    if clean_line in funding_dict:
                        # Check if it's already in our list
                        if not any(p['Project_Name'] == clean_line for p in projects):
                            projects.append({
                                'Project_Name': clean_line,
                                'type': 'capital',
                                'status': 'design',
                                'amount': funding_dict[clean_line]
                            })

# Also do a broader search for any capital design projects that might be missed
# Check for project names that appear with design-related context
for project_name in funding_dict.keys():
    if any(project_name in p['Project_Name'] for p in projects):
        continue  # Already found
    
    for doc in civic_docs:
        text = doc.get('text', '')
        
        if project_name in text:
            # Look for design context
            idx = text.find(project_name)
            if idx >= 0:
                context_start = max(0, idx - 300)
                context_end = min(len(text), idx + len(project_name) + 300)
                context = text[context_start:context_end].lower()
                
                # Check if this is a design phase project and capital (not disaster)
                design_terms = ['design', 'complete design', 'final design']
                has_design = any(term in context for term in design_terms)
                
                # Check if it's capital (not disaster)
                is_disaster = 'fema' in project_name.lower() or 'disaster' in context
                is_capital = not is_disaster
                
                if has_design and is_capital:
                    projects.append({
                        'Project_Name': project_name,
                        'type': 'capital',
                        'status': 'design',
                        'amount': funding_dict[project_name]
                    })
                    break  # Found it, no need to check more docs

# Result - just get the count
count = len(projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Process funding data - convert amounts to integers
funding_projects = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    if amount > 50000:
        funding_projects[project_name] = {
            'amount': amount,
            'source': item['Funding_Source']
        }

# Extract projects with 'design' status from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for sections about Capital Improvement Projects in Design phase
    # Pattern: find lines that indicate design status
    
    # Split into lines for easier processing
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Check if we enter a design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design_section = True
            continue
            
        # Check if we leave the design section (next major section)
        if in_design_section and (line.startswith('Capital') or line.startswith('DISASTER') or line.startswith('Construction') or line.startswith('Not Started')):
            if 'Design' not in line:
                in_design_section = False
                continue
        
        # If we're in a design section, extract project names
        if in_design_section and line:
            # Skip metadata lines
            skip_keywords = ['Updates:', 'Schedule:', 'Complete', 'Advertise', 'Begin', 'Staff', 'City', 'Project', 'RECOMMENDED', 'DISCUSSION', 'cid:', '(cid', 'Page', 'Agenda', '---']
            should_skip = any(keyword in line for keyword in skip_keywords)
            
            # Also skip lines that are dates or phases
            if any(phase in line for phase in ['Spring', 'Summer', 'Fall', 'Winter', '2022', '2023', '2024']):
                should_skip = True
                
            if not should_skip and len(line) > 5 and len(line) < 150:
                # This looks like a project name
                clean_name = line.strip()
                # Remove common suffixes for matching
                base_name = re.sub(r'\s*\(.*\)$', '', clean_name)
                design_projects.add(base_name.strip())

# Debug: list some projects we found
print("Found design projects:", len(design_projects))
sorted_projects = sorted(list(design_projects))[:15]
for p in sorted_projects:
    print(f"  - {p}")

# Now match with funding data
capital_design_with_funding = []

for project_base_name in design_projects:
    # Look for matches in funding data
    for fund_name in funding_projects.keys():
        # Check for direct match or project name contained in funding name
        if project_base_name == fund_name or \
           fund_name.startswith(project_base_name + ' ') or \
           fund_name.startswith(project_base_name + '('):
            
            capital_design_with_funding.append({
                'project': project_base_name,
                'funding_amount': funding_projects[fund_name]['amount'],
                'funding_source': funding_projects[fund_name]['source']
            })
            break

# Count results
count = len(capital_design_with_funding)

print("__RESULT__:")
print(count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

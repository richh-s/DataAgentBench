code = """import json
import re

# Load funding data with Amount > 50000
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_file = var_functions.query_db:6
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections in the text
    # Pattern to find project names and their details
    # Common patterns in the documents:
    # - Project names are often followed by status information
    # - Status indicators like "(Design)", "(Construction)", "(Not Started)"
    # - Type indicators like "Capital Improvement Projects"
    
    # Split by lines to process each line
    lines = text.split('\n')
    
    current_project = None
    in_capital_section = False
    
    for line in lines:
        line = line.strip()
        
        # Check if we're in a Capital Improvement Projects section
        if 'Capital Improvement Projects' in line:
            in_capital_section = True
            continue
            
        # Check if we're leaving the capital section (look for other major sections)
        if 'Disaster Recovery Projects' in line or 'Public Works Commission' in line:
            in_capital_section = False
            continue
        
        # Look for project names (typically bold or start with special characters)
        # Pattern: lines that look like project names
        if in_capital_section and line and not line.startswith('(') and not line.startswith('•') and not line.startswith('○'):
            # Skip update/schedule lines
            if any(keyword in line.lower() for keyword in ['updates:', 'schedule:', 'advertise:', 'begin', 'complete', 'project description:', 'recommended action']):
                continue
            if any(keyword in line.lower() for keyword in ['staff is', 'city will', 'city submitted', 'city has', 'city is', 'consultant', 'project is']):
                continue
            if line.startswith('2022') or line.startswith('2023') or line.startswith('2024'):
                continue
                
            # Potential project name
            if len(line) > 10 and len(line) < 200:  # Reasonable length for project name
                # Check if next few lines contain status information
                project_name = line
                
                # Default values
                status = None
                project_type = "capital"
                
                # Look for status indicators in surrounding text
                context = text[text.find(line):text.find(line) + 500]
                
                if 'Design' in context or 'design' in line.lower():
                    status = "design"
                elif 'Construction' in context or 'construction' in line.lower():
                    status = "construction"
                elif 'Not Started' in context or 'not started' in line.lower():
                    status = "not started"
                elif 'Complete' in context or 'completed' in line.lower():
                    status = "completed"
                
                # Additional check: if line ends with status indicator
                if line.endswith('(Design)'):
                    status = "design"
                    project_name = line.replace('(Design)', '').strip()
                elif line.endswith('(Construction)'):
                    status = "construction"
                    project_name = line.replace('(Construction)', '').strip()
                elif line.endswith('(Not Started)'):
                    status = "not started"
                    project_name = line.replace('(Not Started)', '').strip()
                
                # If we found a status, add the project
                if status:
                    projects.append({
                        'Project_Name': project_name.strip(),
                        'status': status,
                        'type': project_type
                    })

# Also parse for explicit patterns like bullet points and project listings
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for patterns like "• Project Name - Status" or similar
    bullet_pattern = r'[•○]\s*([^•○\n]+?)(?:\(Design\)|\(Construction\)|\(Not Started\))'
    matches = re.findall(bullet_pattern, text, re.IGNORECASE)
    
    for match in matches:
        project_name = match.strip()
        if 'Design' in text[text.find(match):text.find(match) + 100]:
            projects.append({
                'Project_Name': project_name,
                'status': 'design',
                'type': 'capital'
            })

# Filter projects for design status and capital type
design_capital_projects = [p for p in projects if p['status'] == 'design' and p['type'] == 'capital']

# Get unique project names
unique_design_capital = {}
for p in design_capital_projects:
    name = p['Project_Name']
    if name not in unique_design_capital:
        unique_design_capital[name] = p

design_capital_names = list(unique_design_capital.keys())

# Filter funding data for projects in our design+capital list
funding_amounts = {item['Project_Name']: int(item['Amount']) for item in funding_data}

# Find matches between design/capital projects and funded projects
matched_projects = []
for design_project in design_capital_names:
    # Direct match
    if design_project in funding_amounts:
        matched_projects.append({
            'Project_Name': design_project,
            'Amount': funding_amounts[design_project]
        })
    else:
        # Fuzzy match - look for similar names
        for funded_name in funding_amounts.keys():
            # Check if one is a substring of the other
            if (design_project.lower() in funded_name.lower() or 
                funded_name.lower() in design_project.lower()):
                if abs(len(design_project) - len(funded_name)) < 30:  # Similar length
                    matched_projects.append({
                        'Project_Name': design_project,
                        'Amount': funding_amounts[funded_name],
                        'Matched_Funding_Name': funded_name
                    })
                    break

# Count projects with funding > 50000
count = sum(1 for p in matched_projects if p['Amount'] > 50000)

# Create detailed result
detailed_result = {
    'count': count,
    'projects': [{k: v for k, v in p.items() if k != 'Matched_Funding_Name'} for p in matched_projects if p['Amount'] > 50000]
}

# Print result
print("__RESULT__:")
print(json.dumps(detailed_result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

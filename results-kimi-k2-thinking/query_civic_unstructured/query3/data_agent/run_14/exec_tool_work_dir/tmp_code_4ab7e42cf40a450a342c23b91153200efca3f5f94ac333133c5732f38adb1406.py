code = """import json
import re

# Load funding data
with open(var_functions.query_db:1, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open(var_functions.query_db:4, 'r') as f:
    civic_docs = json.load(f)

# Print summary info for debugging
print(f"Total funding records: {len(funding_data)}")
print(f"Total civic documents: {len(civic_docs)}")

# Create a dictionary for quick lookup of funding info by project name
funding_dict = {item['Project_Name']: item for item in funding_data}

# Extract projects from civic documents
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections
    # Status categories
    status_patterns = [
        (r'Capital Improvement Projects \(Design\)', 'design'),
        (r'Capital Improvement Projects \(Construction\)', 'construction'),
        (r'Capital Improvement Projects \(Not Started\)', 'not started'),
        (r'Disaster Recovery Projects \(Design\)', 'design'),
        (r'Disaster Recovery Projects \(Construction\)', 'construction'),
        (r'Disaster Recovery Projects \(Not Started\)', 'not started'),
    ]
    
    # Find all project names in the text
    # Look for patterns like:
    # - Project names followed by Updates/Schedule
    # - Lines that start with capital letters and seem like project names
    
    lines = text.split('\n')
    current_status = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check for status section headers
        for pattern, status in status_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                current_status = status
                break
        
        # Look for project names (typically title case lines that are not headers)
        if (line and 
            not line.startswith('RECOMMENDED ACTION:') and
            not line.startswith('DISCUSSION:') and
            not line.startswith('To:') and
            not line.startswith('Prepared by:') and
            not line.startswith('Approved by:') and
            not line.startswith('Date prepared:') and
            not line.startswith('Meeting date:') and
            not line.startswith('Subject:') and
            not line.startswith('Public Works') and
            not line.startswith('Agenda Report') and
            not re.match(r'Page \d+ of \d+', line) and
            not re.match(r'Agenda Item #', line) and
            not re.match(r'cid:\d+', line) and
            not line.startswith('--') and
            not line.startswith('___') and
            len(line) > 5 and
            not line.isupper()):  # Not all uppercase
            
            # Check if this looks like a project name
            # Project names typically end with 'Project' or don't end with certain words
            if (re.match(r'^[A-Z][a-z]', line) or  # Starts with capital letter
                re.match(r'^\d{4} [A-Z]', line)):  # Or starts with year
                
                # Skip common non-project lines
                skip_terms = ['Updates:', 'Project Schedule:', 'Estimated Schedule:', 
                             'Complete Design:', 'Advertise:', 'Begin Construction:',
                             'Complete Construction:', 'Project Description:', 'Project Updates:',
                             'Staff has also prepared', 'City Council', 'The tool']
                
                should_skip = any(term in line for term in skip_terms)
                
                if not should_skip and len(line.split()) > 1:
                    project_name = line.strip()
                    
                    # Check if this project has funding
                    if project_name in funding_dict:
                        funding_info = funding_dict[project_name]
                        extracted_projects.append({
                            'Project_Name': project_name,
                            'Funding_Source': funding_info['Funding_Source'],
                            'Amount': funding_info['Amount'],
                            'Status': current_status
                        })

# Check for projects that have FEMA/emergency suffixes in their names
fema_related_projects = []
emergency_keywords = ['FEMA', 'emergency', 'warning', 'siren', 'fire', 'disaster', 'recovery']

for project in extracted_projects:
    project_name = project['Project_Name']
    
    # Check if project name contains FEMA/emergency related terms
    name_match = any(keyword.lower() in project_name.lower() for keyword in emergency_keywords)
    
    if name_match:
        fema_related_projects.append(project)

# Also check all funding records for projects with FEMA/emergency in name
for funding_item in funding_data:
    project_name = funding_item['Project_Name']
    name_match = any(keyword.lower() in project_name.lower() for keyword in emergency_keywords)
    
    if name_match:
        # Check if we already have status info
        existing = next((p for p in extracted_projects if p['Project_Name'] == project_name), None)
        if not existing:
            # Add without status
            fema_related_projects.append({
                'Project_Name': project_name,
                'Funding_Source': funding_item['Funding_Source'],
                'Amount': funding_item['Amount'],
                'Status': 'unknown'
            })
        elif not any(p['Project_Name'] == project_name for p in fema_related_projects):
            fema_related_projects.append(existing)

# Remove duplicates and sort
unique_projects = {}
for project in fema_related_projects:
    unique_projects[project['Project_Name']] = project

final_results = list(unique_projects.values())
final_results.sort(key=lambda x: x['Project_Name'])

print(f"Found {len(final_results)} emergency/FEMA related projects")
for p in final_results[:10]:  # Print first 10 for debugging
    print(f"  - {p['Project_Name']}: {p.get('Status', 'unknown')}")

# Prepare output
output = json.dumps(final_results, indent=2)

# Print in required format
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

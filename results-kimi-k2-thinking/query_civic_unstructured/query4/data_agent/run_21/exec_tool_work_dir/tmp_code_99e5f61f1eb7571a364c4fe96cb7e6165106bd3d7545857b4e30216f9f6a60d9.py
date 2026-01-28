code = """import json
import re

# Load funding data
funding_result = locals()['var_functions.query_db:12']
if isinstance(funding_result, str):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result

# Load civic documents
civic_result = locals()['var_functions.query_db:2']
if isinstance(civic_result, str):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

print("Data loaded successfully")
print(f"Funding records: {len(funding_records)}")
print(f"Civic documents: {len(civic_docs)}")

# Create a dictionary for funding lookup
funding_lookup = {}
for record in funding_records:
    proj_name = record['Project_Name'].strip()
    funding_lookup[proj_name] = {
        'amount': int(record['Amount']),
        'source': record['Funding_Source']
    }

print(f"Funding lookup created with {len(funding_lookup)} projects")

# Extract Spring 2022 projects from civic documents
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all project sections
    lines = text.split('\n')
    current_project = None
    project_start = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically bolded or title case lines)
        if line and len(line) > 5 and not line.startswith('(') and not line.startswith('•'):
            # Check if this looks like a project name
            if (line[0].isupper() or 'Project' in line) and len(line) < 150:
                # Check for project indicators
                has_project_indicators = any(word in line.lower() for word in [
                    'project', 'improvements', 'repairs', 'replacement', 'renovation',
                    'construction', 'installation', 'upgrades', 'development'
                ])
                
                # Exclude section headers
                excluded_terms = ['capital improvement', 'disaster recovery', 'status report', 
                                'recommended action', 'project schedule', 'project updates']
                is_section_header = any(term in line.lower() for term in excluded_terms)
                
                if has_project_indicators and not is_section_header:
                    current_project = line.replace('•', '').strip()
                    project_start = None
        
        # Look for Spring 2022 dates
        if current_project:
            # Check for Spring 2022 mentions
            spring_patterns = [
                r'Spring\s+2022',
                r'2022[-\s]Spring',
                r'2022[-\s]March',
                r'2022[-\s]April', 
                r'2022[-\s]May',
                r'March\s+2022',
                r'April\s+2022',
                r'May\s+2022'
            ]
            
            has_spring_2022 = any(re.search(pattern, line, re.IGNORECASE) for pattern in spring_patterns)
            
            if has_spring_2022:
                project_start = 'Spring 2022'
                # Check context - is this about start date or something else?
                if any(word in line.lower() for word in ['start', 'begin', 'commence', 'advertise', 'design', 'complete']):
                    spring_2022_projects.append({
                        'project_name': current_project,
                        'date_context': line,
                        'document': doc.get('filename', 'Unknown')
                    })
                    current_project = None  # Reset after finding a Spring 2022 date

print(f"\nFound {len(spring_2022_projects)} potential Spring 2022 projects in civic documents")

# Now match with funding data and extract unique projects
unique_spring_projects = {}

for proj in spring_2022_projects:
    proj_name = proj['project_name']
    
    # Direct match
    if proj_name in funding_lookup:
        unique_spring_projects[proj_name] = funding_lookup[proj_name]
    else:
        # Try fuzzy matching - check if funding project contains this name or vice versa
        for funding_proj, funding_info in funding_lookup.items():
            if (proj_name.lower() in funding_proj.lower() or 
                funding_proj.lower() in proj_name.lower()):
                unique_spring_projects[funding_proj] = funding_info
                break

print(f"Matched {len(unique_spring_projects)} unique projects with funding data")

# Calculate totals
total_projects = len(unique_spring_projects)
total_funding = sum(info['amount'] for info in unique_spring_projects.values())

# Show the projects
print(f"\n{'='*60}")
print(f"SPRING 2022 PROJECTS: {total_projects}")
print(f"TOTAL FUNDING: ${total_funding:,}")
print(f"{'='*60}")

for proj_name, info in unique_spring_projects.items():
    print(f"• {proj_name}: ${info['amount']:,} ({info['source']})")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records'}

exec(code, env_args)

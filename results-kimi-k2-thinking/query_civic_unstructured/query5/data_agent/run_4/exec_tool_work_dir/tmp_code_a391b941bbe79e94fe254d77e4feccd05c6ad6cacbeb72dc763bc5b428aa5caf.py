code = """import json
import re

# Load the civic documents from the file
civic_docs_path = locals()['var_functions.query_db:9']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_data = locals()['var_functions.query_db:5']

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# First, let's extract project information from civic documents
# We'll look for patterns that indicate disaster projects with start dates in 2022

disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project sections in the text
    # Common patterns: lines that start with project names, often followed by updates and schedules
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names - typically at the beginning of sections or as bullet points
        # Disaster projects often have (FEMA Project), (CalOES Project), or (CalJPIA Project) suffixes
        # Also check for keywords like "disaster", "fire", "FEMA", "CalOES", "CalJPIA"
        
        # Pattern 1: Project names with disaster suffixes
        if re.search(r'\((FEMA|CalOES|CalJPIA)\s+Project\)', line, re.IGNORECASE):
            # This is likely a disaster project
            current_project = line.strip()
            # Look for start date in following lines (st field)
            # Check next few lines for date information containing 2022
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].strip()
                if '2022' in next_line and any(keyword in next_line.lower() for keyword in ['begin', 'start', 'complete', 'design', 'advertise', 'construction']):
                    disaster_projects_2022.append({
                        'Project_Name': current_project,
                        'start_info': next_line,
                        'source': filename
                    })
                    break
        
        # Pattern 2: Check for disaster-related keywords in project name and date info
        elif any(keyword in line.lower() for keyword in ['disaster', 'fire', 'fema', 'emergency', 'woolsey']):
            current_project = line.strip()
            # Look for start date info
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].strip()
                if '2022' in next_line and any(keyword in next_line.lower() for keyword in ['begin', 'start', 'complete', 'design', 'advertise', 'construction']):
                    disaster_projects_2022.append({
                        'Project_Name': current_project,
                        'start_info': next_line,
                        'source': filename
                    })
                    break

print(f"Found {len(disaster_projects_2022)} potential disaster projects with 2022 dates")
for proj in disaster_projects_2022[:10]:
    print(f"  - {proj['Project_Name']}: {proj['start_info']}")

# Display all funding records for potential disaster projects
project_names = [proj['Project_Name'] for proj in disaster_projects_2022]

print("\nFunding records that might match:")
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    if any(disaster_proj in proj_name or proj_name in disaster_proj 
           for disaster_proj in project_names):
        print(f"  - {proj_name}: ${fund.get('Amount', 0)}")

# Now let's be more systematic - extract ALL projects from documents
# and identify disaster types based on broader patterns

all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project-like lines - often start with capital letters, not agenda items
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
            
        # Skip agenda sections and headers
        if line.startswith(('To:', 'From:', 'Date:', 'Subject:', 'Agenda', 'Page', 'Public Works', 'Commission', 'Item', 'RECOMMENDED', 'DISCUSSION')):
            continue
            
        # Skip lines that are just status labels
        if line in ['Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 
                   'Disaster Recovery Projects (Design)', 'Disaster Recovery Projects (Construction)', 'Disaster Recovery Projects (Not Started)']:
            continue
            
        # Look for potential project names (typically title case, not bullet points)
        if re.match(r'^[A-Z][A-Za-z\s&\-]{10,80}$', line):
            # Check if this looks like a project name
            project_name = line
            
            # Determine if it's disaster-related
            is_disaster = False
            if any(keyword in project_name.lower() for keyword in ['disaster', 'fema', 'caloes', 'caljpia', 'fire', 'emergency', 'recovery']):
                is_disaster = True
            elif re.search(r'\((FEMA|CalOES|CalJPIA)\s+Project\)', project_name, re.IGNORECASE):
                is_disaster = True
                
            if is_disaster:
                # Look for date info in following lines
                for j in range(i+1, min(i+6, len(lines))):
                    next_line = lines[j].strip()
                    if '2022' in next_line:
                        all_projects.append({
                            'Project_Name': project_name,
                            'start_info': next_line,
                            'type': 'disaster',
                            'source': doc.get('filename', '')
                        })
                        break

print(f"\nSystematically found {len(all_projects)} disaster projects")
for proj in all_projects[:10]:
    print(f"  - {proj['Project_Name']}")

# Save results for next step
disaster_projects_found = all_projects
print('\n__RESULT__:')
print(json.dumps(disaster_projects_found))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)

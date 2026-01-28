code = """import json
import re
from datetime import datetime

# Read the civic documents
with open('var_functions.query_db:14', 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
with open('var_functions.query_db:8', 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")


def extract_projects_from_text(text):
    """Extract project information from text"""
    projects = []
    
    # Look for project patterns - project name followed by updates and schedule
    # Project names are typically on their own line or followed by special characters
    lines = text.split('\n')
    
    current_project = None
    in_schedule_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Skip common headers/footers
        if any(x in line.lower() for x in ['page', 'agenda item', 'public works commission', 'capital improvement', 'disaster recovery']):
            continue
            
        # Look for project names (typically title case, not bullet points)
        if (len(line) > 5 and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('·') and
            not line.startswith('-') and
            not any(x in line.lower() for x in ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:']) and
            (line.istitle() or (sum(1 for c in line if c.isupper()) > len(line) * 0.3))):
            
            # Might be a project name
            project_name = line.strip()
            
            # Check if next few lines contain project info
            project_info = {
                'name': project_name,
                'status': None,
                'start_time': None,
                'end_time': None,
                'type': None,
                'topics': []
            }
            
            # Look ahead for status and schedule info
            for j in range(i+1, min(i+20, len(lines))):
                next_line = lines[j].strip()
                if not next_line:
                    continue
                    
                # Extract status from Updates section
                if 'Updates:' in next_line or 'updates:' in next_line:
                    # Look for status keywords
                    for k in range(j+1, min(j+10, len(lines))):
                        update_line = lines[k].strip()
                        if 'design' in update_line.lower():
                            project_info['status'] = 'design'
                            break
                        elif 'construction' in update_line.lower() or 'completed' in update_line.lower():
                            if 'completed' in update_line.lower():
                                project_info['status'] = 'completed'
                            else:
                                project_info['status'] = 'construction'
                            break
                        elif 'not started' in update_line.lower():
                            project_info['status'] = 'not started'
                            break
                            
                # Extract schedule information
                if 'Project Schedule:' in next_line or 'schedule:' in next_line.lower():
                    # Look for dates in the next few lines
                    for k in range(j+1, min(j+15, len(lines))):
                        schedule_line = lines[k].strip()
                        
                        # Look for Spring 2022 references
                        if re.search(r'2022[-\s](Spring|March|April|May|03|04|05)', schedule_line, re.IGNORECASE):
                            project_info['start_time'] = '2022-Spring'
                            break
                        elif 'Spring 2022' in schedule_line:
                            project_info['start_time'] = '2022-Spring'
                            break
                            
                # Determine project type based on name and content
                if any(word in project_name.lower() for word in ['fema', 'fire', 'disaster', 'recovery', 'woolsey']):
                    project_info['type'] = 'disaster'
                elif any(word in project_name.lower() for word in ['capital', 'infrastructure', 'improvement', 'road', 'bridge', 'park', 'drainage', 'storm drain', 'water', 'street']):
                    project_info['type'] = 'capital'
                    
                # Extract topics
                project_name_lower = project_name.lower()
                if 'park' in project_name_lower:
                    project_info['topics'].append('park')
                if 'road' in project_name_lower or 'street' in project_name_lower:
                    project_info['topics'].append('road')
                if 'drainage' in project_name_lower or 'storm drain' in project_name_lower:
                    project_info['topics'].append('drainage')
                if 'fema' in project_name_lower:
                    project_info['topics'].append('fema')
                if 'fire' in project_name_lower:
                    project_info['topics'].append('fire')
                    
            if project_info['name'] and len(project_info['name']) > 5:
                projects.append(project_info)
                
    return projects


# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc.get('text', ''))
    all_projects.extend(projects)

# Filter projects that started in Spring 2022
spring_2022_projects = []
for project in all_projects:
    if project.get('start_time') == '2022-Spring':
        spring_2022_projects.append(project)

print(f"\nFound {len(spring_2022_projects)} projects that started in Spring 2022:")
for proj in spring_2022_projects:
    print(f"- {proj['name']}: status={proj['status']}, type={proj['type']}")

# Find matching funding for these projects
matching_funding = []
for project in spring_2022_projects:
    project_name = project['name']
    
    # Look for exact matches and close matches
    for fund in funding_data:
        fund_project_name = fund.get('Project_Name', '')
        
        # Exact match
        if fund_project_name == project_name:
            matching_funding.append({
                'project_name': project_name,
                'funding_id': fund.get('Funding_ID'),
                'funding_source': fund.get('Funding_Source'),
                'amount': int(fund.get('Amount', 0))
            })
        # Partial match - check if project name is contained in funding project name
        elif project_name in fund_project_name or fund_project_name in project_name:
            if len(project_name) > 10:  # Avoid very short partial matches
                matching_funding.append({
                    'project_name': fund_project_name,
                    'matched_project': project_name,
                    'funding_id': fund.get('Funding_ID'),
                    'funding_source': fund.get('Funding_Source'),
                    'amount': int(fund.get('Amount', 0))
                })

print(f"\nFound {len(matching_funding)} funding matches")

# Sum up total funding
total_funding = sum(f['amount'] for f in matching_funding)

print(f"\nTotal Spring 2022 projects: {len(spring_2022_projects)}")
print(f"Total funding: ${total_funding:,}")

print(f"\nSpring 2022 Projects details:")
for proj in spring_2022_projects:
    print(f"  - {proj['name']} (Status: {proj['status']}, Type: {proj['type']})")

print(f"\nFunding matches:")
for fund in matching_funding[:10]:  # Show first 10
    print(f"  - {fund['project_name']}: ${fund['amount']:,}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

code = """import json
import re

# Read the civic documents
with open('var_functions.query_db:14', 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
with open('var_functions.query_db:8', 'r') as f:
    funding_data = json.load(f)

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding_data), 'funding records')


def extract_projects_from_text(text):
    """Extract project information from text"""
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
            
        # Skip headers and footers
        skip_keywords = ['page', 'agenda item', 'public works commission', 'capital improvement', 'disaster recovery']
        if any(x in line.lower() for x in skip_keywords):
            continue
            
        # Look for project names - lines that are mostly title case and not bullet points
        if (not line.startswith(('(', '·', '-', '•')) and 
            not any(x in line.lower() for x in ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'estimated schedule:']) and
            (line.istitle() or sum(1 for c in line if c.isupper()) > len(line) * 0.3)):
            
            project_name = line.strip()
            
            # Skip if it's just a section header
            if project_name in ['Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
                continue
                
            project_info = {
                'name': project_name,
                'status': None,
                'start_time': None,
                'type': None,
                'topics': []
            }
            
            # Look ahead for project details
            for j in range(i+1, min(i+30, len(lines))):
                next_line = lines[j].strip()
                if not next_line:
                    continue
                
                # Find status
                if 'Updates:' in next_line:
                    for k in range(j+1, min(j+15, len(lines))):
                        update_line = lines[k].strip().lower()
                        if 'design' in update_line:
                            project_info['status'] = 'design'
                            break
                        elif 'construction' in update_line:
                            project_info['status'] = 'construction'
                            break
                        elif 'completed' in update_line:
                            project_info['status'] = 'completed'
                            break
                        elif 'not started' in update_line:
                            project_info['status'] = 'not started'
                            break
                
                # Find schedule with Spring 2022
                if 'Schedule:' in next_line or next_line.startswith('Project Schedule:'):
                    for k in range(j+1, min(j+15, len(lines))):
                        schedule_line = lines[k].strip()
                        if re.search(r'2022[-\s](Spring|March|April|May|03|04|05)', schedule_line, re.I) or 'Spring 2022' in schedule_line:
                            project_info['start_time'] = '2022-Spring'
                            break
                
                # Determine type
                name_lower = project_name.lower()
                if any(word in name_lower for word in ['fema', 'fire', 'woolsey']):
                    project_info['type'] = 'disaster'
                elif any(word in name_lower for word in ['road', 'bridge', 'park', 'street', 'drainage', 'storm', 'water', 'infrastructure']):
                    project_info['type'] = 'capital'
                
                # Extract topics
                if 'park' in name_lower:
                    project_info['topics'].append('park')
                if 'road' in name_lower or 'street' in name_lower:
                    project_info['topics'].append('road')
                if 'drainage' in name_lower or 'storm' in name_lower:
                    project_info['topics'].append('drainage')
                if 'fema' in name_lower:
                    project_info['topics'].append('fema')
            
            if len(project_info['name']) > 10:  # Filter out short lines
                projects.append(project_info)
    
    return projects


# Extract all projects
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc.get('text', ''))
    all_projects.extend(projects)

# Filter for Spring 2022 projects
spring_2022_projects = [p for p in all_projects if p.get('start_time') == '2022-Spring']

print('Found', len(spring_2022_projects), 'Spring 2022 projects')
for proj in spring_2022_projects:
    print('-', proj['name'], 'Status:', proj['status'], 'Type:', proj['type'])

# Find funding matches
matching_funds = []
total_funding = 0

for project in spring_2022_projects:
    project_name = project['name']
    
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '')
        
        # Check for match (exact or project name contained in fund name)
        if (fund_name == project_name or 
            project_name in fund_name or 
            (len(project_name) > 15 and any(word in fund_name for word in project_name.split()[:3]))):
            
            amount = int(fund.get('Amount', 0))
            matching_funds.append({
                'project': project_name,
                'fund_name': fund_name,
                'amount': amount
            })
            total_funding += amount
            break  # Avoid double counting

print('\nFunding matches found for', len(matching_funds), 'projects')
print('Total funding:', total_funding)

print('\nDetailed matches:')
for match in matching_funds:
    print('-', match['project'], '->', match['fund_name'], ':', match['amount'])

result = {
    'project_count': len(spring_2022_projects),
    'total_funding': total_funding,
    'projects': spring_2022_projects,
    'funding_matches': matching_funds
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

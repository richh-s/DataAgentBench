code = """import json
import re

# Load the funding data
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the civic docs text data
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Process funding data into a dictionary for easy lookup
funding_dict = {}
for record in funding_data:
    funding_dict[record['Project_Name']] = {
        'Funding_ID': record['Funding_ID'],
        'Funding_Source': record['Funding_Source'],
        'Amount': int(record['Amount'])
    }

# Function to extract project information from civic doc text
def extract_projects_from_text(text_content):
    projects = []
    
    # Look for project sections in the text
    # Project names are typically followed by updates and schedules
    lines = text_content.split('\n')
    
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        
        # Look for project name headers (typically bold or all caps, or with specific markers)
        # Pattern: Project name followed by updates or schedule
        if (line and 
            not line.startswith('(') and 
            not line.startswith('-') and 
            len(line) > 5 and
            not any(keyword in line.lower() for keyword in ['agenda', 'report', 'meeting', 'item', 'to:', 'prepared by:', 'approved by:', 'date:', 'subject:', 'recommended action:', 'discussion:'])):
            
            # Check if this line looks like a project name
            if (any(word.isupper() for word in line.split()[:3]) or 
                line.startswith('20') or  # Years often start project names
                'Project' in line or
                'Park' in line):
                
                # Save previous project if exists
                if current_project and 'Project_Name' in project_info:
                    projects.append(project_info)
                
                # Start new project
                current_project = line
                project_info = {
                    'Project_Name': line,
                    'topic': '',
                    'status': '',
                    'st': '',
                    'et': ''
                }
        
        # Extract status information
        if current_project:
            # Look for completion mentions
            if any(phrase in line for phrase in ['completed', 'completion', 'Construction was completed']):
                if '2022' in line or 'November 2022' in line or 'January 2023' in line:
                    project_info['status'] = 'completed'
                    project_info['et'] = '2022'
            
            # Look for topics - park-related keywords
            if 'Park' in line:
                project_info['topic'] = 'park'
            elif 'park' in line.lower():
                if project_info['topic']:
                    project_info['topic'] += ', park'
                else:
                    project_info['topic'] = 'park'
    
    # Add the last project if exists
    if current_project and 'Project_Name' in project_info:
        projects.append(project_info)
    
    return projects

# Extract all projects from civic documents
all_projects = []
for doc in civic_data:
    if 'text' in doc:
        projects = extract_projects_from_text(doc['text'])
        all_projects.extend(projects)

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for project in all_projects:
    # Check if it's park-related
    is_park = 'park' in project['topic'].lower()
    
    # Check if it's completed in 2022
    is_completed_2022 = (project['status'] == 'completed' and 
                        ('2022' in project.get('et', '') or 
                         '2022' in project.get('st', '')))
    
    if is_park and is_completed_2022:
        project_name = project['Project_Name']
        
        # Look for matching funding
        for fund_name, fund_info in funding_dict.items():
            # Simple name matching (case-insensitive, strip whitespace)
            if (project_name.strip().lower() in fund_name.strip().lower() or
                fund_name.strip().lower() in project_name.strip().lower()):
                
                # Check if already exists to avoid duplicates
                existing = next((p for p in park_projects_2022 if p['Project_Name'] == fund_name), None)
                if not existing:
                    project_with_funding = {
                        'Project_Name': fund_name,
                        'status': 'completed',
                        'year': '2022',
                        'Funding_Source': fund_info['Funding_Source'],
                        'Amount': fund_info['Amount']
                    }
                    park_projects_2022.append(project_with_funding)
                break

# Also check for projects that have park keywords in their names directly
park_keywords = ['park', 'playground']
for fund_name, fund_info in funding_dict.items():
    # Check if fund_name contains park keywords
    has_park = any(keyword in fund_name.lower() for keyword in park_keywords)
    
    if has_park:
        # Look for status in civic docs
        for project in all_projects:
            if (fund_name.strip().lower() in project['Project_Name'].strip().lower() or
                project['Project_Name'].strip().lower() in fund_name.strip().lower()):
                
                is_completed_2022 = (project['status'] == 'completed' and 
                                   ('2022' in project.get('et', '') or 
                                    '2022' in project.get('st', '')))
                
                if is_completed_2022:
                    existing = next((p for p in park_projects_2022 if p['Project_Name'] == fund_name), None)
                    if not existing:
                        project_with_funding = {
                            'Project_Name': fund_name,
                            'status': 'completed',
                            'year': '2022',
                            'Funding_Source': fund_info['Funding_Source'],
                            'Amount': fund_info['Amount']
                        }
                        park_projects_2022.append(project_with_funding)
                    break

# Calculate total funding
total_funding = sum(project['Amount'] for project in park_projects_2022)

# Format results
result = {
    'total_funding': total_funding,
    'project_count': len(park_projects_2022),
    'projects': park_projects_2022
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

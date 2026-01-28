code = """import json
import re

# Get the file paths from storage
civic_docs_path = var_functions.query_db:5
funding_path = var_functions.query_db:20

# Load civic documents
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create a dictionary for funding lookup
funding_dict = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    if project_name in funding_dict:
        funding_dict[project_name] += amount
    else:
        funding_dict[project_name] = amount

# Function to extract projects from civic document text
def extract_projects_from_text(text):
    projects = []
    
    # Look for project name patterns - typically bold/underline or all caps or title case
    # Look for sections that start with project names, followed by updates and schedules
    lines = text.split('\n')
    
    current_project = None
    in_schedule_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names - they're often standalone lines that look like titles
        # Check if line looks like a project name (not a section header like "Capital Improvement Projects")
        if (len(line) < 100 and 
            not line.isupper() and  # Not all caps (likely a section header)
            not line.endswith(':') and  # Not a label
            not line.startswith('(') and  # Not a bullet point continuation
            'Project' not in line and  # Not a category header
            'Projects' not in line and
            'Schedule' not in line and
            'Updates' not in line and
            'To:' not in line and
            'From:' not in line and
            'Subject:' not in line and
            'Page' not in line):
            
            # This might be a project name, check if next lines contain updates or schedule
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if 'Updates:' in next_line or 'Project Schedule:' in next_line or '(cid:' in next_line:
                    if current_project:
                        projects.append(current_project)
                    current_project = {'name': line, 'start_dates': []}
                    continue
        
        # If we're in a project section, look for dates
        if current_project:
            # Look for schedule items with dates
            if 'Project Schedule:' in line or 'Estimated Schedule:' in line:
                in_schedule_section = True
                continue
            
            if in_schedule_section:
                # Look for date patterns like "Begin Construction: Fall 2023", "Complete Design: Summer 2023"
                date_match = re.search(r'(?:Begin|Start|Construction|Design|Advertise|Complete)[\s\w]*:\s*([A-Za-z\s]+(?:\d{4}|\d{2}))', line, re.IGNORECASE)
                if date_match:
                    date_str = date_match.group(1).strip()
                    current_project['start_dates'].append(date_str)
                
                # If we hit a blank line or new section, reset
                if line.isupper() and ('PROJECT' in line or 'CAPITAL' in line or 'DISASTER' in line):
                    in_schedule_section = False
                    projects.append(current_project)
                    current_project = None
    
    if current_project:
        projects.append(current_project)
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

# Filter for Spring 2022 projects
spring_2022_projects = []
for project in all_projects:
    for date_str in project['start_dates']:
        # Check if it's Spring 2022
        if '2022' in date_str:
            # Check for Spring indicators (March, April, May, Spring)
            spring_indicators = ['Spring', 'March', 'April', 'May', 'Mar', 'Apr', 'May']
            if any(indicator.lower() in date_str.lower() for indicator in spring_indicators):
                spring_2022_projects.append(project['name'])
                break

# Get unique project names
unique_spring_2022_projects = list(set(spring_2022_projects))

# Find funding for these projects
project_funding = {}
for project_name in unique_spring_2022_projects:
    # Look for exact matches and partial matches
    for funded_project in funding_dict:
        if project_name.lower() in funded_project.lower() or funded_project.lower() in project_name.lower():
            if project_name in project_funding:
                project_funding[project_name] += funding_dict[funded_project]
            else:
                project_funding[project_name] = funding_dict[funded_project]

# Calculate totals
total_projects = len(project_funding)
total_funding = sum(project_funding.values())

print("__RESULT__:")
print(json.dumps({
    "total_projects": total_projects,
    "total_funding": total_funding,
    "project_details": project_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'num_civic_docs': 5, 'num_funding_records': 500}}

exec(code, env_args)

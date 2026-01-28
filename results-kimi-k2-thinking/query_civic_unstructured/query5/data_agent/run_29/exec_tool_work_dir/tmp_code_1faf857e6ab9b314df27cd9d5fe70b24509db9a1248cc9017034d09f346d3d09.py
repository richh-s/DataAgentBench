code = """import json
import re

# Read the MongoDB data from the file
with open('/tmp/tmp9q1f0j8y.json', 'r') as f:
    civic_docs = json.load(f)

# Read the funding data from the file
with open('/tmp/tmphg9s8x_1.json', 'r') as f:
    funding_data = json.load(f)

# Function to extract projects from text
# The text format seems to have project names followed by updates and schedules

def extract_projects_from_text(text):
    projects = []
    
    # Look for patterns that indicate project names and their details
    # Projects often start with a name and then have sections like "Updates:" and "Project Schedule:"
    
    # First, let's look for disaster-related indicators
    disaster_indicators = ['FEMA', 'CalJPIA', 'CalOES', 'fire', 'disaster', 'emergency']
    
    # Split text into lines for easier parsing
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for potential project names (typically not indented, followed by updates/schedule)
        # Skip empty lines and common headers
        if (line and 
            not line.startswith('Public Works') and 
            not line.startswith('Commission') and
            not line.startswith('Agenda') and
            not line.startswith('To:') and
            not line.startswith('Prepared') and
            not line.startswith('Approved') and
            not line.startswith('Date') and
            not line.startswith('Meeting') and
            not line.startswith('Subject:') and
            not line.startswith('RECOMMENDED') and
            not line.startswith('DISCUSSION:') and
            not line.startswith('Capital Improvement') and
            not line.startswith('Page') and
            not line.startswith('(') and  # Skip bullet points
            not line.startswith('•') and
            not line.startswith('●') and
            'cid:' not in line):
            
            # This might be a project name
            # Check if next few lines contain updates or schedule
            has_updates = False
            has_schedule = False
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].strip()
                if 'Updates:' in next_line or 'Updates' in next_line:
                    has_updates = True
                if 'Schedule:' in next_line or 'Project Schedule:' in next_line:
                    has_schedule = True
                    
            if has_updates or has_schedule:
                # This is likely a project name
                project_name = line
                
                # Determine if it's a disaster project
                is_disaster = any(indicator.lower() in project_name.lower() for indicator in disaster_indicators)
                
                # Look for date information in subsequent lines
                start_date = None
                end_date = None
                status = None
                
                # Search for schedule information
                for j in range(i+1, min(i+15, len(lines))):
                    schedule_line = lines[j].strip()
                    
                    # Look for completion dates, start dates
                    if 'Complete Design:' in schedule_line or 'Complete Construction:' in schedule_line:
                        # Extract date
                        date_match = re.search(r'(\d{4}|Spring \d{4}|Summer \d{4}|Fall \d{4}|Winter \d{4}|\d{4}-[A-Za-z]+)', schedule_line)
                        if date_match:
                            end_date = date_match.group(1)
                    
                    if 'Begin Construction:' in schedule_line or 'Advertise:' in schedule_line:
                        date_match = re.search(r'(\d{4}|Spring \d{4}|Summer \d{4}|Fall \d{4}|Winter \d{4}|\d{4}-[A-Za-z]+)', schedule_line)
                        if date_match:
                            start_date = date_match.group(1)
                    
                    # Determine status based on context
                    if 'Project is currently under construction' in schedule_line:
                        status = 'construction'
                    elif 'not started' in schedule_line.lower():
                        status = 'not started'
                    elif 'design' in schedule_line.lower() and 'complete' not in schedule_line.lower():
                        status = 'design'
                    elif 'completed' in schedule_line.lower():
                        status = 'completed'
                
                # If project name contains FEMA/CalJPIA/CalOES, mark as disaster
                project_type = 'disaster' if is_disaster else 'capital'
                
                projects.append({
                    'Project_Name': project_name,
                    'type': project_type,
                    'topic': 'disaster' if is_disaster else '',
                    'status': status,
                    'st': start_date,
                    'et': end_date
                })
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

# Filter for disaster projects with start dates containing 2022
disaster_projects_2022 = []
for proj in all_projects:
    if proj['type'] == 'disaster' and proj['st'] and '2022' in proj['st']:
        disaster_projects_2022.append(proj)

# Create a lookup for project funding
funding_lookup = {f['Project_Name'].lower(): int(f['Amount']) for f in funding_data}

# Find matching funding for disaster projects that started in 2022
total_funding = 0
matched_projects = []

for proj in disaster_projects_2022:
    proj_name = proj['Project_Name']
    proj_name_lower = proj_name.lower()
    
    # Try exact match first
    if proj_name_lower in funding_lookup:
        amount = funding_lookup[proj_name_lower]
        total_funding += amount
        matched_projects.append({
            'project': proj_name,
            'amount': amount,
            'start_date': proj['st']
        })
    else:
        # Try partial matching - look for projects containing this name or vice versa
        for funding_name, amount in funding_lookup.items():
            if (proj_name_lower in funding_name or funding_name in proj_name_lower):
                # Additional check: ensure it's the same project type
                if ('fema' in funding_name or 'caljpia' in funding_name or 'caloes' in funding_name):
                    total_funding += amount
                    matched_projects.append({
                        'project': proj_name,
                        'funding_name': funding_name,
                        'amount': amount,
                        'start_date': proj['st']
                    })
                    break

result = {
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'disaster_projects_2022_count': len(disaster_projects_2022)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

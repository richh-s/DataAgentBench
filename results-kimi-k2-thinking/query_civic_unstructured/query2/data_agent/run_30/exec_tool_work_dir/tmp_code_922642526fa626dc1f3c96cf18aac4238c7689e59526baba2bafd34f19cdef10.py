code = """import json
import re
from collections import defaultdict

# Load the full civic documents data
civic_docs_file = var_functions.query_db:2
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load the full funding data
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    # Projects often appear as titles followed by updates
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Skip common headers/footers
        if any(skip in line for skip in ['Page ', 'Agenda Item', 'Public Works Commission', 'Agenda Report']):
            continue
            
        # Look for potential project names (typically not bullet points)
        if (len(line) > 10 and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('-') and
            not line.startswith('□') and
            'cid:' not in line and
            not line.startswith('To:') and
            not line.startswith('From:') and
            not line.startswith('Date:') and
            not line.startswith('Subject:') and
            'Project Schedule' not in line and
            'Recommended Action' not in line and
            'Discussion' not in line):
            
            # This might be a project name
            potential_project = line
            
            # Look ahead for status and date information
            status = None
            completion_date = None
            
            # Check next few lines for status/completion info
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                
                # Look for completed status
                if 'completed' in next_line.lower():
                    status = 'completed'
                    # Look for date in this line
                    if '2022' in next_line:
                        completion_date = '2022'
                    elif 'November 2022' in next_line:
                        completion_date = '2022'
                    elif '2022' in next_line:
                        completion_date = '2022'
                    break
                elif 'Complete Construction' in next_line and '2022' in next_line:
                    status = 'completed'
                    completion_date = '2022'
                    break
            
            # Check if project name contains "park" (park-related)
            is_park_related = 'park' in potential_project.lower()
            
            # Also check if it's in a context that suggests park
            context_check = ' '.join(lines[i:min(i+20, len(lines))]).lower()
            if 'park' in context_check and any(park_word in potential_project.lower() for park_word in ['park', 'playground', 'bluffs', 'canyon']):
                is_park_related = True
            
            if status == 'completed' and completion_date == '2022' and is_park_related:
                projects.append({
                    'Project_Name': potential_project,
                    'status': status,
                    'completion_date': completion_date,
                    'topic': 'park',
                    'source_file': filename
                })
                print(f"Found park project completed in 2022: {potential_project}")

print(f"\nFound {len(projects)} park-related projects completed in 2022")

# Create a mapping of project names to funding
project_names = [p['Project_Name'] for p in projects]
print(f"\nProject names to match: {project_names}")

# Find matching funding records
matching_funding = []
total_funding = 0

for fund in funding_data:
    fund_project_name = fund.get('Project_Name', '').lower()
    fund_amount = int(fund.get('Amount', 0))
    
    for project in projects:
        proj_name = project['Project_Name'].lower()
        
        # Check for exact match or close match
        if proj_name in fund_project_name or fund_project_name in proj_name:
            matching_funding.append({
                'project': project['Project_Name'],
                'funding_project': fund.get('Project_Name'),
                'amount': fund_amount,
                'source': fund.get('Funding_Source')
            })
            total_funding += fund_amount
            print(f"Matched: {project['Project_Name']} -> {fund.get('Project_Name')}: ${fund_amount}")
            break

print(f"\nTotal matching funding records: {len(matching_funding)}")
print(f"Total funding amount: ${total_funding}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

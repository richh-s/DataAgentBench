code = """import json
import re

# Get the file paths from storage
funding_file_path = locals()['var_functions.query_db:5']
civic_file_path = locals()['var_functions.query_db:6']

# Load funding data
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open(civic_file_path, 'r') as f:
    civic_data = json.load(f)

# Create a dict to store projects with their start dates from civic documents
projects_with_dates = {}

# Helper function to check if a date string indicates Spring 2022
def is_spring_2022(date_str):
    if not date_str or not isinstance(date_str, str):
        return False
    
    # Check if 2022 is in the string
    if '2022' not in date_str:
        return False
    
    # Check for Spring indicators
    spring_indicators = ['spring', 'march', 'april', 'may', '-03-', '-04-', '-05-']
    
    date_lower = date_str.lower()
    return any(indicator in date_lower for indicator in spring_indicators)

# Process each civic document
for doc in civic_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Split text into lines for easier processing
    lines = text.split('\n')
    
    current_project = None
    
    # Regex patterns for project names (typically start of line, followed by schedule info)
    # Looking for bold patterns or lines that look like project titles
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Skip common header lines
        if any(skip in line.lower() for skip in ['page ', 'agenda item', 'public works', 'commission']):
            continue
        
        # Look for project names - they often appear before "Project Schedule" or other keywords
        # Assume project names are relatively short lines that don't contain certain keywords
        if len(line) < 150 and not any(keyword in line.lower() for keyword in ['updates', 'schedule', 'project description', 'status', 'project updates']):
            # Check if next few lines contain schedule info
            current_pos = lines.index(line)
            next_lines = '\n'.join(lines[current_pos:current_pos+10])
            
            # Look for date patterns in the nearby text
            if '2022' in next_lines or 'Project Schedule' in next_lines:
                # This might be a project name, extract dates from nearby text
                
                # Look for date patterns like "2022-Spring", "2022-March", etc.
                date_matches = re.findall(r'\b(2022\s*-?\s*(?:Spring|March|April|May|02|-03|-04|-05))\b', next_lines, re.IGNORECASE)
                
                if date_matches:
                    for date_match in date_matches:
                        if is_spring_2022(date_match):
                            projects_with_dates[line] = date_match
                            break

# Now filter projects that started in Spring 2022
spring_2022_projects = {name: date for name, date in projects_with_dates.items() if is_spring_2022(date)}

# Load funding data into a dict by project name for lookup
funding_by_project = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = record.get('Amount', 0)
    
    # Some amounts might be strings
    try:
        amount = int(amount)
    except (ValueError, TypeError):
        amount = 0
    
    if proj_name:
        if proj_name not in funding_by_project:
            funding_by_project[proj_name] = 0
        funding_by_project[proj_name] += amount

# Match Spring 2022 projects with their funding
matched_projects = []
total_funding = 0

for proj_name, start_date in spring_2022_projects.items():
    # Try exact match first
    funding = funding_by_project.get(proj_name, 0)
    
    # If no exact match, check for partial matches
    if funding == 0:
        for funded_proj_name, funded_amount in funding_by_project.items():
            if proj_name.lower() in funded_proj_name.lower() or funded_proj_name.lower() in proj_name.lower():
                funding = funded_amount
                break
    
    if funding > 0:
        matched_projects.append({
            'project_name': proj_name,
            'start_date': start_date,
            'funding': funding
        })
        total_funding += funding

# Prepare result
result = {
    'count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)

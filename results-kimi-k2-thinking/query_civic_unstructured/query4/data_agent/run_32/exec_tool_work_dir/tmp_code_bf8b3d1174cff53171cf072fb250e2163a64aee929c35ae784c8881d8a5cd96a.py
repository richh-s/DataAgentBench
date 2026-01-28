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
    spring_indicators = ['spring', 'march', 'april', 'may']
    
    date_lower = date_str.lower()
    return any(indicator in date_lower for indicator in spring_indicators)

# Process each civic document
for doc in civic_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for project sections in the text
    # Pattern: Project name followed by project schedule with dates
    
    # Find all project names and their nearby dates
    # Look for patterns like "Project Schedule:" followed by date entries
    project_blocks = re.split(r'\n\s*(?=\b[A-Z][^\n]{3,80}\b)\n', text, flags=re.MULTILINE)
    
    for block in project_blocks:
        if len(block) > 500:  # Skip really large blocks
            continue
        
        # Look for project name (typically first line that looks like a title)
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        if not lines:
            continue
        
        # Skip non-project lines
        if any(skip in ' '.join(lines[:3]).lower() for skip in ['page ', 'agenda item', 'public works', 'commission', 'prepared by', 'approved by']):
            continue
        
        project_name = None
        for i, line in enumerate(lines):
            if len(line) < 100 and not any(keyword in line.lower() for keyword in ['update', 'schedule', 'description', 'status']):
                # Check if subsequent lines contain schedule info with 2022
                next_text = ' '.join(lines[i:i+10])
                
                # Look for spring 2022 dates
                if '2022' in next_text and any(spring in next_text.lower() for spring in ['spring', 'march', 'april', 'may']):
                    project_name = line
                    
                    # Extract the date string
                    date_match = re.search(r'(\d{4}\s*-?\s*(?:Spring|March|April|May|\d{2})\b)', next_text, re.IGNORECASE)
                    if date_match:
                        date_str = date_match.group(1)
                        if is_spring_2022(date_str):
                            projects_with_dates[project_name] = date_str
                    break

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

for proj_name, start_date in projects_with_dates.items():
    # Try exact match first
    funding = funding_by_project.get(proj_name, 0)
    
    # If no exact match, check for partial matches
    if funding == 0:
        # Check for variations like appending (FEMA Project) etc.
        for funded_proj_name, funded_amount in funding_by_project.items():
            # More flexible matching: check if the base project name is in the funded name
            base_name = proj_name.split(' (')[0]  # Remove parenthetical parts
            if base_name and base_name.lower() in funded_proj_name.lower():
                funding = funded_amount
                break
    
    if funding > 0:
        matched_projects.append({
            'project_name': proj_name,
            'start_date': start_date,
            'funding': funding
        })
        total_funding += funding

# Prepare result with basic stats
result = {
    'spring_2022_projects_found': len(projects_with_dates),
    'projects_with_funding': len(matched_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)

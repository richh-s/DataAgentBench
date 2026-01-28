code = """import json
import re

# Load the data
with open('file_storage/functions.query_db:2.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:3.json', 'r') as f:
    civic_docs_data = json.load(f)

# Create a mapping of project names to funding amounts
project_funding = {item['Project_Name']: int(item['Amount']) for item in funding_data}

print(f'Found {len(project_funding)} funding records')
print(f'Found {len(civic_docs_data)} civic documents')

# Process civic documents to extract project information
disaster_projects_2022 = []

# Keywords that indicate disaster projects
disaster_keywords = [
    'FEMA', 'fire', 'emergency', 'storm drain', 'stormwater', 'drainage', 'culvert', 
    'slope stabilization', 'CalOES', 'CalJPIA', 'Woolsey'
]

# Combine all text from civic documents
all_text = "\n\n".join([doc['text'] for doc in civic_docs_data])

# Look for project patterns in the text
# Pattern matching for project names and their schedules
project_pattern = re.compile(r'([A-Z][A-Za-z0-9\s&\-\(\)]+)\n\n\(cid:190\) (Updates|Project Schedule|Project Description):', re.MULTILINE)
schedule_pattern = re.compile(r'\(cid:131\) (Begin Construction|Advertise|Complete Design):\s*(Spring|Summer|Fall|Winter)\s*(202[0-9])')

# Simple approach: Find all project names that appear in both funding data and civic documents
# and check if they have disaster-related keywords
for project_name in project_funding.keys():
    # Check if project has disaster indicators
    is_disaster = False
    
    # Check for explicit disaster markers in project name
    if any(marker in project_name for marker in ['(FEMA', '(CalOES', '(CalJPIA']):
        is_disaster = True
    
    # Check if project name contains disaster keywords
    if not is_disaster:
        for keyword in disaster_keywords:
            if keyword.lower() in project_name.lower():
                is_disaster = True
                break
    
    # If disaster project, check if it's mentioned with 2022 timeline
    if is_disaster and project_name in all_text:
        # Find all mentions of this project
        project_mentions = [m.start() for m in re.finditer(re.escape(project_name), all_text)]
        
        for mention_pos in project_mentions:
            # Look for schedule info near this mention (within 500 characters)
            context_start = max(0, mention_pos - 200)
            context_end = min(len(all_text), mention_pos + 500)
            context = all_text[context_start:context_end]
            
            # Check if 2022 appears in the context
            if '2022' in context:
                # Extract the schedule info
                schedule_matches = schedule_pattern.findall(context)
                for match in schedule_matches:
                    if match[2] == '2022':  # Found a 2022 schedule
                        disaster_projects_2022.append({
                            'project_name': project_name,
                            'amount': project_funding[project_name],
                            'schedule': f"{match[0]}: {match[1]} {match[2]}"
                        })
                        break

print(f'Found {len(disaster_projects_2022)} disaster projects with 2022 schedule')

# Calculate total funding
total_funding = sum(p['amount'] for p in disaster_projects_2022)

print('__RESULT__:')
print(json.dumps({
    'total_funding_2022': total_funding,
    'disaster_projects': disaster_projects_2022
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'funding_type': "<class 'str'>", 'funding_preview': 'file_path', 'civic_type': "<class 'str'>", 'civic_preview': 'file_storage/functions.query_db:3.json'}, 'var_functions.execute_python:16': {'funding_count': 500, 'civic_count': 5, 'sample_funding': {'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, 'sample_civic': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChai'}}

exec(code, env_args)

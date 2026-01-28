code = """import json
import re

# Read the data from files
civic_docs = []
funding_data = []

with open('var_functions.query_db:16.json', 'r') as f:
    civic_docs = json.load(f)

with open('var_functions.query_db:17.json', 'r') as f:
    funding_data = json.load(f)

print("Processing civic documents...")

# Extract project information from civic documents
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line looks like a project name (not a bullet point, not a status line)
        if (len(line) > 5 and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('◦') and
            'Project Schedule' not in line and
            'Updates' not in line and
            'Complete Construction' not in line and
            'Construction was completed' not in line):
            
            # This might be a project name
            current_project = line
            
        # Check for completion in 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            if current_project:
                # Clean up project name
                clean_name = re.sub(r'^[A-Z]\s+', '', current_project)  # Remove leading letter+space
                clean_name = clean_name.strip()
                
                extracted_projects.append({
                    'project_name': clean_name,
                    'completion_info': line,
                    'year': '2022'
                })
                current_project = None

# Filter for park-related projects
park_projects = []
for proj in extracted_projects:
    name_lower = proj['project_name'].lower()
    if 'park' in name_lower or 'playground' in name_lower:
        park_projects.append(proj)

print(f"Found {len(park_projects)} park-related projects completed in 2022")

# Match with funding data
total_funding = 0
matched_projects = []

for park in park_projects:
    park_name = park['project_name']
    
    for fund in funding_data:
        fund_name = fund['Project_Name']
        
        # Flexible matching - check if park name is contained in fund name or vice versa
        park_key = park_name.lower().replace(' ', '').replace('-', '')
        fund_key = fund_name.lower().replace(' ', '').replace('-', '')
        
        # Also check for common variations
        if (park_key in fund_key or 
            fund_key in park_key or
            park_name.lower() in fund_name.lower() or
            fund_name.lower() in park_name.lower()):
            
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'park_project': park_name,
                'funding_record': fund_name,
                'amount': amount
            })
            break  # Avoid double-counting the same project

# Prepare result
result = {
    "total_funding_2022_park_projects": total_funding,
    "number_of_projects": len(matched_projects),
    "project_details": matched_projects
}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)

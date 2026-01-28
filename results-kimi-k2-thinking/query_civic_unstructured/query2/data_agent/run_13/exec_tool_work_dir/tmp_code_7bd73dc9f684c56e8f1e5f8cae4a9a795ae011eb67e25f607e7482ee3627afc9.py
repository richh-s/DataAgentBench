code = """import json
import re

# Read the civic documents from the file
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Read the funding data from the file  
with open('var_functions.query_db:5', 'r') as f:
    funding_data = json.load(f)

# Simple pattern matching to extract project names and completion dates
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for projects with park in the name that were completed
    # Pattern: "Bluffs Park Shade Structure" followed by "Construction was completed November 2022"
    # or similar patterns
    
    # First, find all park mentions
    park_mentions = re.finditer(r'([^.]*park[^.\n]*)', text, re.IGNORECASE)
    
    for match in park_mentions:
        context = match.group(1)
        
        # Check if this project was completed in 2022
        # Look for completion mentions after the project name
        if 'completed' in context.lower() and '2022' in context:
            # Extract project name (usually before "Updates:" or similar)
            proj_name = context.split('Updates:')[0].strip()
            proj_name = proj_name.split('\n')[0].strip()
            
            # Clean up project name
            if proj_name and len(proj_name) < 200:
                park_projects_2022.append({
                    'Project_Name': proj_name,
                    'status': 'completed',
                    'completed_year': '2022'
                })
        
        # Also check broader context
        start_pos = match.start()
        end_pos = min(len(text), start_pos + 500)  # Look at next 500 chars
        broader_context = text[start_pos:end_pos]
        
        if 'completed' in broader_context.lower() and '2022' in broader_context:
            proj_name = match.group(1).strip()
            if proj_name and len(proj_name) < 200:
                # Check if it's not already in the list
                exists = any(p['Project_Name'] == proj_name for p in park_projects_2022)
                if not exists:
                    park_projects_2022.append({
                        'Project_Name': proj_name,
                        'status': 'completed',
                        'completed_year': '2022'
                    })

# Remove duplicates and clean up
unique_projects = {}
for proj in park_projects_2022:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

park_projects_2022_clean = list(unique_projects.values())

# Try to match these with funding records
total_funding = 0
funding_matches = []

for proj in park_projects_2022_clean:
    proj_name = proj['Project_Name']
    
    # Look for funding records with matching project names
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '')
        
        # Match if project names are similar (one contains the other)
        if (proj_name.lower() in fund_name.lower() or 
            fund_name.lower() in proj_name.lower()):
            amount = int(fund.get('Amount', 0))
            total_funding += amount
            funding_matches.append({
                'project': proj_name,
                'funded_project': fund_name,
                'amount': amount,
                'source': fund.get('Funding_Source')
            })

result = {
    'park_projects_2022': park_projects_2022_clean,
    'funding_matches': funding_matches,
    'total_funding': total_funding,
    'count': len(park_projects_2022_clean)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

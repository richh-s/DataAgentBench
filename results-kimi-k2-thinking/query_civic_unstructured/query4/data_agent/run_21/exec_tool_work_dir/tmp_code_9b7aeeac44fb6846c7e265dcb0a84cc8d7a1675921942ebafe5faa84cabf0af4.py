code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:12']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic data
 civic_path = locals()['var_functions.query_db:2']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding map
funding_map = {}
for r in funding_records:
    funding_map[r['Project_Name']] = int(r['Amount'])

# Find spring 2022 projects
spring_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Simple pattern: find Spring 2022 mentions
    spring_matches = re.finditer('Spring 2022', text)
    
    for match in spring_matches:
        # Get context around the match
        start = max(0, match.start() - 200)
        end = min(len(text), match.end() + 200)
        context = text[start:end]
        
        # Look for project names in context
        lines = context.split('\n')
        for line in lines:
            line = line.strip().replace('•', '')
            # Basic project name detection
            if len(line) < 100 and any(w in line.lower() for w in ['project', 'improvements', 'repairs', 'installation']):
                spring_projects.add(line)
                break

# Match with funding
matches = {}
for proj in spring_projects:
    if proj in funding_map:
        matches[proj] = funding_map[proj]
    else:
        # Try partial match
        for fproj, amt in funding_map.items():
            if proj.lower().split('(')[0].strip() == fproj.lower().split('(')[0].strip():
                matches[fproj] = amt
                break

# Calculate
result = {
    'count': len(matches),
    'total_funding': sum(matches.values()) if matches else 0,
    'projects': list(matches.keys())[:20]  # Sample
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records'}

exec(code, env_args)

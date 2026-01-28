code = """import json

# Read data from files
civic_path = '/tmp/tmpyq7d3x4g.json'
funding_path = '/tmp/tmp8j8x8g9f.json'

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Simple approach: Search for Spring 2022 mentions and extract context
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Find spring 2022 references
    spring_pos = 0
    while True:
        spring_pos = lower_text.find('spring 2022', spring_pos)
        if spring_pos == -1:
            break
        
        # Get context before the reference
        context_start = max(0, spring_pos - 400)
        context = text[context_start:spring_pos]
        
        # Try to find project name (look for last meaningful line)
        lines = context.split('\n')
        for line in reversed(lines):
            stripped = line.strip()
            if (stripped and len(stripped) > 8 and not stripped.startswith('(') and 
                'Page' not in stripped and 'Capital Improvement' not in stripped and
                'Project Schedule' not in stripped and 'Estimated Schedule' not in stripped):
                spring_projects.append(stripped[:200])
                break
        
        spring_pos += 1

# Remove duplicates
unique_projects = []
seen = set()
for p in spring_projects:
    if p not in seen:
        seen.add(p)
        unique_projects.append(p)

# Match with funding data
total_funding = 0

for project_name in unique_projects:
    project_lower = project_name.lower()
    for funding in funding_data:
        funding_name = funding['Project_Name']
        # Check for match
        if (project_lower in funding_name.lower() or 
            funding_name.lower() in project_lower):
            total_funding += int(funding['Amount'])
            break

result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

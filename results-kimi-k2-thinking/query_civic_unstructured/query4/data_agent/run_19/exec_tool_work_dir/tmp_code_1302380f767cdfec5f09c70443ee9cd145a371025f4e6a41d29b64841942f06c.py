code = """import json, re

# Read the civic documents from the file
with open('/tmp/tmpyq7d3x4g.json', 'r') as f:
    civic_docs = json.load(f)

# Look for projects specifically mentioned with Spring 2022 dates
spring2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find occurrences of "Spring 2022" or "spring 2022"
    pattern = r'Spring\s+2022'
    matches = [(m.start(), m.group()) for m in re.finditer(pattern, text, re.I)]
    
    for pos, match_text in matches:
        # Look backwards to find the project name
        # Project names typically appear before the schedule info
        start_context = max(0, pos - 300)
        context = text[start_context:pos]
        
        # Find project name by looking for the last significant heading before this position
        lines = context.split('\n')
        for i in range(len(lines)-1, -1, -1):
            line = lines[i].strip()
            if (line and len(line) > 5 and not line.startswith('(') and 
                not line.startswith('Page') and 'Capital Improvement' not in line and
                'Project Schedule' not in line and 'Estimated Schedule' not in line):
                
                project_name = line[:200]
                if 'Project' in project_name or any(keyword in project_name.lower() for keyword in ['road', 'park', 'drainage', 'storm', 'improvements', 'structure']):
                    spring2022_projects.append(project_name)
                    break

# Remove duplicates
unique_projects = []
seen = set()
for p in spring2022_projects:
    if p not in seen:
        seen.add(p)
        unique_projects.append(p)

print('Found', len(unique_projects), 'Spring 2022 projects')

# Read the funding data from the full query
with open('/tmp/tmp8j8x8g9f.json', 'r') as f:
    funding_data = json.load(f)

# Match project names and sum funding
matched_funding = 0
matching_projects = []

for project_name in unique_projects:
    # Try to find matching funding records
    for funding in funding_data:
        funding_proj = funding['Project_Name']
        # Check if our project name is contained in the funding project name
        if project_name.lower() in funding_proj.lower():
            matched_funding += int(funding['Amount'])
            matching_projects.append({
                'document_project': project_name,
                'funding_project': funding_proj,
                'amount': int(funding['Amount'])
            })
            break

result = {
    'spring_2022_project_count': len(unique_projects),
    'total_funding_amount': matched_funding,
    'projects_details': matching_projects
}

print('Total funding for Spring 2022 projects:', matched_funding)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

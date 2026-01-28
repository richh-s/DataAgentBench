code = """import json, re

# Load civic documents data
civic_path = '/tmp/tmpyq7d3x4g.json'
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Find projects with Spring 2022 dates
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    txt_lower = text.lower()
    
    # Find all Spring 2022 references
    spring_pos = 0
    while True:
        spring_pos = txt_lower.find('spring 2022', spring_pos)
        if spring_pos == -1:
            break
        
        # Get context before the Spring 2022 mention
        context_start = max(0, spring_pos - 500)
        context = text[context_start:spring_pos]
        
        # Look for project name (typically separated by double newlines)
        sections = context.split('\n\n')
        for section in reversed(sections):
            lines = section.strip().split('\n')
            for line in reversed(lines):
                proj_name = line.strip()
                # Filter out non-project lines
                if (proj_name and len(proj_name) > 8 and 
                    not proj_name.startswith('(') and 
                    'Page' not in proj_name and 
                    'Capital Improvement' not in proj_name and
                    'Project Schedule' not in proj_name and 
                    'Estimated Schedule' not in proj_name and
                    not proj_name.startswith('cid:') and
                    'Project Description' not in proj_name):
                    spring_2022_projects.add(proj_name)
                    break
            if spring_2022_projects and proj_name in spring_2022_projects:
                break
        
        spring_pos += 1

# Also check for 2022-Spring format
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022-Spring' in text or '2022-spring' in text:
        # Find project names near these mentions
        matches = list(re.finditer(r'2022[-\s]Spring', text, re.IGNORECASE))
        for match in matches:
            pos = match.start()
            context_start = max(0, pos - 400)
            context = text[context_start:pos]
            lines = [l.strip() for l in context.split('\n') if l.strip()]
            for line in reversed(lines):
                if (line and not line.startswith('(') and 'Page' not in line and
                    'Capital Improvement' not in line and len(line) > 10):
                    spring_2022_projects.add(line)
                    break

print("Found", len(spring_2022_projects), "unique Spring 2022 projects in documents")

# Load funding data
funding_path = '/tmp/tmp8j8x8g9f.json'
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Match with funding and calculate total
total_funding = 0
matched_count = 0

for project_name in spring_2022_projects:
    project_lower = project_name.lower()
    for funding in funding_data:
        funding_name = funding['Project_Name'].lower()
        # Check if project name contains or is contained in funding name
        if (project_lower in funding_name or funding_name in project_lower):
            amount = int(funding['Amount'])
            total_funding += amount
            matched_count += 1
            print(f"Matched: {project_name} -> {funding['Project_Name']} = ${amount}")
            break

result = {
    "total_spring_2022_projects": len(spring_2022_projects),
    "projects_with_funding": matched_count,
    "total_funding_amount": total_funding
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)

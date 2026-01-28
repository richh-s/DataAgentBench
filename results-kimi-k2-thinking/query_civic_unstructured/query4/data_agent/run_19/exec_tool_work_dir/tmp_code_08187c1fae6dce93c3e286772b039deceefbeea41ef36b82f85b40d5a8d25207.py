code = """import json
import re

# Load civic documents
with open('/tmp/tmpyq7d3x4g.json', 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open('/tmp/tmp8j8x8g9f.json', 'r') as f:
    funding_data = json.load(f)

spring_2022_project_names = []

# Extract project names with Spring 2022 mentions
for doc in civic_docs:
    text = doc.get('text', '')
    # Find Spring 2022 dates
    spring_matches = list(re.finditer(r'Spring\s+2022', text, re.IGNORECASE))
    
    for match in spring_matches:
        pos = match.start()
        # Get context before this match to find project name
        context_start = max(0, pos - 400)
        context_text = text[context_start:pos]
        
        # Look for project name patterns
        # Projects are typically separated by double newlines
        sections = re.split(r'\n\n', context_text)
        if sections:
            # The last section in context is likely the project name
            for section in reversed(sections):
                lines = section.strip().split('\n')
                for line in reversed(lines):
                    line = line.strip()
                    # Skip headers, markers, and short lines
                    if (line and len(line) > 10 and not line.startswith('(') and 
                        'Page' not in line and 'Capital Improvement' not in line and
                        'Project Schedule' not in line and 'Estimated Schedule' not in line and
                        not line.startswith('cid:')):
                        spring_2022_project_names.append(line[:200])
                        break
                if len(spring_2022_project_names) > 0 and spring_2022_project_names[-1]:
                    break

# Remove duplicates while preserving order
seen = set()
unique_projects = []
for proj in spring_2022_project_names:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

# Match projects with funding data
total_funding = 0
matched_projects = []

for project_name in unique_projects:
    for funding in funding_data:
        funding_proj_name = funding['Project_Name']
        # Check if project name matches (allow partial match)
        if (project_name.lower() in funding_proj_name.lower() or 
            funding_proj_name.lower() in project_name.lower() or
            any(word in funding_proj_name.lower() for word in project_name.lower().split() if len(word) > 4)):
            amount = int(funding['Amount'])
            total_funding += amount
            matched_projects.append({
                'project': project_name,
                'funding_match': funding_proj_name,
                'amount': amount
            })
            break

result = {
    'spring_2022_project_count': len(unique_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

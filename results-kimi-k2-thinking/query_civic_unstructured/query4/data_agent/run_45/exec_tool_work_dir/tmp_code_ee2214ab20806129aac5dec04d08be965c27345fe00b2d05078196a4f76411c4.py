code = """import json
import re

# Get file paths from previous queries
civic_docs_file = locals()['var_functions.query_db:60']
funding_file = locals()['var_functions.query_db:48']

# Load the data
with open(civic_docs_file, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r', encoding='utf-8') as f:
    funding_data = json.load(f)

print('Civic documents loaded:', len(civic_docs))
print('Funding records loaded:', len(funding_data))

# Create funding lookup map
funding_map = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if proj_name and amount > 0:
        funding_map[proj_name] = amount
        # Also store base name without parentheses for better matching
        base_name = proj_name.split('(')[0].strip()
        if base_name != proj_name:
            funding_map[base_name] = amount

# Extract Spring 2022 projects from civic documents
spring_2022_projects = set()
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']

for doc in civic_docs:
    text = doc.get('text', '')
    # Lowercase for pattern matching
    text_lower = text.lower()
    
    # Check if this document mentions spring 2022
    has_spring_2022 = any(pattern.lower() in text_lower for pattern in spring_patterns)
    if not has_spring_2022:
        continue
    
    # Split into lines for processing
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Look for lines that contain project-related keywords
        project_keywords = ['PROJECT', 'IMPROVEMENTS', 'REPAIRS', 'REPAIR', 'IMPROVEMENT']
        has_project_keyword = any(keyword in line.upper() for keyword in project_keywords)
        
        if has_project_keyword:
            # Check if this line looks like a project name (contains uppercase)
            upper_count = sum(1 for c in line if c.isupper())
            total_alpha = len([c for c in line if c.isalpha()])
            
            # Project names typically have significant uppercase content
            if total_alpha > 0 and (upper_count / total_alpha) > 0.2:
                # Check nearby context for spring 2022 references
                context_start = max(0, i-5)
                context_end = min(len(lines), i+6)
                context = ' '.join([l.strip() for l in lines[context_start:context_end]]).lower()
                
                if any(pattern.lower() in context for pattern in spring_patterns):
                    spring_2022_projects.add(line.strip())

print('Spring 2022 projects found:', len(spring_2022_projects))

# Match projects with funding data
matched_projects = []
total_funding = 0

for project in spring_2022_projects:
    # Try exact match
    if project in funding_map:
        amount = funding_map[project]
        matched_projects.append({'project_name': project, 'amount': amount})
        total_funding += amount
    else:
        # Try base name match (without parentheses)
        base_project = project.split('(')[0].strip()
        if base_project in funding_map:
            amount = funding_map[base_project]
            matched_projects.append({'project_name': project, 'matched_as': base_project, 'amount': amount})
            total_funding += amount

# Output final result
result = {
    'spring_2022_project_count': len(matched_projects),
    'total_funding': total_funding,
    'matched_projects': matched_projects
}

print('Matched projects:', len(matched_projects))
print('Total funding:', total_funding)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': [{'total_records': '500'}]}

exec(code, env_args)

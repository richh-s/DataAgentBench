code = """import json

# Load civic documents
docs_file = locals()['var_functions.query_db:2']
with open(docs_file, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

print('Civic documents loaded:', len(civic_docs))

# Load funding data
funding_file = locals()['var_functions.query_db:48']
with open(funding_file, 'r', encoding='utf-8') as f:
    funding_data = json.load(f)

print('Funding records loaded:', len(funding_data))

# Extract Spring 2022 projects from civic docs
spring_2022_projects = []
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if document mentions Spring 2022
    has_spring = any(pattern in text for pattern in spring_patterns)
    if not has_spring:
        continue
    
    # Split into lines and look for project names
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Look for lines that contain project keywords
        project_keywords = ['Project', 'Improvements', 'Repairs', 'Repair', 'Improvement']
        has_keyword = any(kw in line for kw in project_keywords)
        
        if has_keyword:
            # Check if line looks like a project name (has uppercase letters)
            upper_count = sum(1 for c in line if c.isupper())
            total_alpha = len([c for c in line if c.isalpha()])
            
            if total_alpha > 0 and upper_count / total_alpha > 0.2:
                # Check nearby context for Spring 2022 date
                context_start = max(0, i-5)
                context_end = min(len(lines), i+6)
                context = ' '.join([l.strip() for l in lines[context_start:context_end]])
                
                if any(pattern in context for pattern in spring_patterns):
                    spring_2022_projects.append(line.strip())

# Remove duplicates
unique_spring_projects = list(set(spring_2022_projects))
print('Spring 2022 projects found:', len(unique_spring_projects))

# Create a mapping of project names to amounts from funding data
funding_map = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if proj_name:
        funding_map[proj_name] = amount

# Match Spring 2022 projects with funding data
matched_projects = []
total_funding = 0

for spring_proj in unique_spring_projects:
    # Look for exact matches or close matches
    if spring_proj in funding_map:
        amount = funding_map[spring_proj]
        matched_projects.append({
            'project_name': spring_proj,
            'amount': amount
        })
        total_funding += amount
    else:
        # Try to find partial matches (project name without suffixes)
        for funded_proj, amount in funding_map.items():
            # Check if funded project starts with spring project name or vice versa
            if (spring_proj.startswith(funded_proj) or 
                funded_proj.startswith(spring_proj) or
                spring_proj.split('(')[0].strip() == funded_proj.split('(')[0].strip()):
                matched_projects.append({
                    'project_name': spring_proj,
                    'matched_funding_name': funded_proj,
                    'amount': amount
                })
                total_funding += amount
                break

print('Matched with funding:', len(matched_projects))
print('Total funding:', total_funding)

# Prepare final result
result = {
    'spring_2022_project_count': len(matched_projects),
    'total_funding': total_funding,
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}}

exec(code, env_args)

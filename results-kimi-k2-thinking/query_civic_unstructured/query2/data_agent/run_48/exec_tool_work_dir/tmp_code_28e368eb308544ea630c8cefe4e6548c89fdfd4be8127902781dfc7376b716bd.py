code = """import json

# Load funding data from the previous query
funding_data = var_functions.query_db:0

# Load civic documents from file
civic_docs_path = var_functions.query_db:6
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(civic_docs)} documents and {len(funding_data)} funding records")

# Extract park-related projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    if not text:
        continue
    
    # Split into lines for easier parsing
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Look for park-related terms in potential project names
        line_lower = line.lower()
        
        # Skip common headings and metadata
        skip_terms = ['capital improvement', 'disaster recovery', 'agenda item', 'page', 'to:', 
                     'prepared by', 'subject:', 'discussion:', 'recommended action', 
                     'updates:', 'project schedule:', 'estimated schedule:', 'project description']
        
        should_skip = any(term in line_lower for term in skip_terms)
        
        if should_skip or len(line) > 150:
            continue
        
        # Check if this line contains park-related keywords
        park_keywords = ['park', 'playground', 'walkway', 'walk way', 'shade structure']
        has_park = any(keyword in line_lower for keyword in park_keywords)
        
        if has_park and line[0].isupper():
            # Look ahead and behind for completion in 2022
            context_start = max(0, i-5)
            context_end = min(len(lines), i+10)
            context = '\n'.join(lines[context_start:context_end]).lower()
            
            # Check for completion and 2022 in context
            if 'completed' in context and '2022' in context:
                # Additional check: ensure it's not just a heading by checking for project structure
                if 'updates:' in context or 'construction' in context:
                    # Clean up the project name
                    clean_name = line.strip()
                    if clean_name and not clean_name.endswith(':'):
                        project_info = {
                            'Project_Name': clean_name,
                            'filename': filename,
                            'context': '\n'.join(lines[max(0,i-2):min(len(lines),i+8)])
                        }
                        park_projects_2022.append(project_info)

print(f"Found {len(park_projects_2022)} park projects completed in 2022")

for proj in park_projects_2022:
    print(f"\nProject: {proj['Project_Name']}")
    print(f"Context preview: {proj['context'][:150]}...")

# Match with funding data and calculate total
total_funding = 0
matched_projects = []

for park_proj in park_projects_2022:
    proj_name = park_proj['Project_Name']
    
    # Also try variations with common project suffixes
    possible_names = [
        proj_name,
        f"{proj_name} (FEMA Project)",
        f"{proj_name} (CalOES Project)",
        f"{proj_name} (CalJPIA Project)"
    ]
    
    matched = False
    for fund in funding_data:
        if fund['Project_Name'] in possible_names:
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'Project_Name': fund['Project_Name'],
                'Amount': amount
            })
            matched = True
            print(f"Matched: {fund['Project_Name']} - ${amount}")
            break
    
    if not matched:
        print(f"No funding match for: {proj_name}")

result = {
    'total_funding_2022': total_funding,
    'number_of_projects': len(matched_projects),
    'matched_projects': matched_projects
}

print('\n__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

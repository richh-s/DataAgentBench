code = """import json
import re

# Read the civic documents data
civic_docs_file = var_functions.query_db:10
with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

# Read the funding data
funding_file = var_functions.query_db:11
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs_data)} civic documents and {len(funding_data)} funding records")

# Create a mapping of project names to funding amounts for easy lookup
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Extract projects from civic docs with Spring 2022 start dates
spring_2022_projects = []

# Patterns for Spring 2022
spring_patterns = [
    r'2022[\-\s]?Spring',
    r'2022[\-\s]?March',
    r'2022[\-\s]?April',
    r'2022[\-\s]?May',
    r'2022[\-\s]?03',
    r'2022[\-\s]?04',
    r'2022[\-\s]?05'
]

# Compile regex pattern for project extraction (more lenient)
project_pattern = re.compile(r"([A-Z][a-zA-Z0-9\s\-\(\)]+?)(?=\n\s*(?:cid:|\d+\.|\u2022|\u2013|\u2014|$))", re.MULTILINE)

# Iterate through documents and extract projects
for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for project sections
    lines = text.split('\n')
    current_project = None
    project_start = None
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names (header-like lines)
        # Usually they are title case and don't start with bullet points
        if (len(line) > 5 and 
            line[0].isalpha() and 
            line[0].isupper() and 
            not line.startswith(('(', '•', '-', '–', '—', '•', '●', '○')) and
            not any(keyword in line.lower() for keyword in ['update', 'schedule', 'project description']) and
            ':' not in line):
            
            # This might be a project name
            potential_project = line.strip()
            
            # Check if the next few lines have date information
            # Store as potential project
            current_project = potential_project
            
        # Look for Spring 2022 dates
        for pattern in spring_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                if current_project:
                    # Found a Spring 2022 project
                    spring_2022_projects.append({
                        'Project_Name': current_project,
                        'Start_Date_Info': line
                    })
                break
    
    # Also try more aggressive pattern matching
    # Look for project sections that mention start dates
    project_blocks = re.findall(r'([A-Z][a-zA-Z\s]+?[A-Z][a-zA-Z\s]+?)(?=\s*(?:update|schedule|estimated schedule|$))', text, re.IGNORECASE)
    
    for block in project_blocks:
        block_text = block.strip()
        if len(block_text) > 10 and not any(skip in block_text.lower() for skip in ['project description', 'cip', 'fiscal year']):
            
            # Check if this block or nearby text contains Spring 2022
            block_start = text.find(block_text)
            nearby_text = text[block_start:min(block_start + 500, len(text))]
            
            for pattern in spring_patterns:
                if re.search(pattern, nearby_text, re.IGNORECASE):
                    # Clean up the project name
                    proj_name = block_text.strip()
                    if proj_name and proj_name not in [p['Project_Name'] for p in spring_2022_projects]:
                        spring_2022_projects.append({
                            'Project_Name': proj_name,
                            'Start_Date_Info': 'Spring 2022 pattern found'
                        })
                    break

print(f"Found {len(spring_2022_projects)} potential Spring 2022 projects")

# Display projects found
for proj in spring_2022_projects[:20]:  # Show first 20
    print(f"  - {proj['Project_Name']}")

# Now match with funding
total_funding = 0
matched_projects = []

for proj in spring_2022_projects:
    proj_name = proj['Project_Name']
    
    # Direct match
    if proj_name in funding_map:
        funding = funding_map[proj_name]
        total_funding += funding
        matched_projects.append({
            'Project_Name': proj_name,
            'Funding': funding
        })
        print(f"Matched: {proj_name} - ${funding:,}")
    else:
        # Try fuzzy matching - check if any funding project contains this name
        # or if this name contains a funding project name
        for fund_proj, fund_amount in funding_map.items():
            # Check for partial matches
            if (proj_name in fund_proj or 
                fund_proj in proj_name or
                any(word in proj_name.lower() for word in fund_proj.lower().split() if len(word) > 5)):
                total_funding += fund_amount
                matched_projects.append({
                    'Project_Name': fund_proj,
                    'Funding': fund_amount
                })
                print(f"Fuzzy matched: {proj_name} -> {fund_proj} - ${fund_amount:,}")
                break

print(f"\nTotal Spring 2022 projects matched with funding: {len(matched_projects)}")
print(f"Total funding: ${total_funding:,}")

# Save results for final answer
result_data = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)

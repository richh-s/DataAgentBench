code = """import json, os, re

# Access the stored results
funding_result = var_functions.query_db_48
civic_result = var_functions.query_db_2

# Load funding data
if isinstance(funding_result, str) and os.path.exists(funding_result):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result

# Load civic docs data
if isinstance(civic_result, str) and os.path.exists(civic_result):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

print("Data loaded successfully!")
print(f"Funding records: {len(funding_records)}")
print(f"Civic documents: {len(civic_docs)}")

# Create funding lookup map
funding_lookup = {}
for record in funding_records:
    proj_name = str(record['Project_Name'])
    funding_lookup[proj_name] = int(record['Amount'])

print(f"Funding lookup created with {len(funding_lookup)} entries")

# Find Spring 2022 projects
spring_2022_projects = set()

# Patterns to match Spring 2022 or March-May 2022
spring_patterns = [r'Spring[\s-]*2022', r'2022[\s-]*-?Spring', 
                   r'March[\s-]*2022', r'2022[\s-]*March',
                   r'April[\s-]*2022', r'2022[\s-]*April',
                   r'May[\s-]*2022', r'2022[\s-]*May']

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for Spring 2022 mentions
    for i, line in enumerate(lines):
        line = line.strip()
        # Check if line contains Spring 2022 pattern
        for pattern in spring_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                # Look backwards for project name
                for j in range(i-1, max(0, i-5), -1):
                    prev_line = lines[j].strip()
                    # Clean up the line
                    prev_line = prev_line.replace('·', '').replace('•', '').replace('+', '').strip()
                    
                    # Skip empty or very short lines
                    if not prev_line or len(prev_line) < 3:
                        continue
                    
                    # Skip section headers
                    if any(header in prev_line.lower() for header in 
                          ['agenda', 'discussion', 'project schedule', 'updates']):
                        continue
                    
                    # Look for project indicators
                    project_keywords = ['project', 'improvements', 'repairs', 'repaving', 
                                       'installation', 'construction', 'upgrades', 'development',
                                       'renovation', 'replacement', 'maintenance', 'restoration']
                    
                    # Title case detection (many capital letters)
                    words = prev_line.split()
                    capital_words = sum(1 for w in words if w and w[0].isupper())
                    title_case_ratio = capital_words / len(words) if words else 0
                    
                    # Check if this looks like a project name
                    if (any(kw in prev_line.lower() for kw in project_keywords) or 
                        title_case_ratio > 0.4):
                        # Valid project name found
                        if len(prev_line) > 3 and len(prev_line) < 200:
                            spring_2022_projects.add(prev_line)
                            break

print(f"Found {len(spring_2022_projects)} potential Spring 2022 projects")

# Match projects with funding data
matched_projects = {}

for proj_name in spring_2022_projects:
    # Direct exact match
    if proj_name in funding_lookup:
        matched_projects[proj_name] = funding_lookup[proj_name]
    else:
        # Try to find similar project names
        for fund_proj, amount in funding_lookup.items():
            # Check if project name appears in funding project name
            if proj_name.lower() in fund_proj.lower():
                matched_projects[fund_proj] = amount
                break
            # Check if funding project (without suffix) matches
            base_fund_name = fund_proj.split('(')[0].strip()
            if proj_name.lower() == base_fund_name.lower():
                matched_projects[fund_proj] = amount
                break

# Calculate final results
total_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

print(f"\n{'='*60}")
print(f"SPRING 2022 PROJECTS: {total_projects}")
print(f"TOTAL FUNDING: ${total_funding:,}")
print(f"{'='*60}")

for proj_name, amount in matched_projects.items():
    print(f"• {proj_name}: ${amount:,}")

# Create JSON result for validation
result_json = json.dumps({
    'total_projects': total_projects,
    'total_funding': total_funding,
    'projects': [{'name': proj, 'funding': amt} for proj, amt in matched_projects.items()]
}, indent=2)

print("\n" + result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)

code = """import json
import re
import os

# Read the file paths from stored variables
funding_file = var_functions.query_db_106
civic_file = var_functions.query_db_88

# Load funding data
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents with Spring 2022 mentions
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_records)} funding records")
print(f"Loaded {len(civic_docs)} civic documents with Spring 2022 references")

# Build funding lookup dictionary
funding_lookup = {}
for record in funding_records:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[proj_name] = amount

print(f"Built funding lookup with {len(funding_lookup)} projects")

# Extract Spring 2022 projects from civic documents
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Look for Spring 2022 mentions
        if 'Spring 2022' in line or '2022-Spring' in line:
            # Look backwards for project name (up to 5 lines back)
            for j in range(i-1, max(0, i-6), -1):
                prev_line = lines[j].strip()
                # Clean up the line
                prev_clean = prev_line.replace('·', '').replace('•', '').replace('+', '').replace('–', '').strip()
                
                # Skip empty lines
                if not prev_clean:
                    continue
                
                # Skip lines that are too long to be project names
                if len(prev_clean) > 200:
                    continue
                
                # Skip section headers and bullet points
                skip_keywords = ['agenda', 'discussion', 'project schedule', 'updates', 'complete design', 'begin construction', 'advertise', 'award contract']
                if any(keyword in prev_clean.lower() for keyword in skip_keywords):
                    continue
                
                # Check if line contains project keywords or is in title case
                project_keywords = ['project', 'improvements', 'repairs', 'repaving', 'installation', 'construction', 'upgrades', 'renovation', 'replacement', 'maintenance', 'development']
                has_keyword = any(keyword in prev_clean.lower() for keyword in project_keywords)
                
                # Check if line is title case (many capitalized words)
                words = prev_clean.split()
                if words:
                    capital_words = sum(1 for w in words if w and w[0].isupper())
                    capital_ratio = capital_words / len(words)
                    is_title_case = capital_ratio > 0.4
                    
                    # If it has project keywords or is title case, it's likely a project name
                    if has_keyword or is_title_case:
                        # Skip lines that are just "Project" or similar
                        if prev_clean.lower() not in ['project', 'project schedule', 'project updates', 'capital improvement projects', 'disaster projects']:
                            spring_2022_projects.add(prev_clean)
                            break

print(f"Found {len(spring_2022_projects)} potential Spring 2022 projects")

# Normalize function for name matching
def normalize_name(name):
    import re
    # Extract base name before parentheses, convert to lowercase, remove special chars and extra spaces
    base = name.split('(')[0].strip()
    # Remove non-alphanumeric characters except spaces
    cleaned = re.sub(r'[^a-z0-9\s]', '', base.lower())
    # Collapse multiple spaces
    return re.sub(r'\s+', ' ', cleaned).strip()

# Match found projects with funding data
matched_projects = {}
unmatched_projects = set()

for spring_proj in spring_2022_projects:
    # Direct exact match
    if spring_proj in funding_lookup:
        matched_projects[spring_proj] = funding_lookup[spring_proj]
        continue
    
    # Try normalized base name match
    spring_normalized = normalize_name(spring_proj)
    
    # Skip if normalized name is too short
    if len(spring_normalized) < 5:
        continue
    
    matched = False
    for funded_name, amount in funding_lookup.items():
        funded_normalized = normalize_name(funded_name)
        
        # Exact normalized match
        if spring_normalized == funded_normalized:
            matched_projects[funded_name] = amount
            matched = True
            break
        
        # Check if spring project is contained in funded project
        if spring_normalized in funded_normalized and len(spring_normalized) > 10:
            matched_projects[funded_name] = amount
            matched = True
            break
        
        # Check if funded project is contained in spring project
        if funded_normalized in spring_normalized and len(funded_normalized) > 10:
            matched_projects[funded_name] = amount
            matched = True
            break
    
    if not matched:
        unmatched_projects.add(spring_proj)

print(f"Matched {len(matched_projects)} projects with funding data")
print(f"Could not match {len(unmatched_projects)} projects")

# Calculate totals
total_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

print('='*70)
print('SPRING 2022 PROJECTS: {0}'.format(total_projects))
print('TOTAL FUNDING: ${0:,}'.format(total_funding))
print('='*70)

for proj_name, amount in sorted(matched_projects.items()):
    print('• {0}: ${1:,}'.format(proj_name, amount))

# Prepare final result
result = {
    'total_projects': total_projects,
    'total_funding': total_funding,
    'projects': [{'name': proj, 'funding': amt} for proj, amt in sorted(matched_projects.items())],
    'unmatched': sorted(list(unmatched_projects))
}

print('\n__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json', 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json'}

exec(code, env_args)

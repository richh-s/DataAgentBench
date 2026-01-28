code = """import json, re, os, sys

# Load data from stored file paths
funding_path = var_functions.query_db_84
civic_path = var_functions.query_db_88

# Read file contents and parse JSON
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

print("Loaded {0} funding records and {1} civic documents".format(len(funding_data), len(civic_data)))

# Build funding lookup dictionary
funding_lookup = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[proj_name] = amount

# Extract Spring 2022 projects from civic documents
spring_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Look for Spring 2022 mentions
        if 'Spring 2022' in line or '2022-Spring' in line:
            # Search backwards for project name (up to 5 lines)
            for j in range(i-1, max(0, i-5), -1):
                prev_line = lines[j].strip()
                # Clean up the line
                prev_clean = prev_line.replace('·', '').replace('•', '').replace('+', '').strip()
                
                # Skip empty or very short lines
                if not prev_clean or len(prev_clean) < 3:
                    continue
                
                # Skip section headers
                if any(header in prev_clean.lower() for header in 
                      ['agenda', 'discussion', 'project schedule', 'updates']):
                    continue
                
                # Check if line contains project keywords
                project_keywords = ['project', 'improvements', 'repairs', 'repaving', 'installation', 'construction', 'upgrades', 'renovation', 'replacement']
                has_keyword = any(keyword in prev_clean.lower() for keyword in project_keywords)
                
                # Check if line is title case (many capital letters)
                words = prev_clean.split()
                if words:
                    capital_words = sum(1 for w in words if w and w[0].isupper())
                    capital_ratio = capital_words / len(words)
                    is_title_case = capital_ratio > 0.4
                    
                    # If it has project keywords or is title case, add it
                    if has_keyword or is_title_case:
                        if len(prev_clean) < 200:  # Reasonable length for project name
                            spring_projects.add(prev_clean)
                            break

print("Found {0} Spring 2022 projects in documents".format(len(spring_projects)))

# Normalize function for matching
def normalize_name(name):
    import re
    # Extract base name before parentheses
    base = name.split('(')[0].strip()
    # Remove non-alphanumeric characters and convert to lowercase
    return re.sub(r'[^a-z0-9\s]', '', base.lower())

# Match found projects with funding data
matched_projects = {}
for proj_name in spring_projects:
    # Direct exact match
    if proj_name in funding_lookup:
        matched_projects[proj_name] = funding_lookup[proj_name]
        continue
    
    # Try normalized base name match
    proj_normalized = normalize_name(proj_name)
    
    for funded_name, amount in funding_lookup.items():
        funded_normalized = normalize_name(funded_name)
        if proj_normalized == funded_normalized:
            matched_projects[funded_name] = amount
            break
        
        # Check if one is contained in the other
        if (len(proj_normalized) > 10 and 
            (proj_normalized in funded_normalized or funded_normalized in proj_normalized)):
            matched_projects[funded_name] = amount
            break

print("Matched {0} projects with funding data".format(len(matched_projects)))

# Calculate totals
total_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

print('\n' + '='*60)
print('SPRING 2022 PROJECTS: {0}'.format(total_projects))
print('TOTAL FUNDING: ${0:,}'.format(total_funding))
print('='*60)

for proj_name, amount in matched_projects.items():
    print('• {0}: ${1:,}'.format(proj_name, amount))

result = {
    'total_projects': total_projects,
    'total_funding': total_funding,
    'projects': [{'name': proj, 'funding': amt} for proj, amt in matched_projects.items()]
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json'}

exec(code, env_args)

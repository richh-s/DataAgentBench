code = """import json
import re

# Load data from the stored file paths
funding_path = var_functions.query_db_48
civic_path = var_functions.query_db_74

# Read funding records
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Read civic documents with Spring 2022 mentions
with open(civic_path, 'r') as f:
    spring_docs = json.load(f)

print('Loaded {0} funding records'.format(len(funding_records)))
print('Loaded {0} civic documents with Spring 2022 references'.format(len(spring_docs)))

# Create funding lookup by project name
funding_lookup = {}
for record in funding_records:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[proj_name] = amount

print('Created funding lookup with {0} entries'.format(len(funding_lookup)))

# Extract Spring 2022 projects from civic documents
spring_2022_projects = set()

for doc in spring_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Look for Spring 2022 mention
        if 'Spring 2022' in line or '2022-Spring' in line:
            # Look backwards for project name
            for j in range(i-1, max(0, i-5), -1):
                prev_line = lines[j].strip().replace('•', '').replace('·', '')
                if prev_line and len(prev_line) > 3:
                    # Check if this is likely a project name
                    project_keywords = ['project', 'improvements', 'repairs', 'construction', 'installation', 'upgrades', 'renovation', 'replacement']
                    has_keyword = any(kw in prev_line.lower() for kw in project_keywords)
                    
                    # Check title case
                    words = prev_line.split()
                    if words:
                        capitalized = sum(1 for w in words if w and w[0].isupper())
                        capital_ratio = capitalized / len(words) if len(words) > 0 else 0
                        is_title_case = capital_ratio > 0.4
                        
                        if has_keyword or is_title_case:
                            spring_2022_projects.add(prev_line)
                            break

print('Found {0} unique Spring 2022 projects in documents'.format(len(spring_2022_projects)))

# Normalize project names for matching
def normalize(name):
    import re
    # Extract base name before parentheses, convert to lowercase, remove special chars
    base = name.split('(')[0].strip()
    return re.sub(r'[^a-z0-9\s]', '', base.lower())

# Match projects with funding
matched_projects = {}

for spring_proj in spring_2022_projects:
    # Direct exact match
    if spring_proj in funding_lookup:
        matched_projects[spring_proj] = funding_lookup[spring_proj]
        continue
    
    # Try normalized base name match
    spring_normalized = normalize(spring_proj)
    
    for funded_proj, amount in funding_lookup.items():
        funded_normalized = normalize(funded_proj)
        if spring_normalized == funded_normalized:
            matched_projects[funded_proj] = amount
            break
        
        # Also check if one contains the other
        if spring_normalized in funded_normalized or funded_normalized in spring_normalized:
            if len(spring_normalized) > 10:  # Avoid short matches
                matched_projects[funded_proj] = amount
                break

print('Matched {0} projects with funding data'.format(len(matched_projects)))

# Calculate totals
total_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

print('\n{0}'.format('='*60))
print('SPRING 2022 PROJECTS: {0}'.format(total_projects))
print('TOTAL FUNDING: ${0:,}'.format(total_funding))
print('{0}'.format('='*60))

for proj_name, amount in matched_projects.items():
    print('• {0}: ${1:,}'.format(proj_name, amount))

# Format final result
result = {
    'total_projects': total_projects,
    'total_funding': total_funding,
    'projects': [{'name': proj, 'funding': amt} for proj, amt in matched_projects.items()]
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)

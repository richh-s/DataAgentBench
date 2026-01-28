code = """import json, os, re, sys

# Load funding data
funding_file = locals()['var_functions.query_db_48']
civic_file = locals()['var_functions.query_db_2']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Create funding lookup dictionary
funding_map = {}
for item in funding_data:
    proj_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_map[proj_name] = amount

# Find projects with Spring 2022 start dates
spring_2022_projects = set()

# Process each document
for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Iterate through lines to find Spring 2022 mentions
    for i in range(len(lines)):
        line = lines[i]
        # Look for Spring 2022 in the line
        if 'Spring 2022' in line or '2022-Spring' in line:
            # Search backwards for the project name
            for j in range(i-1, max(0, i-4), -1):
                prev_line = lines[j].strip()
                # Remove bullet points and special characters
                prev_line = prev_line.replace('·', '').replace('•', '').replace('+', '').strip()
                
                # Skip empty lines
                if not prev_line:
                    continue
                
                # Skip lines that are too long to be project names
                if len(prev_line) > 150:
                    continue
                
                # Check if this is likely a project name
                project_keywords = ['project', 'improvements', 'repairs', 'repaving', 'installation', 'construction', 'upgrades', 'renovation', 'replacement']
                has_project_keyword = any(kw in prev_line.lower() for kw in project_keywords)
                
                # Title case check (many capitalized words)
                words = prev_line.split()
                if len(words) > 0:
                    capitalized_words = sum(1 for w in words if w and w[0].isupper())
                    capital_ratio = capitalized_words / len(words)
                    
                    # If it has project keywords OR high title case ratio, it's likely a project name
                    if has_project_keyword or capital_ratio > 0.4:
                        spring_2022_projects.add(prev_line)
                        break

# Match found projects with funding data
matched_projects = {}

for project_name in spring_2022_projects:
    # Direct exact match
    if project_name in funding_map:
        matched_projects[project_name] = funding_map[project_name]
    else:
        # Try to find similar project names (base name match)
        for funded_project, amount in funding_map.items():
            # Extract base names (before parentheses)
            base_project = project_name.split('(')[0].strip().lower()
            base_funded = funded_project.split('(')[0].strip().lower()
            
            # Match if base names are identical or very similar
            if base_project == base_funded:
                matched_projects[funded_project] = amount
                break

# Calculate totals
total_count = len(matched_projects)
total_funding = sum(matched_projects.values())

# Display results
print('SPRING 2022 PROJECTS:', total_count)
print('TOTAL FUNDING: $'+str(total_funding))

for proj, amt in matched_projects.items():
    print('- '+proj+': $'+str(amt))

# Return structured result
output = {
    'total_projects': total_count,
    'total_funding': total_funding,
    'projects': [{'name': proj, 'funding': amt} for proj, amt in matched_projects.items()]
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)

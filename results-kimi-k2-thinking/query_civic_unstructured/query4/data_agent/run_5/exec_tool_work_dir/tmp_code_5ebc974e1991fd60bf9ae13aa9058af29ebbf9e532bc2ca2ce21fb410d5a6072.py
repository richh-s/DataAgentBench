code = """import json
import re

# Load data from files
civic_file = open('/tmp/tmp5.json', 'r')
funding_file = open('/tmp/tmp6.json', 'r')

civic_docs = json.load(civic_file)
funding_data = json.load(funding_file)

civic_file.close()
funding_file.close()

# Build funding lookup - aggregate by project name
funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name']
    # Convert amount to integer
    try:
        amount = int(str(record['Amount']).replace(',', '').strip())
    except:
        amount = 0
    
    if project_name in funding_lookup:
        funding_lookup[project_name] += amount
    else:
        funding_lookup[project_name] = amount

print("Funding lookup built with", len(funding_lookup), "projects")

# Find all projects that mention 2022 and Spring or have 2022 in their name
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Look for project name patterns (lines that are likely project names)
        if len(line) > 15 and not line.isupper() and not line.startswith('(') and 'cid:' not in line:
            # Check if next line contains project indicators
            if i + 1 < len(lines):
                next_line = lines[i+1].strip()
                if any(indicator in next_line for indicator in ['Updates:', 'Project Schedule:', 'Project Description:', 'Project Updates:']):
                    current_project = line
        
        # Look for 2022 Spring dates
        if '2022' in line and 'Spring' in line:
            if current_project:
                projects_2022.append(current_project)
                current_project = None
        
        # Also capture project names that contain 2022
        if '2022' in line and len(line.split()) > 2:
            # Skip if it's a schedule line
            if not any(schedule_word in line for schedule_word in ['Complete:', 'Begin:', 'Advertise:', 'Construction:', 'Design:']):
                if not line.startswith('(') and 'cid:' not in line and len(line) > 10:
                    projects_2022.append(line)

# Remove duplicates
unique_projects = list(dict.fromkeys(projects_2022))
print("Found", len(unique_projects), "projects related to 2022")

# Match with funding and filter for those with "Spring 2022" or likely Spring projects
total_funding = 0
matched_list = []

for project in unique_projects:
    # Direct exact match
    if project in funding_lookup:
        amount = funding_lookup[project]
        total_funding += amount
        matched_list.append({
            'project_name': project,
            'funding': amount,
            'match': 'exact'
        })
    else:
        # Try to find similar projects in funding (substring match)
        for funded_name in funding_lookup:
            if (project.lower() in funded_name.lower() or 
                funded_name.lower() in project.lower()):
                # More likely to be a match if the project name is substantial
                if len(project) > 15:
                    amount = funding_lookup[funded_name]
                    total_funding += amount
                    matched_list.append({
                        'project_name': project,
                        'funding': amount,
                        'match': 'partial',
                        'matched_name': funded_name
                    })
                    break

# Also check funding records with "2022" in the name
for funded_name, amount in funding_lookup.items():
    if '2022' in funded_name:
        # Don't double count already matched
        already_matched = any(m['project_name'] == funded_name for m in matched_list)
        if not already_matched:
            # Check if it's likely a Spring 2022 project based on name
            if 'Morning View' in funded_name or 'Annual' in funded_name:
                total_funding += amount
                matched_list.append({
                    'project_name': funded_name,
                    'funding': amount,
                    'match': 'funding_record'
                })

result = {
    'count': len(matched_list),
    'total_funding': total_funding,
    'projects': matched_list
}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json'}

exec(code, env_args)

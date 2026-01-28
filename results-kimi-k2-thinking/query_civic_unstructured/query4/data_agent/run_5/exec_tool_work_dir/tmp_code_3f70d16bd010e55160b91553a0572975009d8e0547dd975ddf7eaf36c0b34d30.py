code = """import json
import re

# Load the data from the files stored from previous queries
civic_docs_path = var_functions.query_db:44
funding_path = var_functions.query_db:31

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup - sum amounts for same project names
funding_lookup = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[proj_name] = funding_lookup.get(proj_name, 0) + amount

print('Funding lookup built with', len(funding_lookup), 'projects')

# Extract projects and their dates from civic docs
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if this looks like a project name (standalone, capitalized, not a header)
        if (len(line) > 15 and not line.isupper() and 
            not line.startswith('(') and 'cid:' not in line and
            not any(line.endswith(x) for x in [':', '.']) and
            not any(line.startswith(x) for x in ['To:', 'From:', 'Date:', 'Subject:', 'RECOMMENDED', 'DISCUSSION:'])):
            
            # Check if next line contains schedule indicators
            if i + 1 < len(lines):
                next_line = lines[i+1].strip()
                if any(marker in next_line for marker in ['Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Project Description:']):
                    current_project = line
                    
        # Look for Spring 2022 in schedule lines
        if current_project and ('2022' in line and 'Spring' in line):
            projects.append(current_project)
            current_project = None
            
        # Also check for project names containing 2022
        if '2022' in line and len(line.split()) > 2:
            # Skip if it's a schedule line
            if not any(marker in line for marker in ['Complete', 'Begin', 'Advertise', 'Construction', 'Design:']):
                if not line.startswith('(') and 'cid:' not in line:
                    projects.append(line)

# Remove duplicates from the projects list
unique_projects = list(dict.fromkeys(projects))

print('Projects found mentioning 2022+Spring or with 2022 in name:', len(unique_projects))
print('Sample projects:', unique_projects[:5])

# Match with funding
total_funding = 0
matched_projects = []

for project in unique_projects:
    # Clean up project name for matching
    clean_project = project.strip()
    
    # Direct match
    if clean_project in funding_lookup:
        amount = funding_lookup[clean_project]
        total_funding += amount
        matched_projects.append({'name': clean_project, 'funding': amount, 'match_type': 'exact'})
    else:
        # Try partial match - look for projects containing this name
        for funded_name in funding_lookup:
            # Check if project name appears within funded name, or vice versa
            if (clean_project.lower() in funded_name.lower() or 
                funded_name.lower().startswith(clean_project.lower()[:20])):
                # Additional check: avoid matching very short names
                if len(clean_project) > 10:
                    amount = funding_lookup[funded_name]
                    total_funding += amount
                    matched_projects.append({
                        'name': clean_project, 
                        'funding': amount, 
                        'match_type': 'partial',
                        'matched_to': funded_name
                    })
                    break

# Also check funding records that have 2022 in their name
for funded_name, amount in funding_lookup.items():
    if '2022' in funded_name:
        # Check if we haven't already matched this
        already_matched = any(m.get('matched_to') == funded_name or m['name'] == funded_name 
                             for m in matched_projects)
        if not already_matched:
            total_funding += amount
            matched_projects.append({
                'name': funded_name,
                'funding': amount,
                'match_type': 'from_funding'
            })

# Final result
result = {
    'count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects[:10]  # Limit output size
}

print('FINAL RESULT:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)

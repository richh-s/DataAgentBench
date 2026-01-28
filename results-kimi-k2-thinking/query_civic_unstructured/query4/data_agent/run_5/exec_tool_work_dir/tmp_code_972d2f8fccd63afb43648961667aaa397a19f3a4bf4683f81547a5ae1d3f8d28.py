code = """import json
import re

# Load the data from files
civic_docs = json.load(open('/tmp/tmp1.json'))
funding_data = json.load(open('/tmp/tmp2.json'))

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Build funding lookup
funding_lookup = {}
for fund in funding_data:
    proj_name = fund['Project_Name']
    amount = int(fund['Amount'])
    if proj_name not in funding_lookup:
        funding_lookup[proj_name] = 0
    funding_lookup[proj_name] += amount

print(f"Funding lookup built with {len(funding_lookup)} projects")

# Extract projects with dates
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for date patterns that indicate project schedules
        # Pattern: Word + Year (e.g., "Spring 2022", "Summer 2023")
        year_season_patterns = re.findall(r'(Spring|Summer|Fall|Winter)\s+(202[0-9])', line, re.IGNORECASE)
        
        if year_season_patterns:
            for season, year in year_season_patterns:
                if year == '2022' and season.lower() == 'spring':
                    # Found a Spring 2022 reference, now find the project name
                    # Look backwards for the project name (usually 1-3 lines before)
                    project_name = None
                    for j in range(i-1, max(0, i-5), -1):
                        prev_line = lines[j].strip()
                        if prev_line and not prev_line.startswith('(') and not prev_line.startswith('cid:'):
                            if len(prev_line) > 10 and not any(x in prev_line.lower() for x in ['updates:', 'project schedule:', 'estimated schedule:', 'complete design:', 'begin construction:', 'advertise:', 'complete construction:']):
                                project_name = prev_line
                                break
                    
                    if project_name:
                        spring_2022_projects.append(project_name)

# Remove duplicates while preserving order
unique_projects = []
seen = set()
for proj in spring_2022_projects:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

print(f"Found {len(unique_projects)} unique projects with Spring 2022 dates")

# Match with funding
total_funding = 0
matched_projects = []

for project_name in unique_projects:
    # Direct match
    if project_name in funding_lookup:
        amount = funding_lookup[project_name]
        total_funding += amount
        matched_projects.append({'name': project_name, 'funding': amount, 'match_type': 'exact'})
    else:
        # Try partial matching - look for projects containing this name or vice versa
        best_match = None
        best_amount = 0
        
        for funded_proj, amount in funding_lookup.items():
            # Check if one is substring of the other
            if (project_name.lower() in funded_proj.lower() or 
                funded_proj.lower() in project_name.lower()):
                if amount > best_amount:
                    best_amount = amount
                    best_match = funded_proj
        
        if best_match:
            total_funding += best_amount
            matched_projects.append({'name': project_name, 'funding': best_amount, 'match_type': 'partial', 'matched_to': best_match})

# Print results
result = {
    'count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

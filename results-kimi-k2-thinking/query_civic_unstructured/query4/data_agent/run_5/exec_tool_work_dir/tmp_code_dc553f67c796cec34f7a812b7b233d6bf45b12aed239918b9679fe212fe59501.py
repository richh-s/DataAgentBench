code = """import json
import re

# Load data
civic_file = open('/tmp/tmp1.json', 'r')
funding_file = open('/tmp/tmp2.json', 'r')

civic_docs = json.load(civic_file)
funding_data = json.load(funding_file)

civic_file.close()
funding_file.close()

# Build funding lookup
funding_lookup = {}
for record in funding_data:
    funding_lookup[record['Project_Name']] = int(record['Amount'])

# Find projects with Spring 2022
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Find all Spring 2022 mentions and capture surrounding context
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'Spring 2022' in line or '2022-Spring' in line:
                # Look backward to find project name (up to 5 lines)
                project_name = None
                for j in range(i-1, max(-1, i-6), -1):
                    candidate = lines[j].strip()
                    if candidate and len(candidate) > 10:
                        # Skip common markers
                        skip = False
n                        for marker in ['(', 'cid:', 'Updates:', 'Schedule:', 'Project Schedule:', 'Estimated Schedule:']:
                            if marker in candidate:
                                skip = True
                                break
                        if not skip and not candidate.isupper():
                            project_name = candidate
                            break
                
                if project_name:
                    spring_projects.append(project_name)

# Remove duplicates
unique_projects = list(dict.fromkeys(spring_projects))

# Match with funding
total = 0
matches = []

for project in unique_projects:
    if project in funding_lookup:
        amount = funding_lookup[project]
        total += amount
        matches.append({'project': project, 'funding': amount, 'type': 'exact'})
    else:
        # Try flexible matching
        for funded_name, amount in funding_lookup.items():
            # Check if names are similar
            proj_lower = project.lower()
            fund_lower = funded_name.lower()
            
            # Check for substring match
            if proj_lower in fund_lower or fund_lower in proj_lower:
                # Additional check to avoid false matches
                if len(proj_lower) > 15 or len(fund_lower) > 15:
                    total += amount
                    matches.append({'project': project, 'funding': amount, 'type': 'partial', 'matched': funded_name})
                    break

# Print result
result = {
    'count': len(matches),
    'total_funding': total,
    'projects': matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)

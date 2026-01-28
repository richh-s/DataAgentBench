code = """import json
import re

# Load the data
with open(var_functions.query_db:2, 'r') as f:
    all_docs = json.load(f)

with open(var_functions.query_db:12, 'r') as f:
    funding_data = json.load(f)

print('Documents:', len(all_docs))
print('Funding records:', len(funding_data))

# Build funding lookup
funding = {}
for record in funding_data:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding[name] = amount

# Look for Spring 2022 projects
spring_projects = []

# Check documents with 2022 in filename first
for doc in all_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Look for project names and schedules
    if '2022' in text:
        # Search for patterns like "Project Name" followed by schedule info
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip empty lines and bullets
            if len(line) < 5 or line.startswith('('):
                continue
            
            # Check if next lines contain Spring 2022
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].lower()
                
                # Spring 2022 patterns
                if 'spring 2022' in next_line or '2022-spring' in next_line:
                    if line in funding:
                        spring_projects.append({
                            'name': line,
                            'funding': funding[line]
                        })
                        break
                
                # March 2022
                if 'march 2022' in next_line or '2022-march' in next_line or '2022-03' in next_line:
                    if line in funding:
                        spring_projects.append({
                            'name': line,
                            'funding': funding[line]
                        })
                        break
                
                # April 2022
                if 'april 2022' in next_line or '2022-april' in next_line or '2022-04' in next_line:
                    if line in funding:
                        spring_projects.append({
                            'name': line,
                            'funding': funding[line]
                        })
                        break
                
                # May 2022
                if 'may 2022' in next_line or '2022-may' in next_line or '2022-05' in next_line:
                    if line in funding:
                        spring_projects.append({
                            'name': line,
                            'funding': funding[line]
                        })
                        break

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in spring_projects:
    if proj['name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['name'])

# Count and sum funding
count = len(unique_projects)
total_funding = sum(p['funding'] for p in unique_projects)

print('Spring 2022 projects found:', count)
print('Total funding:', total_funding)

# Also check for specific known projects like Morning View
if '2022 Morning View Resurfacing & Storm Drain Improvements' in funding:
    mv_funding = funding['2022 Morning View Resurfacing & Storm Drain Improvements']
    print('Morning View project funding: %d' % mv_funding)
    # Add if not already in list
    if not any('Morning View' in p['name'] for p in unique_projects):
        unique_projects.append({
            'name': '2022 Morning View Resurfacing & Storm Drain Improvements',
            'funding': mv_funding
        })
        count = len(unique_projects)
        total_funding = sum(p['funding'] for p in unique_projects)

result = {
    'count': count,
    'total_funding': total_funding,
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

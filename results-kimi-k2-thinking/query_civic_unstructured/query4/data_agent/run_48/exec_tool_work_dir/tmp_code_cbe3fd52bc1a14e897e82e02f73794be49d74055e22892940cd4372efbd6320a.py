code = """import json
import re

# Load data from the stored results
funding_file = open('var_functions.query_db:8', 'r')
funding_data = json.load(funding_file)
funding_file.close()

civic_file = open('var_functions.query_db:14', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Build funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    name = item.get('Project_Name', '')
    if name:
        funding_lookup[name] = {
            'amount': int(item.get('Amount', 0)),
            'source': item.get('Funding_Source', '')
        }

# Find all projects with 2022 in their names from funding data
# These are highly likely to be 2022 projects
projects_2022_from_funding = []
for name, info in funding_lookup.items():
    if '2022' in name and info['amount'] > 0:
        projects_2022_from_funding.append({
            'name': name,
            'funding': info['amount'],
            'source': info['source']
        })

print('\nProjects with 2022 in name from funding data:')
for p in projects_2022_from_funding:
    print('-', p['name'], ': $', p['funding'])

# Now search civic documents for Spring 2022 projects
spring_2022_from_docs = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
            
        # Skip headers and control lines
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in ['page', 'agenda item', 'public works commission', 'capital improvement projects']):
            continue
            
        if any(phrase in line_lower for phrase in ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'estimated schedule:']):
            continue
            
        # Look for project names (title case or mixed case, not bullet points)
        if (not line.startswith(('(', '-', '•', '·')) and 
            (line.istitle() or (sum(1 for c in line if c.isupper()) >= 3 and not line.isupper()))):
            
            # Look ahead for Spring 2022 dates
            for j in range(i, min(i+15, len(lines))):
                context_line = lines[j].strip()
                
                # Check for 2022 with Spring or March/April/May
                if '2022' in context_line:
                    if any(indicator in context_line for indicator in ['Spring', 'March', 'April', 'May']):
                        spring_2022_from_docs.append(line)
                        break
                    if any(month in context_line for month in ['2022-03', '2022-04', '2022-05']):
                        spring_2022_from_docs.append(line)
                        break

# Remove duplicates
spring_2022_from_docs = list(set(spring_2022_from_docs))

print('\nSpring 2022 projects found in civic documents:')
for proj in spring_2022_from_docs:
    print('-', proj)

# Match civic doc projects with funding
matched_from_docs = []
for project_name in spring_2022_from_docs:
    # Direct match
    if project_name in funding_lookup:
        info = funding_lookup[project_name]
        matched_from_docs.append({
            'name': project_name,
            'funding': info['amount'],
            'source': info['source']
        })
    else:
        # Partial match for substantial names
        if len(project_name) > 15:
            for fund_name, info in funding_lookup.items():
                if project_name.lower() in fund_name.lower() or fund_name.lower() in project_name.lower():
                    matched_from_docs.append({
                        'name': project_name,
                        'matched_fund': fund_name,
                        'funding': info['amount'],
                        'source': info['source']
                    })
                    break

print('\nMatched civic doc projects with funding:')
for p in matched_from_docs:
    print('-', p['name'], ': $', p['funding'])

# Combine results - use funding data as primary source since it's more reliable
# The projects with 2022 in their names are most likely to be Spring 2022 projects
all_spring_2022_projects = projects_2022_from_funding.copy()

# Add any additional matches from documents that aren't already included
existing_names = set(p['name'] for p in all_spring_2022_projects)

for p in matched_from_docs:
    proj_name = p.get('name') or p.get('matched_fund')
    if proj_name not in existing_names:
        all_spring_2022_projects.append(p)
        existing_names.add(proj_name)

# Calculate final totals
total_funding = sum(p['funding'] for p in all_spring_2022_projects)
project_count = len(all_spring_2022_projects)

print('\n=== FINAL RESULTS ===')
print('Total Spring 2022 projects:', project_count)
print('Total funding: $', total_funding)

print('\nAll Spring 2022 projects:')
for p in all_spring_2022_projects:
    print('-', p['name'], ': $', p['funding'], '(', p.get('source', ''), ')')

result = {
    'project_count': project_count,
    'total_funding': total_funding,
    'projects': all_spring_2022_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': [], 'var_functions.list_db:66': ['civic_docs'], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json'}

exec(code, env_args)

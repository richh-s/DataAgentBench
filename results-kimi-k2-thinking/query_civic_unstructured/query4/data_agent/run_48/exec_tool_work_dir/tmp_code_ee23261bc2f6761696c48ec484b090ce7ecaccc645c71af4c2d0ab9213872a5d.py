code = """import json
import re

# Load funding data
funding_file = open('var_functions.query_db:8', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Load civic documents  
civic_file = open('var_functions.query_db:14', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Build funding lookup by project name
funding_lookup = {}
for item in funding_data:
    name = item.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(item.get('Amount', 0))

# Find Spring 2022 projects from civic documents
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
            
        # Skip headers and footers
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in ['page', 'agenda item', 'public works commission']):
            continue
            
        # Skip schedule/control lines
        if any(phrase in line_lower for phrase in ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'estimated schedule:']):
            continue
            
        # Check if line looks like a project name (title case or mixed case, not bullet points)
        if (not line.startswith(('(', '-', '•', '·')) and 
            (line.istitle() or (sum(1 for c in line if c.isupper()) >= 3 and not line.isupper()))):
            
            # Look ahead for Spring 2022 date indicators
            has_spring_2022 = False
            for j in range(i, min(i+15, len(lines))):
                context_line = lines[j].strip()
                
                # Check for 2022 with Spring or March/April/May indicators
                if '2022' in context_line:
                    if any(indicator in context_line for indicator in ['Spring', 'March', 'April', 'May']):
                        has_spring_2022 = True
                        break
                    # Also check for 2022-03, 2022-04, 2022-05 formats
                    if any('2022-' + month in context_line for month in ['03', '04', '05']):
                        has_spring_2022 = True
                        break
            
            if has_spring_2022:
                spring_2022_projects.append(line)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

print('\nFound', len(spring_2022_projects), 'Spring 2022 projects from civic docs')
for proj in spring_2022_projects:
    print('-', proj)

# Match projects with funding and calculate totals
matched_projects = []
total_funding = 0

for project_name in spring_2022_projects:
    # Direct exact match
    if project_name in funding_lookup:
        amount = funding_lookup[project_name]
        total_funding += amount
        matched_projects.append({'name': project_name, 'funding': amount})
    else:
        # Try partial match for substantial project names
        if len(project_name) > 15:
            for fund_name, amount in funding_lookup.items():
                if (project_name.lower() in fund_name.lower() or fund_name.lower() in project_name.lower()):
                    total_funding += amount
                    matched_projects.append({'name': project_name, 'matched_fund': fund_name, 'funding': amount})
                    break

# Also include projects that have 2022 in their funding name (strong indicator of 2022 start)
additional_2022 = []
for fund_name, amount in funding_lookup.items():
    if '2022' in fund_name and amount > 0:
        # Check if not already counted
        if not any(p.get('name') == fund_name or p.get('matched_fund') == fund_name for p in matched_projects):
            additional_2022.append({'name': fund_name, 'funding': amount})
            total_funding += amount

# Combine all projects
all_matched_projects = matched_projects + additional_2022

print('\nFinal matched projects:', len(all_matched_projects))
for p in all_matched_projects:
    print('-', p['name'], ': $', p['funding'])

print('\nTotal Spring 2022 projects:', len(all_matched_projects))
print('Total funding: $', total_funding)

result = {
    'project_count': len(all_matched_projects),
    'total_funding': total_funding,
    'projects': all_matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': [], 'var_functions.list_db:66': ['civic_docs'], 'var_functions.list_db:68': ['civic_docs']}

exec(code, env_args)

code = """import json, os, re, sys

# Find data files in current directory
files = os.listdir('.')
funding_file = None
civic_file = None

for filename in files:
    if 'query_db' in filename:
        # Funding queries have been 14, 28, 44, 46
        if any(str(num) in filename for num in [14, 28, 44, 46]):
            funding_file = filename
        else:
            civic_file = filename

# Load funding data
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open(civic_file, 'r') as f:
    civic_documents = json.load(f)

print('Loaded', len(funding_records), 'funding records')
print('Loaded', len(civic_documents), 'civic documents')

# Create funding lookup by project name
funding_dict = {}
for record in funding_records:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_dict[project_name] = amount

print('Funding dictionary created with', len(funding_dict), 'entries')

# Find Spring 2022 projects in civic documents
spring_projects = []
spring_patterns = ['2022-Spring', '2022 March', '2022 April', '2022 May', '2022-March', '2022-April', '2022-May', 'Spring 2022', 'March 2022', 'April 2022', 'May 2022']

for doc in civic_documents:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check if document contains Spring 2022 dates
    has_spring_date = False
    for pattern in spring_patterns:
        if pattern.lower() in text_lower:
            has_spring_date = True
            break
    
    if has_spring_date:
        # Look for project names near those dates
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            # Skip empty/short lines and common headers
            if not line or len(line) < 10:
                continue
            if line.startswith('Page') or 'Agenda Item' in line or 'Public Works Commission' in line:
                continue
                
            # Check if line looks like a project name
            if line.istitle() or (len(line.split()) >= 3 and line[0].isupper() and not line.isupper()):
                # Look ahead for spring dates in context
                context = ' '.join(lines[i:i+8])
                context_lower = context.lower()
                
                for pattern in spring_patterns:
                    if pattern.lower() in context_lower:
                        # Add if not already found
                        existing_names = [p['name'] for p in spring_projects]
                        if line not in existing_names:
                            spring_projects.append({'name': line, 'context': context[:100]})
                        break

print('Potential Spring 2022 projects found:', len(spring_projects))

# Match Spring projects with funding data
matched_projects = []
total_funding = 0

for proj in spring_projects:
    project_name = proj['name']
    
    # Exact match
    if project_name in funding_dict:
        amount = funding_dict[project_name]
        matched_projects.append([project_name, amount, 'exact'])
        total_funding += amount
    else:
        # Partial/fuzzy match
        for funded_name, amount in funding_dict.items():
            proj_lower = project_name.lower()
            funded_lower = funded_name.lower()
            
            # Check if one name contains the other
            if proj_lower in funded_lower or funded_lower in proj_lower:
                # Avoid matching very short or generic names
                if len(project_name) > 15 and len(funded_name) > 15:
                    matched_projects.append([project_name, amount, 'partial', funded_name])
                    total_funding += amount
                    break

print('Projects with funding matched:', len(matched_projects))
print('Total funding calculated:', total_funding)

# Create result
project_count = len(matched_projects)
funding_formatted = '{:,}'.format(total_funding)

print('\n__RESULT__:')
print('Projects started in Spring 2022: ' + str(project_count) + '. Total funding: $' + funding_formatted)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)

code = """import json, os, re

# Find the data files in current directory
files = os.listdir('.')
funding_file = None
civic_file = None

for filename in files:
    if 'query_db' in filename:
        # Funding queries have IDs 14, 28, 44, 46
        if any(str(num) in filename for num in [14, 28, 44, 46]):
            funding_file = filename
        else:
            civic_file = filename

print('Found funding file:', funding_file)
print('Found civic file:', civic_file)

# Load funding data
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents data
with open(civic_file, 'r') as f:
    civic_documents = json.load(f)

print('Total funding records:', len(funding_records))
print('Total civic documents:', len(civic_documents))

# Create lookup dictionary for project funding
funding_map = {}
for record in funding_records:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Search patterns for Spring 2022 dates
spring_patterns = ['2022-Spring', '2022 March', '2022 April', '2022 May', 'Spring 2022', 'March 2022', 'April 2022', 'May 2022']

# Find Spring 2022 projects in civic documents
spring_projects = []

for doc in civic_documents:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check if document mentions Spring 2022 dates
    has_spring_date = False
    for pattern in spring_patterns:
        if pattern.lower() in text_lower:
            has_spring_date = True
            break
    
    if has_spring_date:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line or len(line) < 10:
                continue
            if line.startswith('Page') or 'Agenda Item' in line:
                continue
                
            # Check if this looks like a project name
            is_project_name = False
            if line.istitle() and len(line.split()) >= 3:
                is_project_name = True
            elif line[0].isupper() and len(line.split()) >= 4:
                is_project_name = True
                
            if is_project_name:
                # Look for spring date in context
                context = ' '.join(lines[i:i+8])
                context_lower = context.lower()
                
                for pattern in spring_patterns:
                    if pattern.lower() in context_lower:
                        # Add project if not already found
                        project_names = [p['name'] for p in spring_projects]
                        if line not in project_names:
                            spring_projects.append({'name': line})
                        break

print('Spring 2022 projects identified:', len(spring_projects))

# Match projects with funding
def match_projects(project_list, funding_dict):
    matched = []
    total_funds = 0
    
    for proj in project_list:
        project_name = proj['name']
        
        # Direct match
        if project_name in funding_dict:
            amount = funding_dict[project_name]
            matched.append([project_name, amount, 'exact'])
            total_funds += amount
        else:
            # Fuzzy match
            for funded_name, amount in funding_dict.items():
                proj_lower = project_name.lower()
                funded_lower = funded_name.lower()
                
                if proj_lower in funded_lower or funded_lower in proj_lower:
                    if len(proj_lower) > 10 and len(funded_lower) > 10:
                        matched.append([project_name, amount, 'partial', funded_name])
                        total_funds += amount
                        break
    
    return matched, total_funds

matched_projects, total_funding = match_projects(spring_projects, funding_map)

# Format final result
project_count = len(matched_projects)
funding_formatted = str(total_funding)

result = 'Projects started in Spring 2022: ' + str(project_count) + '. Total funding: $' + funding_formatted

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)

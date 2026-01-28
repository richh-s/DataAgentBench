code = """import json, re

# Read civic documents
civic_docs_file = '../var_functions.query_db:8'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read funding data  
funding_file = '../var_functions.query_db:10'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract all projects from text
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty and header lines
        if not line or '---' in line or 'Agenda Item' in line or 'Page' in line:
            continue
        
        # Detect potential project names
        if (5 < len(line) < 150 and line[0] not in '-*+([{' and
            'PROJECTS' not in line.upper() and i < len(lines)-1):
            
            next_line = lines[i+1].strip()
            if 'Updates:' in next_line or 'Project Schedule:' in next_line or 'Project Description:' in line:
                
                # Look ahead for status and dates
                status = 'unknown'
                et = None
                topics = []
                
                for j in range(i+1, min(i+15, len(lines))):
                    check = lines[j].strip()
                    
                    if 'completed' in check.lower() or 'Complete Construction:' in check:
                        status = 'completed'
                        year_match = re.search(r'\b202[0-9]\b', check)
                        if year_match:
                            et = year_match.group()
                    elif 'under construction' in check.lower() and status == 'unknown':
                        status = 'construction'
                    elif 'Complete Design:' in check and status == 'unknown':
                        status = 'design'
                    elif 'Not Started' in check and status == 'unknown':
                        status = 'not started'
                
                # Find topics from name
                name_lower = line.lower()
                if 'park' in name_lower:
                    topics.append('park')
                if 'road' in name_lower or 'street' in name_lower:
                    topics.append('road')
                if 'drain' in name_lower:
                    topics.append('drainage')
                if 'fema' in name_lower:
                    topics.append('FEMA')
                
                if topics:
                    all_projects.append({
                        'Project_Name': line,
                        'topics': ','.join(topics),
                        'status': status,
                        'et': et
                    })

# Filter park projects completed in 2022
park_projects_2022 = []
for p in all_projects:
    if 'park' in p['topics'] and p['status'] == 'completed' and p['et'] == '2022':
        park_projects_2022.append(p)

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# Find funding matches
total = 0
results = []

for project in park_projects_2022:
    proj_name = project['Project_Name']
    proj_key = proj_name.lower().replace(' ', '')
    
    amount = 0
    if proj_key in funding_lookup:
        amount = funding_lookup[proj_key]
    else:
        # Try without parentheses
        clean_key = re.sub(r'\(.*\)', '', proj_key).strip()
        if clean_key in funding_lookup:
            amount = funding_lookup[clean_key]
        else:
            # Fuzzy match
            proj_lower = proj_name.lower()
            for fund_name, fund_amount in funding_lookup.items():
                if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
                    amount = fund_amount
                    break
    
    if amount > 0:
        total += amount
        results.append({
            'project': proj_name,
            'amount': amount
        })

output = {
    'park_projects_2022': results,
    'count': len(results),
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

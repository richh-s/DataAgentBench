code = """import json

# Load the data from the stored file paths
civic_docs_file = open('/tmp/tmprp5f5z5k.json', 'r')
civic_docs = json.load(civic_docs_file)
civic_docs_file.close()

funding_file = open('/tmp/tmp0k5s9q8h.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Create a mapping from project name to funding amount
funding_map = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if proj_name:
        funding_map[proj_name] = amount

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding_data), 'funding records')
print('Funding map has', len(funding_map), 'entries')

# Find disaster projects that started in 2022 and have funding
total_funding = 0
matched_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Check if this is a disaster project (has FEMA/CalJPIA/CalOES indicators)
        is_disaster = False
        if line.find('(FEMA Project)') >= 0:
            is_disaster = True
        elif line.find('(CalJPIA Project)') >= 0:
            is_disaster = True
        elif line.find('(CalOES Project)') >= 0:
            is_disaster = True
        elif line.find('FEMA/CalOES Project') >= 0:
            is_disaster = True
        
        if is_disaster:
            project_name = line
            
            # Look for start date information in nearby lines (within 5 lines)
            found_2022_start = False
            context_start = max(0, i-2)
            context_end = min(len(lines), i+6)
            
            for j in range(context_start, context_end):
                context_line = lines[j].strip()
                lower_line = context_line.lower()
                
                # Check if this line contains both a start indicator and 2022
                if (lower_line.find('st:') >= 0 or lower_line.find('start:') >= 0) and context_line.find('2022') >= 0:
                    found_2022_start = True
                    break
            
            # If we found a 2022 start date, get the funding
            if found_2022_start:
                funding_amount = funding_map.get(project_name, 0)
                if funding_amount > 0:
                    total_funding += funding_amount
                    matched_projects.append({
                        'name': project_name,
                        'funding': funding_amount
                    })

# Output the result
print('Found', len(matched_projects), 'disaster projects that started in 2022')
print('Total funding:', total_funding)

result = {
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)

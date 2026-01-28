code = """import json

# Load civic documents
with open('/tmp/tmp2d2u8k1a.json', 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open('/tmp/tmp0k5s9q8h.json', 'r') as f:
    funding_data = json.load(f)

# Create funding lookup dictionary
funding_lookup = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_lookup[project_name] = amount

# Initialize tracking variables
total_funding = 0
found_projects = []

# Process each civic document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check if this is a disaster project (FEMA, CalJPIA, or CalOES)
        if '(FEMA Project)' in line or '(CalJPIA Project)' in line or '(CalOES Project)' in line or 'FEMA/CalOES Project' in line:
            project_name = line
            
            # Look for start date in the next few lines
            start_date = ''
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].strip()
                lower_line = next_line.lower()
                if 'st:' in lower_line or 'start:' in lower_line:
                    start_date = next_line
                    break
            
            # Check if project started in 2022
            if '2022' in start_date:
                amount = funding_lookup.get(project_name, 0)
                if amount > 0:
                    total_funding += amount
                    found_projects.append({
                        'name': project_name,
                        'amount': amount,
                        'start': start_date
                    })

# Prepare result
result = {
    'total_funding': total_funding,
    'project_count': len(found_projects),
    'projects': found_projects
}

# Print details
print('Found disaster projects that started in 2022:')
for p in found_projects:
    print(p['name'], ':', p['amount'])
print('Total funding:', total_funding)

# Output result
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

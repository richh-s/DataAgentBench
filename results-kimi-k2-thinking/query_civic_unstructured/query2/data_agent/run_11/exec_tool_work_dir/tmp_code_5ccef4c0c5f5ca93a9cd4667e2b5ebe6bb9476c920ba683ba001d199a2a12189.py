code = """import json, re, sys

# Load civic documents
civic_docs_path = var_functions.query_db:5
civic_docs = json.load(open(civic_docs_path))

# Load funding data
funding_path = var_functions.query_db:6
funding = json.load(open(funding_path))

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find project blocks that mention parks
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names containing "Park"
        if 'Park' in line and len(line) > 5:
            # Skip headers and metadata
            if any(skip in line for skip in ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Public Works', 'Commission']):
                continue
            if line.startswith('(') or line.startswith('cid'):
                continue
            
            # Check the next 15 lines for completion status and 2022 date
            next_lines = lines[i:i+15]
            next_text = ' '.join(next_lines)
            
            # Check if this project was completed in 2022
            if ('completed' in next_text.lower() or 'completion' in next_text.lower()) and '2022' in next_text:
                # Verify it's actually completed (not "to be completed")
                if not re.search(r'to be completed', next_text, re.IGNORECASE):
                    park_projects_2022.append(line)

# Remove duplicates
unique_park_projects = list(set(park_projects_2022))

# Find funding for these projects from the funding table
funding_matches = []
total_funding = 0

# Also check for partial matches (e.g., "Bluffs Park" matches "Bluffs Park Shade Structure")
for park_project in unique_park_projects:
    for fund_rec in funding:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        # Check for exact match or if park project name is part of funding project name
        if (park_project.lower() == fund_name.lower() or 
            park_project.lower() in fund_name.lower()):
            funding_matches.append({
                'park_project': park_project,
                'funding_name': fund_name,
                'amount': fund_amount
            })
            total_funding += fund_amount

# Format the result
result = {
    'park_projects_completed_2022': unique_park_projects,
    'number_of_projects': len(unique_park_projects),
    'total_funding_dollars': total_funding,
    'funding_breakdown': funding_matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)

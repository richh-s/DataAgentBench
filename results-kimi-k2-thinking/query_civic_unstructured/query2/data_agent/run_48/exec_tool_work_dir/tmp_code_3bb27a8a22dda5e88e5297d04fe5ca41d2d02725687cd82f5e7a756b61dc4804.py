code = """import json

# Read funding data - it's directly available
funding_records = var_functions.query_db:0

# Read civic documents from file path
civic_file_path = locals()['var_functions.query_db:6']
with open(civic_file_path, 'r') as file:
    civic_docs = json.load(file)

print('Loaded %d funding records' % len(funding_records))
print('Loaded %d civic documents' % len(civic_docs))

# Identify park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) > 150:
            continue
        
        # Skip headings
        if 'capital improvement' in line.lower() or 'agenda' in line.lower() or 'page' in line.lower():
            continue
        
        # Look for park-related terms
        line_lower = line.lower()
        if 'park' in line_lower or 'playground' in line_lower or 'walkway' in line_lower:
            # Look for completion in 2022 in context
            context_start = max(0, i-3)
            context_end = min(len(lines), i+6)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if 'completed' in context and '2022' in context:
                # Avoid duplicates
                if not any(p['name'] == line for p in park_projects_2022):
                    park_projects_2022.append({'name': line})
                    print('Added project:', line)

print('Total park projects completed in 2022:', len(park_projects_2022))

# Match projects with funding records and calculate total
total_funding = 0
matched_projects = []

for proj in park_projects_2022:
    proj_name = proj['name']
    for fund in funding_records:
        if fund['Project_Name'] == proj_name:
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({'project': proj_name, 'amount': amount})
            print('Matched funding for:', proj_name, '-', amount)

result = {
    'total_funding_2022': total_funding,
    'matched_projects': matched_projects,
    'park_projects_count': len(park_projects_2022)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

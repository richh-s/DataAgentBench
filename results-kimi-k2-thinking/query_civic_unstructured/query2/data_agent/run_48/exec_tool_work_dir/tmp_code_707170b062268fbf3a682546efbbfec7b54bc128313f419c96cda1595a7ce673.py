code = """import json

# Read the full civic documents from the file
civic_docs_path = var_functions.query_db:6
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Get funding data
funding_list = var_functions.query_db:0

print(f"Found {len(civic_docs)} civic documents")
print(f"Found {len(funding_list)} funding records")

# Look for park projects completed in 2022 in the text
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Search for park projects with completion in 2022
    search_text = text.lower()
    
    # Split into lines to find project names and their completion status
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if line and 'park' in line.lower():
            # Look around this line for completion info
            context_start = max(0, i-3)
            context_end = min(len(lines), i+5)
            context = '\n'.join(lines[context_start:context_end])
            
            if 'completed' in context.lower() and '2022' in context:
                park_projects_2022.append({
                    'project_name': line,
                    'context': context,
                    'filename': filename
                })

print(f"Found {len(park_projects_2022)} potential park projects completed in 2022")

for proj in park_projects_2022:
    print(f"\nProject: {proj['project_name']}")
    print(f"File: {proj['filename']}")
    print(f"Context: {proj['context'][:200]}...")

# Now try to match these with funding data
total_funding = 0
matched_projects = []

for park_proj in park_projects_2022:
    proj_name = park_proj['project_name']
    for fund in funding_list:
        if fund['Project_Name'].lower() == proj_name.lower():
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'project': proj_name,
                'amount': amount
            })
            print(f"\nMATCHED: {proj_name} - ${amount}")

result = {
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'park_projects_2022': len(park_projects_2022)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

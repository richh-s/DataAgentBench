code = """import json

# Load the funding data for park projects
funding_file = str(var_functions.query_db:19)
with open(funding_file, 'r') as f:
    park_funding = json.load(f)

# Load the civic docs that mention 2022 completions
civic_file = str(var_functions.query_db:18)  
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create lookup for park funding
funding_lookup = {item['Project_Name']: item for item in park_funding}

# Search through civic docs for park projects completed in 2022
completed_2022_parks = []
seen_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for park project names and completion in 2022
    for proj_name, funding_info in funding_lookup.items():
        if proj_name in seen_projects:
            continue
            
        # Check if project name appears in text
        if proj_name in text:
            # Check if it was completed in 2022
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if proj_name in line or (i > 0 and proj_name in lines[i-1]):
                    # Look for completion status in surrounding lines
                    for j in range(max(0, i-3), min(len(lines), i+4)):
                        check_line = lines[j]
                        if 'completed' in check_line.lower() and '2022' in check_line:
                            completed_2022_parks.append({
                                'Project_Name': proj_name,
                                'Funding_Source': funding_info['Funding_Source'],
                                'Amount': int(funding_info['Amount'])
                            })
                            seen_projects.add(proj_name)
                            break

# Calculate total funding
total_amount = sum(p['Amount'] for p in completed_2022_parks)

result = {
    'total_funding': total_amount,
    'number_of_projects': len(completed_2022_parks),
    'projects': completed_2022_parks
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}, {'Funding_ID': '94', 'Project_Name': 'Trancas Playground Resurfacing', 'Funding_Source': 'Impact Investment Fund', 'Amount': '90000'}]}

exec(code, env_args)
